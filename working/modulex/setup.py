from setuptools import setup, find_packages

setup(name='modulex',
      description='exercise module for the SciComp class',
      url='https://gitlab.com/fcaruggi',
      author='Federico Caruggi',
      author_email='f.caruggi@campus.unimib.it',
      license='MIT',
      version='0.0.3',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])