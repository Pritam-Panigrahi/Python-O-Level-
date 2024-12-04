d = {1:'Computer',2:'CPU',3:'Mouse'}
print(d) #{1: 'Computer', 2: 'CPU', 3: 'Mouse'}
d.setdefault(4,"Software")
print(d) #{1: 'Computer', 2: 'CPU', 3: 'Mouse', 4: 'Software'}
print(d.setdefault(1))  # Computer