#!/bin/python2

import sys
import string

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()

#a = list(string.ascii_lowercase)
max = 0
for ch in word:
    if h[int(ord(ch)-97)] >= max:
        max = h[int(ord(ch)-97)]
print int((max*1)*len(word))
#print ord(list(word))