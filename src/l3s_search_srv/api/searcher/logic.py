import ast, os, pathlib
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import regex as re
from flask_restx import Namespace
# from pyserini.search.lucene import LuceneSearcher
# from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
import faiss
from swagger_client import sse_search_client
from transformers import AutoTokenizer

from l3s_search_srv.api.encoder.logic import BertGermanCasedDenseEncoder, XlmRobertaDenseEncoder, DeBERTaDenseEncoder, \
    BertGermanUncasedDenseEncoder, BertMultiLingualUncasedDenseEncoder, BertMultiLingualCasedDenseEncoder, CrossRobertaSentenceTransformerEncoder

class EmbeddingCustomizer:
    ns_customizer = Namespace("CustomizedEmbedding", validate=True)
    sse_search_config = sse_search_client.Configuration()
    sse_search_config.host = os.getenv("SSE_SEARCH_HOST")
    client_sse_search = sse_search_client.ApiClient(sse_search_config)
    sse_search_user_api = sse_search_client.UserApi(client_sse_search)
    sse_search_learning_profile_api = sse_search_client.LearningProfilesApi(client_sse_search)
    sse_search_learning_history_api = sse_search_client.LearningHistoryApi(client_sse_search)
    sse_search_learning_unit_api = sse_search_client.LearningUnitsApi(client_sse_search)
    sse_search_learning_path_api = sse_search_client.LearningPathApi(client_sse_search)
    sse_search_skill_api = sse_search_client.SkillApi(client_sse_search)

    def __init__(self):
        pass

    def add_after(self, query, use_skill_profile, use_learning_profile, user_id, language_model, dataset_name,
                  index_method):
        searcher = Searcher()

        relevant_skills = []
        if not use_skill_profile and not use_learning_profile:
            ## case 1: not using skill profile and learning profile
            self.ns_customizer.logger.info("*** case 1: not using skill profile and learning profile ***")

        elif not use_skill_profile and use_learning_profile:
            ## case 2: not using skill profile but using learning profile
            # get the learning profile of the user
            self.ns_customizer.logger.info("*** case 2: not using skill profile but using learning profile ***")

            # retrieve user specific data
            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info:\n{user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id == '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info:\n{learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info:\n{learning_history}")

            started_learning_units = learning_history["started_learning_units"]
            started_learning_paths = learning_history["personal_paths"]

            # retrieve learning unit skills relevant to query
            relevant_skills = []

            for started_unit_id in started_learning_units:
                learning_unit = self.sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(
                    started_unit_id).to_dict()

                check_already_learned = lambda x: x not in relevant_skills
                teachingGoals = learning_unit["teaching_goals"]
                teachingGoals = list(filter(check_already_learned, teachingGoals))

                requiredSkills = learning_unit["required_skills"]
                requiredSkills = list(filter(check_already_learned, requiredSkills))

                all_skills = teachingGoals + requiredSkills

                relevant_skills += all_skills

            for started_path_id in started_learning_paths:
                learning_path = self.sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                    started_path_id).to_dict()

                check_already_learned = lambda x: x not in relevant_skills
                path_goals = learning_path["path_goals"]
                path_goals = list(filter(check_already_learned, path_goals))

                requirements = learning_path["requirements"]
                requirements = list(filter(check_already_learned, requirements))

                all_skills = path_goals + requirements

                relevant_skills += all_skills

            self.ns_customizer.logger.info(f"Relevant Skills:\n{relevant_skills}")

        elif use_skill_profile and not use_learning_profile:
            ## case 3: using skill profile but not learning profile
            # get the skill profile of the user
            self.ns_customizer.logger.info("*** case 3: using skill profile but not learning profile ***")

            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info:\n{user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id == '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id=learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info:\n{learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info:\n{learning_history}")

            learned_skills = learning_history["learned_skills"]

            # retrieve skills relevant to query
            relevant_skills = learned_skills
            self.ns_customizer.logger.info(f"Relevant Skills:\n{relevant_skills}")

        else:
            ## case 4: using both skill profile and learning profile
            # get the skill and learning profile of the user
            self.ns_customizer.logger.info("*** case 4: using both skill profile and learning profile ***")

            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info:\n{user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id == '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info:\n{learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info:\n{learning_history}")

            started_learning_units = learning_history["started_learning_units"]
            started_learning_paths = learning_history["personal_paths"]
            learned_skills = learning_history["learned_skills"]

            # retrieve skills relevant to query
            relevant_skills = learned_skills

            for started_unit_id in started_learning_units:
                learning_unit = self.sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(
                    started_unit_id).to_dict()

                check_already_learned = lambda x: x not in relevant_skills
                teachingGoals = learning_unit["teaching_goals"]
                teachingGoals = list(filter(check_already_learned, teachingGoals))

                requiredSkills = learning_unit["required_skills"]
                requiredSkills = list(filter(check_already_learned, requiredSkills))

                all_skills = teachingGoals + requiredSkills

                relevant_skills += all_skills

            for started_path_id in started_learning_paths:
                learning_path = self.sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                    started_path_id).to_dict()

                check_already_learned = lambda x: x not in relevant_skills
                path_goals = learning_path["path_goals"]
                path_goals = list(filter(check_already_learned, path_goals))

                requirements = learning_path["requirements"]
                requirements = list(filter(check_already_learned, requirements))

                all_skills = path_goals + requirements

                relevant_skills += all_skills
            self.ns_customizer.logger.info(f"Relevant Skills:\n{relevant_skills}")

        results = searcher.dense_retrieval(
            query=query,
            language_model=language_model,
            dataset_name=dataset_name,
            index_method=index_method
        )

        top_priority = []
        low_priority = []
        for result in results:
            if result["entity_id"] in relevant_skills:
                top_priority.append(result)
            else:
                low_priority.append(result)

        results = top_priority + low_priority
        return results

    def add_before(self, query, use_skill_profile, use_learning_profile, user_id, language_model, dataset_name,
                   index_method):
        searcher = Searcher()

        if not use_skill_profile and not use_learning_profile:
            ## case 1: not using skill profile and learning profile
            self.ns_customizer.logger.info("*** case 1: not using skill profile and learning profile ***")
            # !!No need to change anything in the query!!
            pass

        elif not use_skill_profile and use_learning_profile:
            ## case 2: not using skill profile but using learning profile
            self.ns_customizer.logger.info("*** case 2: not using skill profile but using learning profile ***")

            # retrieve user specific data
            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info: {user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id is '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info: {learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id is '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history}")

            started_learning_units = learning_history["started_learning_units"]
            started_learning_paths = learning_history["personal_paths"]
            learned_skills = learning_history["learned_skills"]

            # retrieve skills relevant to query
            relevant_skills = []
            for started_unit_id in started_learning_units:
                learning_unit = self.sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(
                    started_unit_id).to_dict()

                teachingGoals = learning_unit["teaching_goals"]
                requiredSkills = learning_unit["required_skills"]

                check_already_learned = lambda x: x in learned_skills
                teachingGoals = list(filter(check_already_learned, teachingGoals))
                requiredSkills = list(filter(check_already_learned, requiredSkills))
                all_skills = teachingGoals + requiredSkills
                learned_skills += all_skills

                relevant_skills += [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                    for
                                    skill_to_learn in all_skills]

            for started_path_id in started_learning_paths:
                learning_path = self.sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                    started_path_id).to_dict()

                check_already_learned = lambda x: x in relevant_skills
                path_goals = learning_path["path_goals"]
                path_goals = list(filter(check_already_learned, path_goals))

                requirements = learning_path["requirements"]
                requirements = list(filter(check_already_learned, requirements))

                all_skills = path_goals + requirements

                learned_skills += all_skills
                relevant_skills += [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                    for skill_to_learn in all_skills]
            self.ns_customizer.logger.info(f"Relevant Skills: {relevant_skills}")

            # get seperator token. Is it needed?
            sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

            # add skill names to query
            self.ns_customizer.logger.info(f"Original Query: {query}")
            for skill in relevant_skills:
                query += f"{sep_token}{skill['name']}"
            self.ns_customizer.logger.info(f"Final Query: {query}")

        elif use_skill_profile and not use_learning_profile:
            ## case 3: using skill profile but not learning profile
            self.ns_customizer.logger.info("*** case 3: using skill profile but not learning profile ***")

            # retrieve user specific data
            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info: {user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id is '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info: {learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id is '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history}")

            learned_skills = learning_history["learned_skills"]

            # retrieve skills relevant to query
            relevant_skills = [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill).to_dict() for skill in
                               learned_skills]
            self.ns_customizer.logger.info(f"Relevant Skills: {relevant_skills}")

            # get seperator token. Is it needed?
            sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

            # add skill names to query
            self.ns_customizer.logger.info(f"Original Query: {query}")
            for skill in relevant_skills:
                query += f"{sep_token}{skill['name']}"
            self.ns_customizer.logger.info(f"Final Query: {query}")

        else:
            ## case 4: using both skill profile and learning profile
            self.ns_customizer.logger.info("*** case 4: using both skill profile and learning profile ***")

            # retrieve user specific data
            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info: {user}")

            learning_profile_id = user["learning_profile"]
            if learning_profile_id is '':
                raise ValueError("User has no learningProfile")

            learning_profile = self.sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                learning_profile_id).to_dict()
            self.ns_customizer.logger.info(f"Learning Profile Info: {learning_profile}")

            learning_history_id = learning_profile["learning_history_id"]
            if learning_history_id is '':
                raise ValueError("Learning profile of user has no learning history")

            learning_history = self.sse_search_learning_history_api.learning_history_controller_get_learning_history(
                learning_history_id).to_dict()
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history}")

            started_learning_units = learning_history["started_learning_units"]
            started_learning_paths = learning_history["personal_paths"]
            learned_skills = learning_history["learned_skills"]

            # retrieve skills relevant to query
            relevant_skills = [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill).to_dict() for skill in
                               learned_skills]
            for started_unit_id in started_learning_units:
                learning_unit = self.sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(
                    started_unit_id).to_dict()

                teachingGoals = learning_unit[
                    "teaching_goals"]
                requiredSkills = learning_unit[
                    "required_skills"]

                check_already_learned = lambda x: x in learned_skills
                teachingGoals = list(filter(check_already_learned, teachingGoals))
                requiredSkills = list(filter(check_already_learned, requiredSkills))
                all_skills = teachingGoals + requiredSkills
                learned_skills += all_skills

                relevant_skills += [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                    for skill_to_learn in all_skills]

            for started_path_id in started_learning_paths:
                learning_path = self.sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                    started_path_id).to_dict()

                check_already_learned = lambda x: x in relevant_skills
                path_goals = learning_path["path_goals"]
                path_goals = list(filter(check_already_learned, path_goals))

                requirements = learning_path["requirements"]
                requirements = list(filter(check_already_learned, requirements))

                all_skills = path_goals + requirements

                learned_skills += all_skills
                relevant_skills += [self.sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                    for skill_to_learn in all_skills]
            self.ns_customizer.logger.info(f"Relevant Skills: {relevant_skills}")

            # get seperator token. Is it needed?
            sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

            # add skill names to query
            self.ns_customizer.logger.info(f"Original Query: {query}")
            for skill in relevant_skills:
                query += f"{sep_token}{skill['name']}"
            self.ns_customizer.logger.info(f"Final Query: {query}")

        results = searcher.dense_retrieval(
            query=query,
            language_model=language_model,
            dataset_name=dataset_name,
            index_method=index_method
        )

        return results

