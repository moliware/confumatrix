confumatrix
===========

Confusion matrix tool.

Further information:

    * http://en.wikipedia.org/wiki/Binary_classification
    * http://en.wikipedia.org/wiki/Sensitivity_and_specificity

Instalation
-----------

From source code: ::

  python setup.py install

From pypi: ::

  pip intall confumatrix


Usage
-----
::

    >>> from confumatrix import ConfuMatrix
    >>> cm = ConfuMatrix(a=10, b=1, c=10, d=3)
    >>> cm.accuracy()
    0.5416666666666666
    >>> cm.precision()
    0.9090909090909091
    >>> cm.recall()
    0.5
    >>> cm.specificity()
    0.75
    >>> cm.sensitivity()
    0.5
    >>> cm.f1()
    0.6451612903225806
    >>> print cm
    =========================
    Confusion Matrix:

        10  1
        10  3

    Accuracy: 0.541666666667
    Recall: 0.5
    Precision: 0.909090909091
    Specificity: 0.75
    F-measure: 0.645161290323
    =========================


binary_classification.py
------------------------

Load a yaml file with results of a binary classfication and prints Confusion matrix for that results.

Input file format: ::

    # Languages that can be detected
    types: [en, es, pt, it, de]
    umbral: 0.5
    sample: 
      - result:
          en: 0.1
          es: 0.2
          pt: 0.3
          it: 0.6666  #hit! ( 0.6666 > 0.5 )
          de: 0.3
        expected: de
      - result:
          en: 0.2
          es: 0.99 # hit
          pt: 0.98 # hit
          it: 0.4
          de: 0.3
        expected: es