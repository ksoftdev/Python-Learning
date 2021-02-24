#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    #A = "a ab ac"
    #B = "b b2"
    A = "a ab ac"
    B = "b bb"

    salida = []
    
    for i in A.split():
        for j in B.split():
            if not ( str(i+j) in salida):
                salida.append(i+j)
                print(i + j + " " , end='')
