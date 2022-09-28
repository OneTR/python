import turtle

wn = turtle.Screen() # Opens the console screen
wn.bgcolor("white") # Bg color of the screen

alper = turtle.Turtle() # Turtle named alper
alper.color("black") # Turtle's color
alper.shape("turtle") # Turtle's shape
#alper.up() # To remove the line between turtles
colors = ["Black", "Purple", "Indigo", "Blue", "Yellow", "Orange", "Magenta", "Cyan", "Chartreuse", "Gold", "Pink", "Olive", "Brown", "Coral", "Maroon", "Crimson", "Black"] # List of colors.

alper_paragraph = """Hi, I'm Alper. I'm a programmer turtle and I developed a nice app named calmix. Today I'm going to move and excercise for 500 steps. 
That's my task for today. I am from Denizli, Turkey. Denizli is famous for it's girl, dust, cock. My old favorite video game is Counter-Strike 1.6. 
I played Haxball for a long time too. I love watching Leyla ile Mecnun. I also have a passion for building cities and shelters in survival strategy games, like frostpunk.
I used to have a Windows PC, now I am using a MacBook. I like Apple products, because of their reliability. They are also very much useful at iOS programming.""" # Alper's paragraph about his life and also it's the measurement for his step count.
alper_list = alper_paragraph.split() # Creates a list made from the words in the paragraph above.

distance = 0 # Predefined distance variable.
for way in range(len(alper_list)): # A loop that creates a huge spiral made from 500 steps by counting the characters in the list.
    alper.stamp() # Alper's footprint.
    distance = distance + len(alper_list[way]) # Counting the length of each element in the list and adds to the distance variable.
    alper.speed(distance + 1) # Alper's speed.
    alper.forward(distance) # Alper's steps.
    alper.right(50) # Alper's direction.
    print(distance) # To check Alper whether he is lying or not.

for color in colors:
    alper.stamp()
    alper.speed(10)
    if alper.pencolor() == "Black":
        alper.forward(50)
    elif alper.pencolor() == "Purple":
        alper.left(90)
        alper.forward(50)
    elif alper.pencolor() == "Indigo":
        alper.left(90)
        alper.forward(50)
    elif alper.pencolor() == "Blue":
        alper.right(90)
        alper.forward(50)
    elif alper.pencolor() == "Yellow":
        alper.right(90)
        alper.forward(50)
    elif alper.pencolor() == "Orange":
        alper.left(90)
        alper.forward(50)
    elif alper.pencolor() == "Magenta":
        alper.left(90)
        alper.forward(50)
    elif alper.pencolor() == "Cyan":
        alper.forward(100)
    elif alper.pencolor() == "Chartreuse":
        alper.forward(50)
        alper.left(90)
    elif alper.pencolor() == "Gold":
        alper.forward(50)
        alper.left(90)
    elif alper.pencolor() == "Pink":
        alper.forward(50)
        alper.right(90)
    elif alper.pencolor() == "Olive":
        alper.forward(50)
        alper.right(90)
    elif alper.pencolor() == "Brown":
        alper.forward(50)
        alper.left(90)
    elif alper.pencolor() == "Coral":
        alper.forward(50)
        alper.left(90)
    elif alper.pencolor() == "Maroon":
        alper.forward(50)
    elif alper.pencolor() == "Crimson":
        alper.forward(100)
    elif alper.pencolor() == "Black":
        alper.forward(0)

    alper.pencolor(color)

wn.exitonclick() # To terminate the program manually