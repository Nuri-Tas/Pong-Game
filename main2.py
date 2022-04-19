from turtle import Turtle, Screen
from ball import Ball
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

paddles = []
for i in range(2):
    paddle = Turtle("square")
    paddle.color("white")
    paddle.penup()
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.speed("fastest")
    paddles.append(paddle)

paddles[0].goto(-380, 0)
paddles[1].goto(380, 0)
screen.tracer(0)

def move_1_up():
    new_y = paddles[0].ycor() + 50
    paddles[0].goto(paddles[0].xcor(), new_y)


def move_1_down():
    new_y = paddles[0].ycor() - 50
    paddles[0].goto(paddles[0].xcor(), new_y)


def move_2_up():
    new_y = paddles[1].ycor() + 50
    paddles[1].goto(paddles[1].xcor(), new_y)


def move_2_down():
    new_y = paddles[1].ycor() - 50
    paddles[1].goto(paddles[1].xcor(), new_y)


screen.listen()
screen.onkey(move_1_up, "w")
screen.onkey(move_1_down, "s")
screen.onkey(move_2_up, "Up")
screen.onkey(move_2_down, "Down")

ball = Ball()

left_score = 0
right_score = 0

screen_speed = 0.1
playing = True
while playing:
    screen.update()
    time.sleep(screen_speed)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(paddles[0]) < 50 and ball.xcor() < -360 or ball.distance(paddles[1]) < 50 and ball.xcor() > 360:
        ball.bounce_x()
        screen_speed *= 0.9
    if ball.xcor() < -390:
        right_score += 1
        print("gamer 0 lost")
        ball.goto(0,0)
        ball.x_move *= -1
        screen_speed = 0.1
    elif ball.xcor() > 390:
        print("gamer 1 lost")
        ball.goto(0,0)
        ball.x_move *= -1
        screen_speed = 0.1


screen.exitonclick()