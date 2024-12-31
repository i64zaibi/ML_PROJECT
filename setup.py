from setuptools import setup, find_packages  # Corrected import statement
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Remove empty lines and newlines
    return requirements

setup(
    name='ml_project',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
