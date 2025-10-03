import os
from pathlib import Path



list_of_files = [
    "Dockerfile",
    "main.py",
    "requirements.txt",
    "src/MANIFEST.in",
    "src/requirements.txt",
    "src/README.md",
    "src/setup.py",
    "src/tox.ini",
    "src/prediction_model/pipeline.py",
    "src/prediction_model/train_pipeline",
    "src/prediction_model/predict.py",
    "src/prediction_model/VERSION",
    "src/__init__.py",
    "src/prediction_model/config/config.py",
    "src/prediction_model/config/__init__.py",
    "src/prediction_model/__init__.py",
    "src/prediction_model/dataset/__init__.py",
    "src/prediction_model/trained_models/__init__.py",
    "src/prediction_model/processing/data_management.py",
    "src/prediction_model/processing/preprocessor.py.py",
    "src/prediction_model/processing/__init__.py",
    "test/pytest.ini",
    "test/python_test.py",
    "__init__.py"

 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated