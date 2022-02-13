from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("Black")
screen.title("The Classic Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score = Scoreboard()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
game_is_on = True

counter = 0
while game_is_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    # Detect Collision with food

    if snake.head.distance(food) < 15:
        hold_of_color = food.refresh()
        score.increase_score()
        snake.extend(hold_of_color)

    # Detect Collision with Wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()




screen.exitonclick()
