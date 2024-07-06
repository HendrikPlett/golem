from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Golem',  
    version='0.7',            
    packages=['golempckg', 'models', 'trainers', 'data_loader'], 
    install_requires = requirements
)