# Uses python3
import math
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def split_expr(dataset):
    global operators
    global operands

    operators = list()
    operands = list()
    
    for i in range(len(dataset)):
        if i%2==0:
            operands.append(dataset[i])
        else:
            operators.append(dataset[i])
    print (operands)
    print (operators)
    
    #minmax(0,len(dataset),dataset)

def minmax(i,j,dataset):
    print ("++++")
    for k in range(i,j,2):
        #print (type(k))
        print (dataset[i:k] , dataset[k], dataset [k+1:j])
        print ("++++")
        



    #write your code here
    return 0

def parantheses(str):
    global operators
    global operands
    n = math.ceil(len(str)/2)
    m = [[0 for i in range(n)] for i in range(n)]
    print (m)
    for i in range(len(operands)):
        m[i][i] = operands[i]
    print (m)
    for s in range(0,len(operands)-1):
        for i in range(0,n-s):
            j = i+s
            print ("operands ",s," inner loop ",i," tthe j is ",j)
            #minmax(i,j,s)





if __name__ == "__main__":
    #str = input()
    str = "5-8+7*4-8+9"
    print (str)
    split_expr(str)
    parantheses(str)
    #print(get_maximum_value(str))
