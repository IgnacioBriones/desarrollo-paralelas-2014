'''
Created on 13-05-2014

@author: leonardo jofre
'''

from unpdfer import Unpdfer


def loadPdfPath(filename):
    # set an input filename
    # conver to text
    worker = Unpdfer()
    (created, pdftext, pdfhash, success) = worker.unpdf(filename, SCRUB=False, verbose=False)
    return created, pdftext, pdfhash, success
