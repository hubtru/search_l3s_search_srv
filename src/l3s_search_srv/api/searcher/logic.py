import ast, os, pathlib
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import regex as re
# from pyserini.search.lucene import LuceneSearcher
# from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
import faiss
import swagger_client
from flask_restx import Namespace

from l3s_search_srv.api.encoder.logic import BertGermanCasedDenseEncoder, CrossRobertaSentenceTransformerEncoder


class EmbeddingCustomizer:
    ns_customizer = Namespace("CustomizedEmbedding", validate=True)
    sse_search_config = swagger_client.Configuration()
    sse_search_config.host = os.getenv("SSE_SEARCH_HOST")
    client_sse_search = swagger_client.ApiClient(sse_search_config)
    sse_search_user_api = swagger_client.UserApi(client_sse_search)
    sse_search_learning_profile_api = swagger_client.LearningProfilesApi(client_sse_search)
    sse_search_learning_history_api = swagger_client.LearningHistoryApi(client_sse_search)
    sse_search_learning_unit_api = swagger_client.LearningUnitsApi(client_sse_search)
    sse_search_learning_path_api = swagger_client.LearningPathApi(client_sse_search)
    sse_search_skill_api = swagger_client.SkillApi(client_sse_search)

    def __init__(self):
        pass

    def _get_skill_profile(self, learning_history_id):
        learned_skills = self.sse_search_learning_history_api.learning_history_controller_get_learned_skills(
            learning_history_id)
        return learned_skills

    def _get_learning_profile(self, learning_history_id):
        personalized_paths = self.sse_search_learning_history_api.learning_history_controller_get_personalized_paths(
            learning_history_id).to_dict()

        relevant_skills = []
        for personalized_path in personalized_paths["paths"]:
            personalized_path_id = personalized_path["personalized_path_id"]

            verbose_personalized_path = self.sse_search_learning_history_api.learning_history_controller_get_personalized_path(
                learning_history_id,
                personalized_path_id).to_dict()

            relevant_skills += verbose_personalized_path["goals"]
            learning_path_id = verbose_personalized_path.get("learning_path_id")
            if learning_path_id is not None:
                learning_path = self.sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                    learning_path_id).to_dict()

                relevant_skills += learning_path["path_goals"]

        return relevant_skills

    def _get_relevant_skills(self, use_skill_profile, use_learning_profile, user_id):
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

            learning_history_id = user["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("User profile no learning history")
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history_id}")

            relevant_skills = self._get_learning_profile(learning_history_id)

        elif use_skill_profile and not use_learning_profile:
            ## case 3: using skill profile but not learning profile
            # get the skill profile of the user
            self.ns_customizer.logger.info("*** case 3: using skill profile but not learning profile ***")

            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info:\n{user}")

            learning_history_id = user["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("User profile no learning history")
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history_id}")

            # retrieve skills relevant to query
            relevant_skills = self._get_skill_profile(learning_history_id)

        else:
            ## case 4: using both skill profile and learning profile
            # get the skill and learning profile of the user
            self.ns_customizer.logger.info("*** case 4: using both skill profile and learning profile ***")

            user = self.sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
            self.ns_customizer.logger.info(f"User Info:\n{user}")

            learning_history_id = user["learning_history_id"]
            if learning_history_id == '':
                raise ValueError("User profile no learning history")
            self.ns_customizer.logger.info(f"Learning History Info: {learning_history_id}")

            skill_profile = self._get_skill_profile(learning_history_id)
            learning_profile = self._get_learning_profile(learning_history_id)

            relevant_skills = skill_profile + learning_profile

        relevant_skills = list(set(relevant_skills))  # filter out duplicates
        self.ns_customizer.logger.info(f"Relevant Skills:\n{relevant_skills}")

        return relevant_skills

    def add_after(self, query, use_skill_profile, use_learning_profile, user_id, language_model, dataset_name,
                  index_method):

        relevant_skills = self._get_relevant_skills(use_skill_profile, use_learning_profile, user_id)

        searcher = Searcher()
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


class Searcher(object):
    language_models = {
        "bert-base-german-cased": "dbmdz/bert-base-german-cased",
        # "xlm-roberta-base": "xlm-roberta-base",
        "cross-en-de-roberta-sentence-transformer": "T-Systems-onsite/cross-en-de-roberta-sentence-transformer"
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
        # print(query)
        encodes_file_path = os.path.join(os.getenv("BASE_ENCODES_DIR"),
                                         f"dense/{language_model}/{dataset_name}/data_encoded.json")
        prebuilt_index_path = os.path.join(os.getenv("BASE_INDEXES_DIR"),
                                           f"{index_method}/{dataset_name}/dense/{language_model}/")

        # print(encodes_file_path)
        # print(prebuilt_index_path)

        if language_model not in ["bert-base-german-cased", "cross-en-de-roberta-sentence-transformer"]:
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
        # elif language_model == "xlm-roberta-base":
        #     encoder = XlmRobertaDenseEncoder()
        elif language_model == "cross-en-de-roberta-sentence-transformer":
            encoder = CrossRobertaSentenceTransformerEncoder()
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

            if i == 0:
                print(query)
                print(results[i]["contents"])
                print(len(query_enc), flush=True)
                print(len(results[i]["vector"]), flush=True)
                print(query_enc, flush=True)
                print(results[i]["vector"], flush=True)
                print(results[i]["cosine_similarity"], flush=True)

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
        return float("{:.2f}".format(n_shared / n_total))
