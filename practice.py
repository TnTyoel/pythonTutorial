people_attending = eval(input("How many people are going to attend?"))

cost_of_people = eval(input("What is the cost of each person?"))

subtotal = cost_of_people * people_attending

building_cost = 75

total = building_cost + subtotal

print("The cost for people attending is $" ,subtotal)
print("The cost for renting a building for one day is $" , building_cost)
print("Your total is $" , total)