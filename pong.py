# Welcome to Po's Python Pong Game
# By Po Kealiinohomoku
# Intensive Project 1

import turtle

# Screen setup
win = turtle.Screen()
win.title("Po's Python Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Gameplay objects

# Player 1 Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Player 2 Paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Game ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.forward(100)

# Main Game Loop
while True:
    win.update()
