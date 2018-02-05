#!/bin/python3

import sys

def getWays(S,m,n):
    table = [0 for k in range(n+1)]
 

    table[0] = 1

    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table[n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
S = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(S,m,n)
print (ways)
