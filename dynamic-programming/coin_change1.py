#python3

def change(n):
    a = []
    for i in range(0,n):
        if i==0:
            a.append(0) 
            continue
        else:
            coin1 = None
            coin2 = None
            coin3 = None
            coin1 = a[i-1]+1

            #print ("add 1 for "+str(i)+" "+str(coin1))
            if i%5 == 0:
                coin2 = a[i-5]+1
                #print ("multipply 2 for "+str(i)+" "+str(coin2))            
            if i%6 == 0:
                coin3 = a[i-6]+1
                #print ("multply 3 for "+str(i)+" "+str(coin3))
            if coin1 != None and coin2 !=None and coin3 !=None:
                a.append(min(coin1,coin2,coin3))
            elif coin1 != None and coin2 != None:
                a.append(min(coin1,coin2))
            elif coin2 != None and coin3 != None:
                a.append(min(coin2,coin3))
            elif coin1 != None and coin3 != None:
                a.append(min(coin1,coin3))
            else:
                a.append(coin1)
            print ("***********")
    print (a)


if __name__=="__main__":
    change(25)
