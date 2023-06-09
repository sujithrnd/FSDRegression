from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requrements=file_obj.readlines()
        requirements=[req.reiplace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            return requirements

setup(
    name='RgressorProject',
    version='0.0.1',
    author='Sujithks',
    author_email='sujithks81@gmail.com',
    install_requires=['pandas','numpy'],
    packages=find_packages()


)