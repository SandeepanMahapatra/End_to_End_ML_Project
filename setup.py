from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements as listed in the requirements text file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    # Adding "-e ." at the end of the req.txt file provides isolation from System-wide Installations
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    
setup(
    name = "ML PROJECT",
    version = "0.0.1",
    author = "Sandeepan",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )