from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Harshal pawar"
DESRCIPTION="This is a first FSDS Nov batch Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    #this functin is going to return list of requrement mention in the req.txt
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()
    
#Declaring variable for setup function

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), #used for installing the housing __init__ files
install_requires=get_requirements_list() #for get all requrement.txt file
)