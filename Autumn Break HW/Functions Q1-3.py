
#Ques 1
def LShift(Arr,n):
    n%=len(Arr)
    Arr = Arr[n:]+Arr[:n]
    print("Arr = ",Arr)

# Ques 2
def INDEX_LIST(L):
    indexList = []
    for i in L:
        if i != 0:
            indexList.append(L.index(i))
    return indexList

#Ques 3
def Sum3(L):
    sum = 0
    for i in L:
        if i %10 == 3:
            sum+=i
    print("Sum of integers ending with digit 3 = ",sum)
