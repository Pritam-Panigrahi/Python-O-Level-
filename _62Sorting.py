dict ={1:'Pritam',3:'Raj',4:'Rahul',2:'Harmeet'}
print(dict)
x = list(dict.keys())
print(x)
x.sort()
print(x)
for i in x:
    print(i,':-',dict[i])