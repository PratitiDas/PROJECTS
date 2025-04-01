#import different libraries
import os
from pathlib import Path
import logging

#Create logging screen
format_string = 'level=%(levelname)s datetime=%(asctime)s %(message)s'
logging.basicConfig(encoding='utf-8', level=logging.DEBUG,
                    format=format_string)


#Project name
project_name = "textSummarization"

#list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb"
    ]

#Creating the files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Check wheather the file directory is empty or not and if the directory is not available, then make the directory
    if filedir !="":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"Creating director:{filedir} for the file {filename}")


    # Check wheather the file is available or not. If not available, then make the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")


