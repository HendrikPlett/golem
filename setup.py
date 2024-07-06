from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Golem',  
    version='0.3',            
    packages=['golem'], 
    install_requires = requirements
)