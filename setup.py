from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

# (file_path: str): The function takes a single parameter named file_path. The : str part indicates that this parameter should be a string, specifically the path to a file.
# -> List[str]: This part specifies the expected return type of the function, which in this case is a list of strings (List[str]). 
# It suggests the function will return a list of requirements, each as a string.
# -e . in requirements.txt will automaticall trigger setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will Return the list of Requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rishu",
    author_email="rishabhkaparwan8@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt")
)