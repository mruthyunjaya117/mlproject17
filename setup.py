from setuptools import setup, find_packages
from typing import List

HYPHEN_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements


setup(
    name='mlproject',
    author="Dhanunjaya",
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)