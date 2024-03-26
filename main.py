from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")

s.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(key="Up", fun=snake.snake_up)
s.onkey(key="Down", fun=snake.snake_down)
s.onkey(key="Right", fun=snake.snake_right)
s.onkey(key="Left", fun=snake.snake_left)


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # DETECT COLLISION WITH WALL

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # DETECT COLLOISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
           score.reset()
           snake.reset()

s.exitonclick()