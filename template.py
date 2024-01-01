import os
from pathlib import Path

package_name = "Student_performance_prediction"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/Components/__init__.py",
    f"src/{package_name}/Components/data_ingestion.py",
    f"src/{package_name}/Components/data_transformation.py",
    f"src/{package_name}/Components/model_trainer.py",
    f"src/{package_name}/Pipelines/__init__.py",
    f"src/{package_name}/Pipelines/training_pipeline.py",
    f"src/{package_name}/Pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/utils.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py"
]


for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not(os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    
    else:
        print(f"file already exists")