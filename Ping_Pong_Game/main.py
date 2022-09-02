# This is a Python script for Ping Pong Game.

import turtle

# class definition
from turtle import fillcolor, Turtle


class MouseClick(Turtle):
    def glow(self, x, y):
        self.fillcolor("red")

    def unglow(self, x, y):
        self.fillcolor("")

wind = turtle.Screen()
wind.title("MSH Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# racket1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("blue")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.25
ball.dy = -0.25

# score
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.score1 = 0
score.score2 = 0
score.write(f"Player1: {score.score1} and Player2: {score.score2}", move=False, align="center",
            font=("Arial", 20, "normal"))


# functions definitions
def racket1_up():
    y = racket1.ycor() + 20
    racket1.sety(y)


def racket1_down():
    y = racket1.ycor() - 20
    racket1.sety(y)


def racket2_up():
    y = racket2.ycor() + 20
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor() - 20
    racket2.sety(y)


# Keyboard binding
wind.listen()
wind.onkeypress(racket1_up, "w")
wind.onkeypress(racket1_down, "s")
wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")


click = MouseClick()
click.onclick(click.glow, btn=1)
# click.onrelease(click.unglow)

while True:
    wind.update()

    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.dy *= -1
        ball.sety(290)

    if ball.ycor() < -290:
        ball.dy *= -1
        ball.sety(-290)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.score2 += 1
        score.clear()
        score.write(f"Player1: {score.score1} and Player2: {score.score2}", move=False, align="center",
                    font=("Arial", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.score1 += 1
        score.clear()
        score.write(f"Player1: {score.score1} and Player2: {score.score2}", move=False, align="center",
                    font=("Arial", 20, "normal"))

    # collision action
    if (-350 < ball.xcor() < -340) and (racket1.ycor() - 40 < ball.ycor() < racket1.ycor() + 40):
        ball.setx(-335)
        ball.dx *= -1

    if (340 < ball.xcor() < 350) and (racket2.ycor() - 40 < ball.ycor() < racket2.ycor() + 40):
        ball.setx(335)
        ball.dx *= -1
