# -*- coding: utf-8 -*-
import sys
import random
import commands
import re


print "Transformando de pdf a txt... " + sys.argv[1]
#pasamos el pdf por argumento
comando = commands.getoutput("pdftotext "+sys.argv[1])
txt= sys.argv[1].replace(".pdf", ".txt");

string = open(txt).read()
#se reemplazan las letras con acento a letras sin acento
str2 = string.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("Á","a").replace("É","e").replace("Í","i").replace("Ó","o").replace("Ú","u")
new_str = re.sub('[^a-zA-Z]', '', str2)
#todo a minusculas
str = new_str.lower()
open(txt, 'w').write(str)
#str = 'todotextounidosinnada....'
