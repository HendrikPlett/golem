from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Golem',  
    version='0.10',            
    packages=['golempckg', 
              'golempckg.models', 
              'golempckg.trainers', 
              'golempckg.data_loader', 
              'golempckg.utils'], 
    install_requires = requirements
)