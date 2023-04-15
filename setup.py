from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_packages(filepath: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='student_management',
    version='0.0.1',
    author='Saptarshi',
    author_email='bandopadhyaysaptarshi@gmail.com',
    packages=find_packages(),
    install_requires=get_packages('requirements.txt')

)
