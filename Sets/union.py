#union(basically adding)
x = {1, 3, 5, 7, 9, 11, 13}
y = {2, 4, 6, 8, 10, 12, 14}
print(y.union(x))
#union method #2
x = {1, 3, 5, 7, 2, 4, 6}
y = {2, 4, 5, 7, 2, 0, 9}
print(x | y)
#intersection method
x = {1, 3, 5, 7, 2, 4, 6}
y = {2, 4, 5, 7, 2, 0, 9}
print(x & y)
#intersection method #2
x = {1, 3, 5, 7, 2, 4, 6}
y = {2, 4, 5, 7, 2, 0, 9}
print(y.intersection(x))

x = {1, 3, 5, 7, 2, 4, 6}
y = {2, 4, 5, 7, 2, 0, 9}
print(x.difference(y))

x = {1, 3, 5, 7, 2, 4, 6}
y = {2, 4, 5, 7, 2, 0, 9}
print(x^y)

my_set = {'land', 'sea', 'air', 'ocean', 'river'}
print('sea' not in my_set)
