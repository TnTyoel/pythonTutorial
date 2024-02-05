import turtle #sets up tutle graphics
t = turtle.Pen()
#add background color
turtle.bgcolor("black")
#set up a list of any 8 vaild python color names
colors = ["red", "green", "yellow", "blue", "purple", "white", "grey"]
#ask the user for the number of sides, betweem 1 and 8 with a default of 4
sides = int(turtle.numinput("number of sides", "how many sides do you want(1-8)?",4, 1, 8))
#Draw a colorful spiral with the user-specified number of sides
for x in range(360):
    t.pencolor(colors[x % sides]) # Only use the right number of colors
    t.forward(x*3 / sides + 1)# change the size to match number of sides
    t.left(360 / sides + 1) # Turn 360 degrees / number of sides, plus 1
    t.width(x * sides / 200) # Make the pen larger as it goes outward