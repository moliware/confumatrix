# -*- coding: utf-8 -*-
"""
    confumatrix
    ~~~~~~~~~~~

    Binary classification.

    http://en.wikipedia.org/wiki/Confusion_matrix

    :copyright: (c) 2011 by  Miguel Olivares and F.Javier Alba.
"""


class ConfuMatrix():
    """ Calculates confusion matrix.
    Further information:
        http://en.wikipedia.org/wiki/Binary_classification
        http://en.wikipedia.org/wiki/Sensitivity_and_specificity
    """
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def accuracy(self):
        return float(self.a + self.d) / float(self.a + self.b + self.c + self.d)

    def precision(self):
        return float(self.a) / max(1.0, float(self.a + self.b))

    def recall(self):
        return float(self.a) / max(1.0, float(self.a + self.c))

    def specificity(self):
        return float(self.d) / max(1.0, float(self.b + self.d))

    def sensitivity(self):
        return self.recall()

    def f1(self):
        precision = self.precision()
        recall = self.recall()
        return 2.0 * precision * recall / max(1.0, (precision + recall))

    def __str__(self):
        s = ''
        s += '%s\n' % ('=' * 25)
        s += 'Confusion Matrix:\n\n'
        s += '\t%s\t%s\n' %(str(self.a), str(self.b))
        s += '\t%s\t%s\n\n' %(str(self.c), str(self.d))
        s += 'Accuracy: %s\n' % self.accuracy()
        s += 'Recall: %s\n' % self.recall()
        s += 'Precision: %s\n' % self.precision()
        s += 'Specificity: %s\n' % self.specificity()
        s += 'F-measure: %s\n' % self.f1()
        s += '%s\n' % ('=' * 25)
        return s