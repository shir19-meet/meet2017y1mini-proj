import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH =7

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for START_LENGTH in range(6):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    x=snake.stamp()
    stamp_list.append(x)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP="100"
UP=0
LEFT=1
DOWN=2
RIGHT=3

ditection=UP

def up():
    global direction
    direction=UP
    move_snake()
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    move_snake()
    print("You pressed the down key!")

def left():
    global direction
    direction=LEFT
    move_snake()
    print("You pressed the left key!")

def right():
    global direction
    direction=LEFT
    move_snake()
    print("You pressed the right key!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake_pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(z_pos,y_pos-SQUARE_SIZE)
        print("You moved down!")
    
          
    
    
