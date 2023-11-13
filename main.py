from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scroreboard import scoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=500)
screen.bgcolor("black")
screen.title("Pong-Game")

scoreboard=scoreBoard()

player1=Paddle(side='left')
player2=Paddle(side='right')

screen.onkeypress(player2.up,"Up")
screen.onkeypress(player2.down,"Down")
screen.onkeypress(player1.up,"w")
screen.onkeypress(player1.down,"s")

screen.listen()

ball=Ball()
ball.start()

while player1.alive and player2.alive:
    screen.update()
    time.sleep(0.08)
    ball.move()
    if(ball.ycor()>=235 or ball.ycor()<=-235):
        ball.bounce_wall()
    if player1.distance(ball)<50 and ball.xcor()<=-350 and ball.xcor()>-370:
        ball.bounce_paddle()
    elif((player2.distance(ball)<50  and ball.xcor()>=350) and ball.xcor()<370):
        ball.bounce_paddle()
    if(ball.xcor()>370):
        scoreboard.clear()
        scoreboard.inc_score(0)
        ball.start()
    if(ball.xcor()<-370):
        scoreboard.clear()
        scoreboard.inc_score(1)
        time.sleep(0.5)
        ball.start()
        

    
screen.exitonclick()