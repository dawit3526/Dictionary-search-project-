import sys
import random
#%% word Dictionery manuplation 


def binary_search(array,element):
    low = 0
    high = int(len(array)-1)
    while (low <= high):
        mid = int((low + high) / 2)
        if (array[mid] > element):
            high = mid - 1
        elif(array[mid] < element):
            low = mid + 1
        else:
            return array[mid]
      
    return -1
def partition(l,left,right,pivot_index):
    l[right-1],l[pivot_index] = l[pivot_index],l[right-1]
    store = left
    for i in range(left,right-1,1):
        if l[i] < l[right-1]:
            l[i],l[store] = l[store],l[i]
            store += 1
    l[store],l[right-1] = l[right-1],l[store]
    return store
    
def rec_quicksort(l,left,right):
    if left < right-1:
        pivot_index = partition(l,left,right,left+((right - left)//2))
        l = rec_quicksort(l, left, pivot_index)
        l = rec_quicksort(l, pivot_index+1, right)
    return l
              
def quicksort(l):
    return rec_quicksort(l, 0, len(l))
    
def minEditDist(target, source,f,v):
    """ Dynamic programing for computing the distance b/n two words """   
    n = len(target)
    m = len(source)
    distance = [[0 for i in range(m+1)] for j in range(n+1)] #intialize the distance mattrix 
    for i in range(1,n+1):
        distance[i][0] = distance[i-1][0] + 1

    for j in range(1,m+1):
        distance[0][j] = distance[0][j-1] + 1
    for i in range(1,n+1):
        for j in range(1,m+1):
           distance[i][j] = min(distance[i-1][j]+v,
                                distance[i][j-1]+v,
                                distance[i-1][j-1]+substCost(source[j-1],target[i-1],v))
    if(f==1):
        return distance
    else:
        return distance[n][m]
def substCost(x,y,v):
    if x == y: return 0
    else: return  v
def evaluatdic(target,dic,v):
    cost = []
    for i in range(len(dic)):
        word = dic[i]
        e = minEditDist(target,word,0,v)
        cost.append(e)
    return cost
    
def EditMatrix(dptable,m,n,str1,str2):
   
    noC = dptable[m][n]
    edits = [noC+1]

    i = m
    j = n
    while(i>0 and j>0):
        if(str1[i-1] == str2[j-1]):
            i=i-1
            j=j-1
            continue	
		
        else:
            if(dptable[i][j] == 1 + dptable[i][j-1]):
                print('Insert '+str2[j-1]+' in '+str1+' at position ',i)
                j=j-1
                
            elif(dptable[i][j] == 1 + dptable[i-1][j]):
                print('Remove '+str1[i-1]+' from '+str1+' at position ', i-1)
                i=i-1
			
            elif(dptable[i][j] == 1 + dptable[i-1][j-1]):
                print('Replace  ' + str1[i-1]+' in ' +str1+ ' with '+str2[j-1]+' from '+str2+' at position ',i-1)
                i=i-1
                j=j-1
			
    while(i>0):
        print('Remove from ' +str1[i-1]+' at pos ', i-1)
        
        i=i-1
	
    while(j>0):
        print('Insert in ' +str2[j-1]+ ' at pos ',i)
        j=j-1
	
   
    return dptable[m][n];
def main(argv):
    Sdic = []
    Words_of_same_length=[]
    q=True
    with open("american-english-ascii.txt") as f:
        dictionary = f.read().splitlines()
    Sdic = quicksort(dictionary)
    while (q==True):
        print("			---------------------------------------------")
        print("			|      small dictionary search project      |")
        print("			---------------------------------------------")
        print("please choose one of these options:")
        print(" ")
        print("1: calculate edit distance between 2 words")
        print("2: search for one word in dictionary")
        print("3: text input")
        print("4: Find same length word like your word")
        print("5: Exit")
        str1=input("your choice:")
        if(str1==5):q=False
        elif(str1==1):
            w1=raw_input("your word:")
            print(w1)
            w2=raw_input("your target:")
            print(w2)
            e=minEditDist(w1,w2,1,1)
            #print(e)
            print("edit distance= "+str(e[len(w1)][len(w2)]))
            EditMatrix(e,len(w1),len(w2),w1,w2)
        elif(str1==2):
            w1=raw_input("your word:")
            v=int(raw_input("your choise of cost Matrix:"))
            Word = binary_search(Sdic,w1)
            if(Word == -1):
                ind = evaluatdic(w1,Sdic,v).index(min(evaluatdic(w1,Sdic,v)))
                str2 = Sdic[ind]
                print('The neareast similar word is '+str2)
            else:
                print(w1+'fond in dictionary')
        elif(str1==3):
            t=raw_input("your text:")
            t1=t.split()
            print("		-----------------search result ---------------")
            for v in range(len(t1)):
                w1=t1[v]
                w=binary_search(Sdic,w1)
                if(w == -1):
                    ind = evaluatdic(w1,Sdic,1).index(min(evaluatdic(w1,Sdic,1)))
                    str2 = Sdic[ind]
                    print('The neareast similar word found in dictionery for ''"'+w1+'"' 'in your sentence is '+str2)
                else:
                    print(w1+ ' fond in dictionary')
        
        elif(str1==4):
             w1=raw_input("your word:")
             for i in range(len(Sdic)):
                if (len(w1) ==len(Sdic[i])):
                    Words_of_same_length.append(Sdic[i])
             print(Words_of_same_length)
if __name__ == "__main__":
    main(sys.argv)