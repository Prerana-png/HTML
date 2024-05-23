def binarysearch (A , low, high, searchkey):
    m=0
    while(low<=high):
        m=(low+high)//2
        if(A[m]==searchkey):
            return 1
        elif(A[m]<searchkey):
            low= m+1
        else:
            high=m-1
        

def twosum(A,arr_size,sum):
    A.sort()
    l=0
    r=arr_size-1

    i=0
    while i< arr_size -1:
        searchkey=sum-A[i]
        if(binarysearch(A,i+1,r,searchkey)==1):
            return 1
        i=i+1
    return 0

A=[1,2,3,4,5,6]
n=8
if (twosum(A,len(A),n)):
    print("yes")
else:
    print("no")


