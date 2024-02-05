#set is identified by {} brackets
#Set with integers
my_set = {1, 2, 3, 4, 5, 6,}
print(my_set)
#set with strings
my_string = {'a', 'e', 'i', 'o', 'u'}
print(my_string)
#set with string, integer, float
my_mixedSet = {5.0, "Python", (5, 4, 2), 6}
print(my_mixedSet)
#lists into sets
list = (set([5, 4, 3, 1]))
print(list)
#Sets ignores duplicates
my_set = {'apple', 'peach', 'grape', 'apple', 'strawberry', 'grape'}
print(my_set)

my_set = {1, 3, 5, 9, 1, 4, 3}
print(my_set)
#empty {} brackets don't work for sets. () brackets work
my_set = set()
print(my_set)
#adding data to a set
my_set = {2, 4, 6, 8, 10}
my_set.add(12)
print(my_set)
#adding multiple data to a set
my_set = {2, 4, 6}
my_set.update([8, 10, 12, 14])
print(my_set)
#adding string to a set
my_set = {2, 4, 6, 8}
my_set.update('a', 'b')
print(my_set)
#Discarding values in a set
my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.discard('c')
print(my_set)
#removing values from a set
my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.remove('f')
print(my_set)
#discard will run the set unchanged when it does not find a value that is wanted
my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.discard('x')
my_set(print)
#remove will show an error when it does not find a value that it is not there
my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.remove('x')
print(my_set)

my_set ={'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.pop()
print(my_set)

my_set ={'a', 'b', 'c', 'd', 'e', 'f', 'g'}
my_set.clear()
print(my_set)