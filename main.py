from turtle import Screen

from scoreboard import Scoreboard
from snakebody import Snake
from food import Food
import time

# Game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Setting Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # sets screen background color
screen.title("My Snake Game")
screen.tracer(0)  # Turn off animation
# Listen to key presses
screen.listen()
screen.onkey(snake.up, "Up")  # takes command
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Game loop
game_is_on = True  # It is a flag, That decides the while loop
while game_is_on:
    screen.update()  # Refresh Screen
    time.sleep(0.1)  # Control Speed
    snake.move()
    # Detect Collison with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    #     scoreboard.increase_score()
    #
     # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
    #     game_is_on = False
    #     scoreboard.game_over()
    #
    #     # Detect collision with tail
    for segment in snake.segments[1:]:
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
