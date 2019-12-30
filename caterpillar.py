
import random as r
import turtle as t

#Create a catapillar turtle
t.bgcolor('orange')
cplr = t.Turtle()
cplr.shape('square')
cplr.color('blue')
cplr.speed(0)
cplr.penup()
cplr.hideturtle()

#Create a leaf turtle
leaf = t.Turtle()
leaf_shape = (0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14)
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
outside = False

#Add some text
text_t = t.Turtle()
text_t.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
text_t.hideturtle()

score_t = t.Turtle()
score_t.hideturtle()
score_t.speed(0)

def outside_window():
    #Stay inside the window
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2

    (x, y) = cplr.pos()

    outside = x > right_wall or x < left_wall or y > top_wall or y < bottom_wall
    return outside

def game_over():
    #cplr.color('orange')
    #leaf.color('orange')
    t.penup()
    #t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 50, 'bold italic'))
def display_score(current_score):
    score_t.clear()
    score_t.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50

    score_t.setpos(x, y)
    score_t.write(str(current_score), align='right', font=('Arial', 50, 'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(r.randint(-200, 200))
    leaf.sety(r.randint(-200, 200))
    leaf.st()

#Game starter
def start_game():
    global game_started
    global outside

    if game_started:
        return

    #Setup variables for game starting
    game_started = True
    score = 0
    text_t.clear()
    cplr_speed = 2
    cplr_length = 3
    cplr.shapesize(1, cplr_length, 1)
    cplr.showturtle()
    display_score(score)
    place_leaf()
    
    
    #Get Moving
    
    while True:
        cplr.forward(cplr_speed)
        if cplr.distance(leaf) < 20:
            place_leaf()
            cplr_length = cplr_length + 1
            cplr.shapesize(1, cplr_length, 1)
            cplr_speed = cplr_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            game_started = False
            outside = False
            t.clear()
            cplr.setx(0)
            cplr.sety(0)
            text_t.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))

            t.listen()
            t.mainloop()

#            start_game()


def up_key():
    # check if catapillar is moving left or right
    if cplr.heading() == 0 or cplr.heading() == 180:
        cplr.setheading(90)

def down_key():
    # check if catapillar is moving left or right
    if cplr.heading() == 0 or cplr.heading() == 180:
        cplr.setheading(270)

def left_key():
    # check if catapillar is moving up or down
    if cplr.heading() == 90 or cplr.heading() == 270:
        cplr.setheading(180)

def right_key():
    # check if catapillar is moving up or down
    if cplr.heading() == 90 or cplr.heading() == 270:
        cplr.setheading(0)

#Bind and Listen
t.onkey(start_game, 'space')
t.onkey(up_key, 'Up')
t.onkey(down_key, 'Down')
t.onkey(left_key, 'Left')
t.onkey(right_key, 'Right')


t.listen()
t.mainloop()
