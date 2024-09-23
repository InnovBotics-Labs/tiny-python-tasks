# EXTERNAL PACKAGE DEPENDENCIES
import time
import turtle as controller

# INTERNAL Modules
from Paddle import Paddle
from ScoreBoard import Scoreboard



# Create a Game screen
game_window = controller.Screen()
game_window.setup(height=600, width=600)
game_window.bgcolor("black")
game_window.title("Pong Game")
game_window.tracer(0)

# Create Paddle and its behaviours
left_paddle = Paddle("left")
right_paddle = Paddle("right")
divider = Paddle("wall")
ball = Paddle("ball")

left_scoreboard = Scoreboard("left")
right_scoreboard = Scoreboard("right")

# Mapping paddle with Keys
game_window.listen()

game_window.onkey(left_paddle.up, 'w')
game_window.onkey(left_paddle.down, 's')
game_window.onkey(right_paddle.up, 'Up')
game_window.onkey(right_paddle.down, 'Down')

game_over = False
while not game_over:
    game_window.update()
    time.sleep(0.1)
    ball.move()

    # Detect a collusion with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect a collusion with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 240 or ball.distance(left_paddle) < 50 and ball.xcor() < -240:
        ball.bounce_from_paddle()

    if ball.xcor() < -300:
        ball.home()
        left_scoreboard.increase_count()

    if ball.xcor() > 300:
        ball.home()
        right_scoreboard.increase_count()



game_window.exitonclick()





#  7. Detect when miss the paddle
#  8. keep the score