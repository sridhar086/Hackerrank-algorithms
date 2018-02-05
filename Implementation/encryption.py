#!/bin/python2

import sys
import math

s = raw_input().strip()
val = math.sqrt(len(s))
row = math.floor(val)
col = math.ceil(val)

j=0
if (row*col) < len(s):
    row = math.ceil(val)
    col = math.ceil(val)
m_list = list()
for i in range(int(row)):
    m_list.append(list(s[j:j+int(col)]))
    j = j+int(col)
for i in range(int(col)):
    for j in range(int(row)):
        if(i<len(m_list[j])):
            sys.stdout.write(str(m_list[j][i]))
    sys.stdout.write(" ")


