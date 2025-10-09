import os
import pandas as pd
import joblib
from prediction_model.config import config

def load_dataset(file_name):
    data_path = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(data_path)
    print("Dataset Loaded.....")
    return _data

def save_pipeline(pipeline_to_save):
    save_file_name = 'classification_v1.pkl'
    save_path = os.path.join(config.SAVED_MODEL_PATH, save_file_name)
    print(save_path)
    joblib.dump(pipeline_to_save, save_path)
    print("Save pipeline", save_file_name)

def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVED_MODEL_PATH, pipeline_to_load)
    print(save_path)
    trained_model = joblib.load(save_path)
    print("Pipeline Loaded", pipeline_to_load)
    return trained_model