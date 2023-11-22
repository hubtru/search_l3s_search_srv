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
    LANGUAGE_MODELS = ['bert-base-german-cased', 'xlm-roberta-base']
    
    
    def __get_subdirs(self, dir):
        if os.path.isdir(dir):
            subdirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
            return subdirs
        else:
            raise ValueError("Directory not found!")


    def get_datasets(self):
        datasets_dir = os.getenv("BASE_DATASETS_PATH")
        subdirs = self.__get_subdirs(datasets_dir)
        return subdirs
    
    def get_encodes(self):
        encodes_dir = os.getenv("BASE_ENCODES_PATH")
        subdirs = self.__get_subdirs(encodes_dir)
        return subdirs
    
    def check_dirs(self):
        base_datasets_dir = os.getenv("BASE_DATASETS_PATH")
        base_encodes_dir = os.getenv("BASE_ENCODES_PATH")
        base_indexes_dir = os.getenv("BASE_INDEXES_PATH")
        
        response = {}
        if not os.path.isdir(base_datasets_dir):
            os.mkdir(base_datasets_dir)
            response["BASE_DATASETS_PATH"] = "created"
        else:
            response["BASE_DATASETS_PATH"] = "exists"
        
        if not os.path.isdir(base_encodes_dir):
            os.mkdir(base_encodes_dir)
            response["BASE_ENCODES_PATH"] = "created"
        else:
            response["BASE_ENCODES_PATH"] = "exists"
            
        if not os.path.isdir(base_indexes_dir):
            os.mkdir(base_indexes_dir)
            response["BASE_INDEXES_PATH"] = "created"
        else:
            response["BASE_INDEXES_PATH"] = "exists"

        return response
    
    def get_existing_dense_encodings(self):
        datasets = self.get_datasets()
        dense_encodes_dir = os.path.join(os.getenv("BASE_ENCODES_PATH"), "dense")
        existing_encodings = []
        
        for l in self.LANGUAGE_MODELS:
            encode_dir = os.path.join(dense_encodes_dir, l)
            encode_subdirs = self.__get_subdirs(encode_dir)
            existing_encodings.append({"language_model": l, "datasets": encode_subdirs})
            
        return existing_encodings
        
    def get_not_dense_encoded_dataset(self):
        
        datasets = self.get_datasets()
        dense_encodes_dir = os.path.join(os.getenv("BASE_ENCODES_PATH"), "dense")
        
        not_encoded_dataset = []
        for l in self.LANGUAGE_MODELS:
            encode_dir = os.path.join(dense_encodes_dir, l)
            encode_subdirs = self.__get_subdirs(encode_dir)
            not_encoded = []
            for d in datasets:
                if d not in encode_subdirs:
                    not_encoded.append(d)
            
            not_encoded_dataset.append({l: not_encoded})
        
        return not_encoded_dataset
    
    def get_existing_indexes(self):
        # datasets = self.get_datasets()
        base_indexes_path = os.getenv("BASE_INDEXES_PATH")
        
        existing_indexes = []
        for i in self.INDEX_METHODS:
            indexed_datasets = self.__get_subdirs(os.path.join(base_indexes_path, i))
            existing_indexes.append({"index_method": i, "datasets": indexed_datasets})
            
        return existing_indexes
                    
    def get_not_indexed_datasets(self):
        datasets = self.get_datasets()
        base_indexes_path = os.getenv("BASE_INDEXES_PATH")
        
        not_indexed_datasets = []
        for i in self.INDEX_METHODS:
            indexed_datasets = self.__get_subdirs(os.path.join(base_indexes_path, i))
            not_encoded = []
            for d in datasets:
                if d not in indexed_datasets:
                    not_encoded.append(d)
            
            not_indexed_datasets.append({i: not_encoded})
        
        return not_indexed_datasets

    def get_latest_dataset(self):
        directory_path = os.getenv("BASE_DATASETS_PATH")
        
        if os.listdir(directory_path) == []:
            latest_folder = ""
        else:
            directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
            if not directories:
                print("No directories found in the specified path.")
            else:
                # Sort the directories by their creation timestamp (most recent first)
                directories.sort(key=lambda d: os.path.getctime(os.path.join(directory_path, d)), reverse=True)

                # Get the latest created folder
                latest_folder = directories[0]
                print(f"The latest created folder is: {latest_folder}")
            return latest_folder