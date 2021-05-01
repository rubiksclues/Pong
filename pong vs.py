#import turtle
import turtle
#import os

#creates game window, capital S
wn = turtle.Screen()
#titles game
wn.title("Pong by @Rubiksclues")
#sets background color of the game window
wn.bgcolor("black")
#size of game window
wn.setup(width=800, height=600)
#stops window from updating, speeds up game 
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Game Paddle L
left_paddle = turtle.Turtle()
#speed of animation of paddle left, set to lowest/fastest setting
left_paddle.speed(0)
#paddle shape
left_paddle.shape("square")
#paddle color
left_paddle.color("white")
#sizes the left paddle so it is wider than the default pixel size of the square
left_paddle.shapesize(5, 1)
#allows the paddle to move up and down
left_paddle.penup()
#starting point of paddle, 0 is middle.
left_paddle.goto(-350, 0)


#Game Paddle R
right_paddle = turtle.Turtle()
#speed of animation of right paddle
right_paddle.speed(0)
#shape of right paddle
right_paddle.shape("square")
#color of right paddle
right_paddle.color("white")
#adjusts length of square of right paddle, to make it longer
right_paddle.shapesize(5, 1)
#allows paddle to move up and down
right_paddle.penup()
#starting point of right paddle
right_paddle.goto(350, 0)

#Ball
ball = turtle.Turtle()
#animation speed of the ball
ball.speed(0)
#shape of the ball
ball.shape("circle")
#color of the ball
ball.color("white")
ball.penup()
ball.goto(0,0)
"""ball movement, set into two parts: an x movement, and a y movement """
#this makes the ball move up, with y and to the right with x
ball.dx = 0.20
ball.dy = 0.20

#score pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B:0 ", align="center", font=("Courier", 24, "normal"))





#Function to move the left paddle up 
def left_paddle_up():
    #assigns current paddle position to y coordinate
    y = left_paddle.ycor()
    #add 20 pixels upwards to y coordinate
    y += 30
    #sets paddle to that y position
    left_paddle.sety(y)
    
#Function to move left paddle down
def left_paddle_down():
    #assigns variable to current y position of paddle
    y = left_paddle.ycor()
    #move paddle 20 pixels down
    y -= 30
    #sets paddle to that y position
    left_paddle.sety(y)
    
#Function to move right paddle up
def right_paddle_up():
    #sets current y position of right paddle to a variable
    y = right_paddle.ycor()
    #moves paddle 20 pixels downward
    y += 30
    #connects the y movement to the paddle
    right_paddle.sety(y)

#function to move right paddle down
def right_paddle_down():
    #sets y position of paddle to a variable
    y = right_paddle.ycor()
    #moves paddle 20 pixels down
    y -= 30
    #sets paddle to that new y position
    right_paddle.sety(y)

#keyboard binding 
#tells turtle to listen for keyboard input
wn.listen()
#moves left paddle up when user presses w by calling on left_paddle_up function above, wont work for capslocked W
wn.onkeypress(left_paddle_up, "w")
#moves left paddle down when user presses s
wn.onkeypress(left_paddle_down, "s")
#moves right paddle up when user presses up arrow
wn.onkeypress(right_paddle_up, "Up")
#moves right paddle down when user presses down arrow
wn.onkeypress(right_paddle_down, "Down")

#Main game loop
while True:
    #everytime the loop runs, the game window updates
    wn.update()
    
    #move the ball
    #sets balls position, and moves it
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    #height of window is 600, so the border is at 300.
    if ball.ycor() > 290:
        #sets ball back to the border point of the screen
        ball.sety(290)
        #reverses direction of ball
        ball.dy *= -1
    #same as above for the bottom border of the window    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        #if ball touches past the paddles on right, ball is returned to center, player a scores
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        #if ball goes past paddles on left it returns to middle and changes direction, player b scores
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    #ball and  right paddle collision
    if ball.xcor() > 340 and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        #turns ball around when it hits paddle
        ball.dx *= -1
    #ball and left paddle collision
    if ball.xcor() < -340 and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        #turns ball around when it hits paddle
        ball.dx *= -1