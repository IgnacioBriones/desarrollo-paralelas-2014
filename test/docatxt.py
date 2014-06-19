# -*- coding: utf-8 -*-
import sys
import random
import commands
import re
#caso doc
print "Transformando de doc a txt... " + sys.argv[1]
#Pasamos el .doc como argumento.
txt= sys.argv[1].replace(".doc", ".txt");
comando = commands.getoutput("catdoc "+sys.argv[1]+" > "+txt)
string = open(txt).read()
#reemplazo de las letras en la cadena string y guardado en str2
str2 = string.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("Á","a").replace("É","e").replace("Í","i").replace("Ó","o").replace("Ú","u")
new_str = re.sub('[^a-zA-Z]', '', str2)
#dejamos todo en minusculas
str = new_str.lower()
open(txt, 'w').write(str)
#al final str = 'muchasletrasjuntassinespacio.....'
