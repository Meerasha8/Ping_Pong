from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.title("pong")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
left_paddle=Paddle((-385,0))
right_paddle=Paddle((385,0))
screen.listen()
screen.onkey(right_paddle.go_up, key="Up")
screen.onkey(right_paddle.go_down, key="Down")
screen.onkey(left_paddle.go_up,key="w")
screen.onkey(left_paddle.go_down,key="s")
ball=Ball()
score=Score()

game_is_on=True
while game_is_on:
    time.sleep(ball.speeding)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if (ball.distance(right_paddle)<50 and ball.xcor()>355) or (ball.distance(left_paddle)<50 and ball.xcor()<-355):
        ball.bounce_x()
    if ball.xcor()>385:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-385:
        ball.reset_position()
        score.r_point()
    if score.score_l==5:
        score.display_winner("Left Side Wins")
        game_is_on=False
    elif score.score_r==5:
        score.display_winner("Right Side Wins")
        game_is_on=False



screen.exitonclick()