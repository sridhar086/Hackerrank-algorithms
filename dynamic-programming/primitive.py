#python3

def change(n):
    total = []
    a = []
    b = []
    chk = {}   
    for i in range(0,n):
        if i==0:
            a.append(0)
            total.append(0)
            continue
        else:
            coin1 = None
            coin2 = None
            coin3 = None
            coin1 = total[i-1]+1


            if i%2 == 0:
                coin2 = total[i//2]+1
         
            if i%3 == 0:
                coin3 = total[i//3]+1

            if coin1 != None and coin2 !=None and coin3 !=None:
                val = min(coin1,coin2,coin3)
                total.append(val)
                if coin3 <= coin2 and coin3 <= coin1:
                    chk[i]=i//3
                elif coin2 <= coin3 and coin2 <= coin1:
                    chk[i] = i//2
                else:
                    chk[i] = i-1


            elif coin1 != None and coin2 != None:
                val = min(coin1, coin2)
                total.append(val)
                if coin2 <= coin1:
                    chk[i]= i//2
                else:
                    chk[i] = i-1

            elif coin2 != None and coin3 != None:
                val = min(coin2,coin3)
                chk[i] = val
                total.append(val)
                if coin3 <= coin2:
                    chk[i] = i//3
                else:
                    chk[i] = i//2

            elif coin1 != None and coin3 != None:
                val = min(coin1,coin3)
                chk[i]=val
                total.append(val)
                if coin3 <= coin1:
                    chk[i] = i//3
                else:
                    chk[i] = i-1

            else:
                total.append(coin1)
                chk[i] = i-1
                
    print (total[-1]-1)
    l = list()
    _next = chk[n-1]
    l.append(n-1)

    while(True):
        l.append(_next)
        _next = chk[_next]
        if _next == 1:
            l.append(_next)
            break
    l = list(reversed(l))
    st = ' '.join(str(item)for item in l)
    print (st)

if __name__=="__main__":
    inp = input()
    change(int(inp)+1)
