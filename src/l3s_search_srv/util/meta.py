import os
from flask import url_for
# from l3s_search_srv.api.encoder.logic import DenseEncoer

print(os.path.isdir('/home/peng-luh/__github/search_l3s_search_srv/src/search_l3s_search/util'))

def get_subdirs(dir):
        if os.path.isdir(dir):
            subdirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
            return subdirs
        else:
            raise ValueError("Directory not found!")

class SearchSrvMeta(object):
    INDEX_METHODS = ['flat-ip', 'flat-l2']
    ENCODE_METHODS = ['bm25', 'dense', 'sparse']
    LANGUAGE_MODELS = ['bert-base-german-cased', 'xlm-roberta-base', 'geberta-xlarge', 'bert-base-german-uncased', 'bert-base-multilingual-uncased', 'bert-base-multilingual-cased']
    
    
    def __get_subdirs(self, dir):
        if os.path.isdir(dir):
            subdirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
            return subdirs
        else:
            raise ValueError("Directory not found!")

    def get_datasets(self):
        datasets_dir = os.getenv("BASE_DATASETS_DIR")
        if not os.path.isdir(datasets_dir):
            os.mkdir(datasets_dir)
            raise FileNotFoundError(f"Path not found: {datasets_dir}")
        subdirs = self.__get_subdirs(datasets_dir)
        return subdirs
    
    def get_encode_methods(self):
        encodes_dir = os.getenv("BASE_ENCODES_DIR")
        if not os.path.isdir(encodes_dir):
            os.mkdir(encodes_dir)
            raise FileNotFoundError(f"Path not found: {encodes_dir}")
        subdirs = self.__get_subdirs(encodes_dir)
        return subdirs
    
    def get_index_methods(self):
        indexes_dir = os.getenv("BASE_INDEXED_DIR")
        if not os.path.isdir(indexes_dir):
            os.mkdir(indexes_dir)
            raise FileNotFoundError(f"Path not found: {indexes_dir}")
        subdirs = self.__get_subdirs(indexes_dir)
        return subdirs
    
    def check_dirs(self):
        base_datasets_dir = os.getenv("BASE_DATASETS_DIR")
        base_encodes_dir = os.getenv("BASE_ENCODES_DIR")
        base_indexes_dir = os.getenv("BASE_INDEXES_DIR")
        
        response = {}
        if not os.path.isdir(base_datasets_dir):
            os.mkdir(base_datasets_dir)
            response["BASE_DATASETS_DIR"] = "created"
        else:
            response["BASE_DATASETS_DIR"] = "exists"
        
        if not os.path.isdir(base_encodes_dir):
            os.mkdir(base_encodes_dir)
            response["BASE_ENCODES_DIR"] = "created"
        else:
            response["BASE_ENCODES_DIR"] = "exists"
            
        if not os.path.isdir(base_indexes_dir):
            os.mkdir(base_indexes_dir)
            response["BASE_INDEXES_DIR"] = "created"
        else:
            response["BASE_INDEXES_DIR"] = "exists"

        return response
    
    def get_existing_dense_encodings(self):
        datasets = self.get_datasets()
        dense_encodes_dir = os.path.join(os.getenv("BASE_ENCODES_DIR"), "dense")
        if not os.path.isdir(dense_encodes_dir):
            raise ValueError(f'Directory not found: {dense_encodes_dir}')
        
        existing_encodings = []
        
        for l in self.LANGUAGE_MODELS:
            encode_dir = os.path.join(dense_encodes_dir, l)
            encode_subdirs = self.__get_subdirs(encode_dir)
            existing_encodings.append({"language_model": l, "datasets": encode_subdirs})
            
        return existing_encodings
    
    def check_if_dataset_dense_encoded(self, dataset_name):
        existing_dense_encodings = self.get_existing_dense_encodings()
        flag = 1
        for e in existing_dense_encodings:
            if not dataset_name in e["datasets"]:
                flag = flag*0
                
        return bool(flag)
        
    def get_not_dense_encoded_datasets(self):
        datasets = self.get_datasets()
        dense_encodes_dir = os.path.join(os.getenv("BASE_ENCODES_DIR"), "dense")
        if not os.path.isdir(dense_encodes_dir):
            os.mkdir(dense_encodes_dir)
        
        not_encoded_datasets = []
        for l in self.LANGUAGE_MODELS:
            encode_dir = os.path.join(dense_encodes_dir, l)
            if not os.path.isdir(encode_dir):
                os.mkdir(encode_dir)
            
            encode_subdirs = self.__get_subdirs(encode_dir)
            not_encoded = []
            for d in datasets:
                if d not in encode_subdirs:
                    not_encoded.append(d)
            
            not_encoded_datasets.append({l: not_encoded})
        
        return not_encoded_datasets
    
    def get_existing_indexes(self):
        # datasets = self.get_datasets()
        BASE_INDEXES_DIR = os.getenv("BASE_INDEXES_DIR")
        if not os.path.isdir(BASE_INDEXES_DIR):
            raise ValueError(f"Directory not found: {BASE_INDEXES_DIR}")
        
        existing_indexes = []
        for i in self.INDEX_METHODS:
            indexed_datasets = self.__get_subdirs(os.path.join(BASE_INDEXES_DIR, i))
            existing_indexes.append({"index_method": i, "datasets": indexed_datasets})
            
        return existing_indexes
    
    def check_if_dataset_indexed(self, dataset_name):
        flag = 1
        existing_indexed = self.get_existing_indexes()
        for i in existing_indexed:
            if not dataset_name in i["datasets"]:
                flag = flag*0
        
        return bool(flag)
                    
    def get_not_indexed_datasets(self):
        datasets = self.get_datasets()
        BASE_INDEXES_DIR = os.getenv("BASE_INDEXES_DIR")
        
        not_indexed_datasets = []
        for i in self.INDEX_METHODS:
            indexed_datasets = self.__get_subdirs(os.path.join(BASE_INDEXES_DIR, i))
            not_encoded = []
            for d in datasets:
                if d not in indexed_datasets:
                    not_encoded.append(d)
            
            not_indexed_datasets.append({i: not_encoded})
        
        return not_indexed_datasets

    def get_latest_dataset(self):
        directory_path = os.getenv("BASE_DATASETS_DIR")
        
        if os.listdir(directory_path) == []:
            latest_folder = ""
        else:
            directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
            if not directories:
                print("No directories found in the specified path.")
            else:
                # Sort the directories by their creation timestamp (most recent first)
                directories.sort(key=lambda d: os.path.getctime(os.path.join(directory_path, d)), reverse=False)

                # Get the latest created folder
                latest_folder = directories[0]
                print(f"The latest created folder is: {latest_folder}")
            return latest_folder
        
    def check_new_dataset(self, dataset_name):
        dataset_file = os.path.join(os.getenv('BASE_DATASETS_DIR'), f"{dataset_name}/data.json")
        is_dataset_dir = os.path.isfile(dataset_file)
        is_dense_encoded = self.check_if_dataset_dense_encoded(dataset_name)
        is_indexed = self.check_if_dataset_indexed(dataset_name)
        results = {"is_dataset_dir": is_dataset_dir,
                   "is_dense_encoded": is_dense_encoded,
                   "is_indexed": is_indexed}
        return results