class Searcher(object):

    language_models = {
        "bert-base-german-cased": "dbmdz/bert-base-german-cased",
        "xlm-roberta-base": "xlm-roberta-base",
        "cross-en-de-roberta-sentence-transformer": "T-Systems-onsite/cross-en-de-roberta-sentence-transformer",
        "geberta-xlarge": "ikim-uk-essen/geberta-xlarge",
        "bert-base-german-uncased": "dbmdz/bert-base-german-uncased",
        "bert-base-multilingual-uncased": "google-bert/bert-base-multilingual-uncased",
        "bert-base-multilingual-cased": "google-bert/bert-base-multilingual-cased"
    }
    punctuation_marks = string.punctuation.replace("-", "")

    def __init__(self):
        self.BASE_INDEXES_DIR = os.getenv("BASE_INDEXES_DIR")

    # def traditional_retrieval(self, query, index_name, dataset_name):
    #     index_path = os.path.join(self.BASE_INDEXES_DIR, f"{index_name}/{dataset_name}")
    #     searcher = LuceneSearcher(index_path)
    #     hits = searcher.search(query)
    #     results=[]

    #     if hits:
    #         for i in range(0, len(hits)):
    #             temp = ast.literal_eval(hits[i].raw)
    #             temp['score'] = f'{hits[i].score:.4f}'
    #             results.append(temp)
    #     return results

    def sparse_retrieval(self):
        pass

    def dense_retrieval(self, query, language_model, index_method, dataset_name):
        # remove the punctuations from the query
        # query = re.sub(r"\p{P}(?<!-)", "", query)
        query = query.translate(str.maketrans('', '', self.punctuation_marks))

        print(query)
        encodes_file_path = os.path.join(os.getenv("BASE_ENCODES_DIR"),
                                         f"dense/{language_model}/{dataset_name}/data_encoded.json")
        prebuilt_index_path = os.path.join(os.getenv("BASE_INDEXES_DIR"),
                                           f"{index_method}/{dataset_name}/dense/{language_model}/")

        print(encodes_file_path)
        print(prebuilt_index_path)

        if language_model not in self.language_models.keys():
            raise ValueError("language model not defined")

        if index_method not in ["flat-l2", "flat-ip", "hnsw", "pq"]:
            raise ValueError("index method not defined")

        # load index
        if not os.path.exists(prebuilt_index_path):
            # print(prebuilt_index_path)
            raise ValueError("index path not exists")

        index = faiss.read_index(os.path.join(prebuilt_index_path, "index.faiss"))
        if language_model == "bert-base-german-cased":
            encoder = BertGermanCasedDenseEncoder()
        elif language_model == "cross-en-de-roberta-sentence-transformer":
            encoder = CrossRobertaSentenceTransformerEncoder()
        elif language_model == "xlm-roberta-base":
            encoder = XlmRobertaDenseEncoder()
        elif language_model == "geberta-xlarge":
            encoder = DeBERTaDenseEncoder()
        elif language_model == "bert-base-german-uncased":
            encoder = BertGermanUncasedDenseEncoder()
        elif language_model == "bert-base-multilingual-uncased":
            encoder = BertMultiLingualUncasedDenseEncoder()
        elif language_model == "bert-base-multilingual-cased":
            encoder = BertMultiLingualCasedDenseEncoder()
        else:
            raise ValueError("search with the given language model is not implemented")

        query_enc = encoder.query_encoder(query)

        xq = np.float32(np.array([query_enc]))

        # data = []
        with open(encodes_file_path, "r") as file:
            data = json.load(file)

        with open(f"{prebuilt_index_path}/docid", "r") as f:
            docid = f.read()

        D, I = index.search(xq, len(data))

        # transform distances and indexes to list
        distance = [round(n, 2) for n in D[0].tolist()]
        indexes = I[0].tolist()

        results = []
        for i in indexes:
            results.append(data[i])

        # add distance to results
        for i in range(len(data)):
            results[i]["distance"] = distance[i]
            # results[i]["ranking"] = i+1
            results[i]["jaccard"] = self.__jaccard(query, results[i]["contents"])
            results[i]["cosine_similarity"] = self.__cosine_sim(query_enc, results[i]["vector"])

        # reranking the result
        rerank_category = ["jaccard", "cosine_similarity"]
        sorted_results = sorted(results, key=lambda x: x[rerank_category[1]], reverse=True)

        for item in sorted_results:
            item.pop("vector", None)

        return sorted_results

    def __cosine_sim(self, query, content):
        x = np.array(query).reshape(1, -1)
        y = np.array(content).reshape(1, -1)
        r = cosine_similarity(x, y)[0][0]
        return float("{:.4f}".format(r))

    def __jaccard(self, query, content):
        # if not type(x) == set or not type(y) == set:
        #     raise ValueError("input must be set.")

        # len(dataset.iloc[0]["task_text"].translate(str.maketrans('', '', string.punctuation)).split())
        query = query.lower()
        content = content.lower()

        x = set(query.translate(str.maketrans('', '', string.punctuation)).split())
        y = set(content.translate(str.maketrans('', '', string.punctuation)).split())

        n_shared = len(x.intersection(y))
        n_total = len(x.union(y))

        # return float("{:.2f}".format(n_shared/len(x)))
        return float("{:.2f}".format(n_shared/n_total))
