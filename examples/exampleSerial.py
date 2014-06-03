# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

import random
from tools.serial import get_pattern
# a modo de ejemplo generamos un array de numeros aleatorios
alfabeto = "abcdefghijklmn?opqrstuvwxyz"

# Generamos un vector aleatorio con esta informacion posible
N = 1000000
# transformar el pdf a texto
text = [random.choice(alfabeto) for _ in range(N)]
# @todo: cargar la path
#

pos = get_pattern(text=text, rank=2, word="casa")
print pos
