from turtle import Turtle,Screen
import random


screen = Screen()

screen.setup(width=500,height=400)
insert_value = screen.textinput(title='Make your bet', prompt="Which turtle will win the race?\n Choose your color: ")
print(insert_value)

color = ['red','green','pink','blue','orange','brown']
direction = [-140,-90,-40,10,60,110]
turtle_list = []
for index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color[index])
    new_turtle.goto(x=-230, y=direction[index])
    turtle_list.append(new_turtle)
if insert_value:
    is_race_on = True
while is_race_on:
    for turtle in  turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == insert_value:
                print("You've won the race!!!")
            else:
                print(f"You loose the race {winning_color} turtle won the race")
            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)









screen.exitonclick()
