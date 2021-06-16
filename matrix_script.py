#!/bin/python3

import math
import os
import random
import re
import sys


sen = ""

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

col = 0
while col < m:
    for i in range(n):
        sen = sen + matrix[i][col]
    col = col + 1

new_sen = re.sub(r"\b[^a-zA-Z0-9]+\b"," ",sen)

print(new_sen)
    
