#python3
import numpy as np
  
def edit_distance(str1,str2):
    #  This code calculates Levenshtein distance between two strings #
    array = np.empty((len(str1)+1,len(str2)+1))
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0:
                array[i,j]=max(i,j)
            else:
                if str1[i-1]==str2[j-1]:
                    array[i,j]=min(array[i-1,j]+1,array[i,j-1]+1,array[i-1,j-1])
                else:
                    array[i,j]=min(array[i-1,j]+1,array[i,j-1]+1,array[i-1,j-1]+1)
    print(int(array[i,j]))

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    edit_distance(str1,str2)

  
