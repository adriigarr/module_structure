# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:54:58 2022
A brief comment just to modify the file
@author: AdrianaGarcia
"""

from setuptools import setup, find_packages
from class_exercise import __name__



NAME = __name__

setup(
    name                    = NAME,
    description             = 'Brief description of your package',
    author_email            = 'adriigarr@gmail.com',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )