# -*- coding: utf-8 -*-
import sys
import random
import commands
import re

def transformaPDF(archivo):
	print "Transformando de pdf a txt... " + archivo

	comando = commands.getoutput("pdftotext "+archivo)
	txt= archivo.replace(".pdf", ".txt");

	string = open(txt).read().lower()
	string = string.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
	string = re.sub('[^a-zA-Z]', '', string)
	open(txt, 'w').write(string)
	return string,txt
