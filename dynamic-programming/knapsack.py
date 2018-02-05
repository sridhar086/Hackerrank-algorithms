# Uses python3
import sys
import copy

#This code calculates the knapsack with repetition#

def optimal_weight(W, w):
    total = []
    total.append(0)
    for i in range(1,W+1):
        total.append(0)
        for j in w: 
            if j <= i:
                val = total[i-j] + j
                if val > total[i]:
                    total[i] = val
    
    return total[W]

if __name__ == '__main__':
    nos = int(input())
    for i in range(nos):
        no,W=list(map(int, input().split()))
        w = list(map(int,input().split()))
        print(int(optimal_weight(W, w)))
