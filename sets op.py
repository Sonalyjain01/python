"""
# symmetric difference update
A = {'Python', 'Java', 'Go'}
B = {'Python', 'JavaScript', 'C' }

print('Original Set A:', A)
A.symmetric_difference_update(B)

print('Updated Set A:', A)
"""
"""
#difference update
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

print('A before (A - B) =', A)

A.difference_update(B)

print('A after (A - B) = ', A)

#copy function
names = {"John", "Charlie", "Marie"}
new_names = names.copy()
print('Original Names: ', names)
print('Copied Names: ', new_names)

# copy set using = operator
names = {"John", "Charlie", "Marie"}
new_names = names
print('Original Names: ', names)
print('Copied Names: ', new_names)

# disjoint function
A = {'a', 'e', 'i', 'o', 'u'}
B = ['d', 'e', 'f']
C = {1 : 'a', 2 : 'b'}
D = {'a' : 1, 'b' : 2}
print('A and B are disjoint:', A.isdisjoint(B))
print('A and C are disjoint:', A.isdisjoint(C))
print('A and D are disjoint:', A.isdisjoint(D))
"""
#subset function
A = {'a', 'c', 'e'}
B = {'a', 'b', 'c', 'd', 'e'}

print('A is subset of B:', A.issubset(B))
print('B is subset of A:', B.issubset(A))
