#ask the customer how many pizzas they want with eval()
number_of_pizzas = eval(input("How many pizzas do you want?"))
# Ask for the menu cost of each pizza
cost_per_pizza = eval(input("How much does each pizza cost? "))
#Calculate the total cost of the pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizza
#calculate the sales tax owed, at *% of the subtotal
tax_rate = 0.08 #store 8% as 0.08
sales_tax = subtotal + tax_rate
#add the sales tax to the subtotal for the final total
total = subtotal + sales_tax
#show the customer the total amount due, including tax
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sales tax.")
print("The total cost is $",total)

