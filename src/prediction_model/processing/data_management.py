import os
import pandas as pd
import joblib

from prediction_model import config

def load_dataset(file_name):
    data_path = os.path.join(config.DATAPATH, filename)
    _data = pd.read_csv(data_path)
    return _data

def save_pipeline(pipeline_to_save):
    save_file_name = 'classification.pkl'
    save_path = os.path.join(config.SAVED_MODEL_PATH, save_file_name)
    joblib.dump(pipeline_to_save, save_path)
    print("Save pipeline", save_file_name)

def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVED_MODEL_PATH, pipeline_to_load)
    trained_model = joblib.load(save_path)
    print("Pipeline Loaded", pipeline_to_load)
    return trained_model