#inserting data
numbers = [1, 2, 4, 6, 8, 10]
numbers.insert(2,3)
print(numbers)
#use comma instead of colon for inserting

numbers[4:3] = (5, 7, 9)
print(numbers)

#removing or delting from a list
#When removing index is not needed
numbers = [1, 2, 3, 4, 5, 6.5, 6, 7.5, 9]
numbers.remove(6.5)
print(numbers)

#Popping method
#When popping it removes from specific index

my_list = ["apple", "orange", "bear", "peach"]
print(my_list.pop(2))
print(my_list)
print(my_list.pop())
print(my_list.pop())
print(my_list)

#clear method
#use when wanting to remove everything in a list
my_list.clear()
print(my_list)