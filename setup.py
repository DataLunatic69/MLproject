from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirement(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Aman',
    author_email='amansingh2002ap@gmail.com',
    packages=find_packages(),  # Corrected this
    install_requires=get_requirement('requirements.txt')
)
