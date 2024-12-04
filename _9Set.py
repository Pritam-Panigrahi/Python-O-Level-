a = {1,2,3,4,4,5,5,6}
b = set([1,2,3,4,5,5,6,6,6,])
print(a)
print(b)
a.add(10) #adds Single Item
print(a)

b.update([20,30,40]) #Updates Multiple item
print(b)

a.remove(4) #Removes Given Item
print(a)

a.pop()   #Removes First Indexed item
print(a)

b.discard(30) # Removes item Even it Present inb Set Or Not .... Not Gives Ann Erreor.
print(b)

b.difference_update([1,2,3])
print(b)