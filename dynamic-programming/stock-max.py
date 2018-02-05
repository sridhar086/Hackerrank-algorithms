#python3



def profit(stockvalues):
    m = 0
    prof = 0
    for i in reversed(range(len(stockvalues))):
        ai=int(stockvalues[i]) # shorthand name
        if m<=ai:
            #dobuy[i]=0
            m=ai
        prof+=m-ai
    print prof
        
        
        
N = raw_input()
for i in range(int(N)):
    c = raw_input()
    d = list(raw_input().split())
    profit(d)