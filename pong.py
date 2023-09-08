import turtle
import winsound
from turtle import *
screen = turtle.Screen()

#screen-edit
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(width=1000, height=800) 

#border
border = turtle.Turtle()
border.color('green')
border.speed(0)
border.penup()
border.goto(400,0)
border.pensize(2)
border.hideturtle()
border.pendown()
border.left(90)
border.forward(300)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(300)

#objects
#game-title
penup()
turtle.setpos(-79,250)
turtle.color("white")
hideturtle()
write("PONG GAME",move ="false", font=("verdana",20,"bold"))

#score
score_1=0
score_2=0

#paddle-1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(4, 0.5)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)

#paddle-2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(4, 0.5)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)

#Ball
ball_1 = turtle.Turtle()
ball_1.shape("circle")
ball_1.shapesize(0.6)
ball_1.color("white")
ball_1.penup()
ball_1.goto(0, 0)
ball_1.dx = 2.8
ball_1.dy = 2.8


# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write(" PLAYER 1 = 0  PLAYER 2 = 0 ", align = "center", font= ("courier",15,"bold"))

#Functions

#Resetting ball to center
def reset_ball():
    penup()
    hideturtle()
    ball_1.goto(0,0)

#Paddle movement
def paddle_1_up():
    y = paddle_1.ycor()
    y += 35
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 35
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 35
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 35
    paddle_2.sety(y)


#keyboard binding
#(left paddle- w & s, right paddle- up & down arr)
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

#Main-game loop 
running=True

while running:
  screen.update()

#to move the ball
  ball_1.setx(ball_1.xcor() + ball_1.dx)
  ball_1.sety(ball_1.ycor() + ball_1.dy) 

# checking border 
  #paddle
  if paddle_1.ycor() > 280:
    paddle_1.sety(280)

  if paddle_1.ycor() < -280:
    paddle_1.sety(-280)

  if paddle_2.ycor() > 280:
    paddle_2.sety(280)

  if paddle_2.ycor() < -280:
    paddle_2.sety(-280)
  #ball 
  #1. top and bottom 
  if ball_1.ycor() > 288:
    ball_1.sety(288)
    ball_1.dy = ball_1.dy * -1
    winsound.PlaySound('Pong bounce.wav', winsound.SND_FILENAME| winsound.SND_ASYNC)

  if ball_1.ycor() < -288:
    ball_1.sety(-288)
    ball_1.dy = ball_1.dy * -1
    winsound.PlaySound('Pong bounce.wav', winsound.SND_FILENAME| winsound.SND_ASYNC)

  #2. right and left
  if ball_1.xcor() > 390: 
    reset_ball()
    ball_1.dx = ball_1.dx * -1
    score_1 = score_1 + 1
    pen.clear()
    pen.write(" PLAYER 1 = {}  PLAYER 2 = {} ".format(score_1, score_2),align="center",
    font= ("courier",15,"bold"))
    winsound.PlaySound('ball_tap.wav', winsound.SND_FILENAME)
    

  if ball_1.xcor() < -390: 
    reset_ball()
    ball_1.dx = ball_1.dx * -1
    score_2 = score_2 + 1
    pen.clear()
    pen.write(" PLAYER 1 = {}  PLAYER 2 = {} ".format(score_1, score_2), align = "center", 
    font= ("courier",15,"bold"))
    winsound.PlaySound('ball_tap.wav', winsound.SND_FILENAME)

  if score_1 == 3 or score_2==3:
     running=False   

# Collisions of ball and paddle 
  if (ball_1.xcor() > 340 and ball_1.xcor() < 
     350)and(ball_1.ycor() <
     paddle_2.ycor() + 40 and ball_1.ycor() > 
     paddle_2.ycor() - 
     40):
      ball_1.setx(340)
      ball_1.dx = ball_1.dx * -1
      winsound.PlaySound('ball_hit.wav', winsound.SND_FILENAME| winsound.SND_ASYNC)

  if (ball_1.xcor() < -340 and ball_1.xcor() > 
     -350)and(ball_1.ycor() <
     paddle_1.ycor() + 40 and ball_1.ycor() > 
     paddle_1.ycor() - 40):
     ball_1.setx(-340)
     ball_1.dx = ball_1.dx * -1
     winsound.PlaySound('ball_hit.wav', winsound.SND_FILENAME| winsound.SND_ASYNC)


pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,25)

if score_1==3:
  pen.write(" PLAYER 1 WINS", align = "center", font= ("courier",15,"bold"))
  
elif score_2==3:
  pen.write(" PLAYER 2 WINS", align = "center", font= ("courier",15,"bold"))
winsound.PlaySound('winner.wav', winsound.SND_FILENAME)
