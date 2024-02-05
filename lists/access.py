# accessing data in lists
school_list = ["biology", "English", "Chemistry", "Sociology", "Algera"]
print(school_list[0])
print(school_list[0][5])
print(school_list[3])

#accessing data in nested lists
nested_list = ["Code", 4, [1, 3, 5, 7, 9]]
print(nested_list[0])
print(nested_list[0][1])
print(nested_list[2][1])

#negative accessing
quick_list = ["s", "h", "o", "r", "t", "c", "u", "t"]
print(quick_list[-1])
print(quick_list[-3])
print(quick_list[-7])

#slicing lists

hw_list = ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
print(hw_list[0:5])
print(hw_list[5:])
print(hw_list[3:6])
print(hw_list[:-4])
print(hw_list[:])