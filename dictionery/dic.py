my_dict = {'Name':'Mark', 'Age': 24, 'Ranking':'5th', 'Average':89.5}
print(my_dict['Name'])
print(my_dict['Ranking'])
print(my_dict)

my_dict = {'Name':'Mark', 'Age': 24, 'Ranking':'5th', 'Average':89.5}
print(my_dict.get('Name'))
print(my_dict.get('Ranking'))

#add key and value
my_dict = {'Name':'Mark', 'Age': 24, 'Ranking':'5th', 'Average':89.5}

my_dict['Status'] = 'regular'
print(my_dict)

#modiy current value of a key
my_dict = {'Name':'Mark', 'Age': 24, 'Ranking':'5th', 'Average':89.5}
my_dict['Ranking'] = '3rd'
print(my_dict)

#removing a key and value from dictionery
my_dict = {'Ocean':'Pacific ocean', 'Sea': 'Baltic Sea', 'river':'Danube', 'swamp':'The Everglades'}
my_dict.pop('river')
print(my_dict)

#popitem method(removes a random key)
my_dict = {'Ocean':'Pacific ocean', 'Sea': 'Baltic Sea', 'river':'Danube', 'swamp':'The Everglades'}
my_dict.popitem()
print(my_dict)

#clear method
my_dict = {'Ocean':'Pacific ocean', 'Sea': 'Baltic Sea', 'river':'Danube', 'swamp':'The Everglades'}
my_dict.clear()
print(my_dict)
#delete method does not work and will give error
#update method adds the second dictinery with the first

dict_1 = {'First Name': 'Chuck', 'Age': 27, 'Branch': 'Chicago'}
dict_2 = {'Last name' : 'Daivdson', 'Postition' :'Supervisor', 'Branch' :'New York'}
dict_1.update(dict_2)
print(dict_1)
print(dict_2)
#item method(to turn dictionery into a list)

x = {1:'abc', 2:'def', 3:'ghi', 4:'jkl'}
print(x.items())
#value method(prints the value of the keys)
print(x.values())
#key method(prints the keys of the values )
dict_one = {'animal':'tiger', 'age':4, 'Location':'Cage 5'}
print(dict_one.keys())
#set default method
my_dict = {'a':'car', 'b':'van', 'c':'yacht', 'd':'bus'}
print(my_dict.setdefault('c', None))
#copy method(prints a editable copy that does not alter the original)
my_dict1 = {'apple':10, 'oranges':5, 'grapefruit':7, 'strawberry':12}
my_dict2 = my_dict1.copy()
print(my_dict2)
my_dict2['oranges'] = 50
my_dict2['apple'] = 5
print(my_dict2)
print(my_dict1)
#fromkeys method(takes information from keys to make a new dictionery)
keys = ['monitor', 'CPU', 'mouse', 'keyboard', 'speaker']
new_dict = dict.fromkeys(keys, 10)
print(new_dict)
#dictionary member test(true/false)
even = {2:'GRQ', 4:'XYZ', 6:'DEF', 8:'GHI', 10:'JKL'}
print(2 in even)
print(12 in even)
print(8 not in even)
print(14 not in even)
#sorted method
my_dict = {'color':'silver', 'year model':2012, 'warehouse':'used'}
print(sorted(my_dict))
#tuple into dictionary
pairs = [('cat', 'kitten'), ('dog', 'puppy'), ('lamb', 'ewe'), ('lion', 'cub')]
print(dict(pairs))