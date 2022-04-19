from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

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

ball = Turtle("circle")
ball.penup()
ball.color("blue")
ball.goto(0, 0)


to_right = random.randint(-45, 45)
to_left = random.randint(135, 225)
directions = [to_right, to_left]
angle = random.choice(directions)


def move_ball():
    ball.setheading(angle)
    ball.forward(20)


playing = True
while playing:
    time.sleep(0.1)
    screen.update()
    move_ball()
    if ball.ycor() > 285:
        angle += 90
    elif ball.ycor() < -285:
        angle -= 90
    if ball.distance(paddles[0]) < 30:
            if angle >= 180:
                angle += 90
            else:
                angle -= 90
    if ball.distance(paddles[1]) < 30:
            if angle >= 180:
                angle -= 90
            else:
                angle += 90
    if ball.xcor() > 480 and ball.distance(paddles[1]) > 20:
        playing = False
        screen.title("gamer 1 lost")
    elif ball.xcor() < -480 and ball.distance(paddles[0]) > 20:
        playing = False
        screen.title("gamer 0 lost")
screen.exitonclick()
