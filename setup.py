from setuptools import find_packages, setup

var = "-e ."

def get_requirements(filepath):

    requirements = []
    
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

    if var in requirements:
        requirements.remove(var)

    return requirements


setup(
    name = "Student Performance Prediction",
    version = "0.0.1",
    author="Nishchal Jinturkar",
    install_requires = get_requirements("requirements.txt"),
    packages=find_packages()
)