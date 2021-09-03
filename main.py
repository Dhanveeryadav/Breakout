# ------------------------------------------- Modules--------------------------------------------------
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from score import Score
from lives import Lives

# -------------------------------------------- objects-------------------------------------------------------
my_screen = Screen()
paddle = Paddle((0, -250))
ball = Ball()
score = Score()
lives = Lives()

# ----------------------------------------- screen setup -------------------------------------------------------
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)


my_screen.listen()
my_screen.onkey(paddle.right_side, "Right")
my_screen.onkey(paddle.left_side, "Left")

# list of position for the bricks (wall)
x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205, 180]
bricks = []

# --------------------------------------------creating bricks------------------------------------------------------
for i in x_list:
    for j in y_list:
        my_bricks = Brick(i, j)
        bricks.append(my_bricks)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.refresh()

    # paddle bounce
    if -240 <= ball.ycor() <= -230 and paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60:
        ball.bounce_y()

    # border bounce
    if ball.xcor() <= -380 or ball.xcor() > 380:
        ball.bounce_x()
    if ball.ycor() >= 280:
        ball.bounce_y()
    if ball.ycor() < - 290:
        ball.position_reset()
        lives.lives_left()

        if lives.lives == 0:
            game_on = False
            lives.setposition(0, 0)
            lives.write("Game Over", align="center", font=("ariel", 24, "normal"))
            score.setposition(0, 50)
            score.result()

    # checking collision of ball with bricks and removing them.
    for i in bricks:
        if i.ycor() - 20 <= ball.ycor() <= i.ycor() + 20 and i.xcor() - 60 < ball.xcor() < i.xcor() + 60:
            i.goto(1000, 1000)
            bricks.remove(i)
            score.inc_score()
            score.update_score()

    # here is  slight problem when there is only one brick remaining, the game is over but last brick did not disapper.
    if len(bricks) == 0:
        lives.setposition(0, 0)
        lives.write("Game Over", align="center", font=("ariel", 24, "normal"))
        score.setposition(0, 50)
        score.result()
        game_on = False

my_screen.exitonclick()
