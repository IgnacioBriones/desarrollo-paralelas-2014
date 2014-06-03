# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

from tools.serial import get_pattern
from tools.pdfstring import pdf2string

#
path =  "./../files/biblia.pdf"
sheets = pdf2string(path, borrarCaracteresEspeciales=True, separadosPorHoja=True)

for sheet in sheets:
    pos = get_pattern(text=sheet, rank=2, word="casa")
    print pos
