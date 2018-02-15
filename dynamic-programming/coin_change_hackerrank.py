#python3

# Dynamic Programming Python implementation of Coin Change problem
def count(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
    print (table)
 
    return table[n][m-1]

# Dynamic Programming Python implementation of Coin 
# Change problem
def count2(S, m, n):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
    print( table)
 
    return table[n]
	
	
	
def change(n,coins):
    a = []
    ways = 1
    for i in range(0,n+1):
        if i==0:
            a.append(0) 
            continue
        else:
            coin = [-1 for i in range(len(coins))]
            #coin1 = None
            #coin2 = None
            #coin3 = None
            for j,num in zip(coins,range(0,len(coins))):
                if i%j == 0:
                    coin[num] = a[i-j]+1
            min_coin = sorted(list(set(coin)))
            
            if min_coin[0] != -1:
                a.append(min_coin[0])
            elif len(min_coin) > 1:
                a.append(min_coin[1])
            else:
                a.append(0)
                continue

            minnie = list(min_coin)
            minnie.pop(0)
            ways = ways * min(minnie)

            '''
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
            '''
    print (a[-1])
    print (ways)


if __name__=="__main__":
    arr = [1,2,3]
    m = len(arr)
    n = 5
    print (count(arr,m,n))
    print (count2(arr,m,n))
    '''
    str1 = input()
    str2 = input()
    n,no = list(map(int,str1.split()))
    coins = list(map(int,str2.split()))
    change(n,coins)
    '''
