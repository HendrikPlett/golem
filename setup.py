from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Golem',  
    version='0.1',            
    packages=['src'], 
    install_requires = requirements
)