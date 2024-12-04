List = [1,3,5,4,7,9]
key = int(input("Enter The Number to be Searched :- "))

def Linear_Search(List , n , key):
    # Searhing List Sequentially
    for i in range(0,n):
        if  (List[i] == key):
            return i
    return -1

n = len(List)
res = Linear_Search(List,n,key)
if (res== -1):
    print("Element Not Found")
else:
    print("Element Found At Index :",res)