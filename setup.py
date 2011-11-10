# -*- coding: utf-8 -*-
from distutils.core import setup

import confumatrix

setup(name = 'confumatrix',
      version = confumatrix.__version__,
      description = 'Confusion matrix tool for binary classification.',
      long_description = open('README.rst').read(),
      author = confumatrix.__author__,
      author_email = confumatrix.__email__,
      url = 'https://github.com/moliware/confumatrix',
      packages = ['confumatrix'],
      license = 'BSD',
      scripts = ['scripts/binary_classification.py'],
      classifiers = ('Development Status :: 4 - Beta',
                     'Natural Language :: English',
                     'License :: OSI Approved :: BSD License',
                     'Programming Language :: Python :: 2.5',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
      ),
)