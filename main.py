import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake


def draw_grid(screen):
    # horizantal drawer
    pen_h = Turtle()
    pen_h.speed(0)
    pen_h.color("gray")
    # vertical drawer
    pen_v = Turtle()
    pen_v.speed(0)
    pen_v.color("gray")
    pen_v.left(90)
    for y in range(-300, 300, 30):
        pen_h.penup()
        pen_v.penup()
        pen_h.goto(-300, y)
        pen_v.goto(y, -300)
        pen_h.pendown()
        pen_v.pendown()
        pen_h.forward(600)
        pen_v.forward(600)
    pen_h.hideturtle()
    pen_v.hideturtle()


def is_collide(snake, food):
    if snake.head.distance(food) < 20:
        return True
    return False


def is_hit_wall(snake):
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        return True
    return False

def is_hit_body(snake):
    for seg in snake.body:
        if snake.head.distance(seg) < 10:
            return True
    return False
        

score = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#151515")
screen.title("My Snake Game")
screen.tracer(0)

# draw grid on screen
draw_grid(screen)

# Instantiate a snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keypress handling
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# game main loop
game_over = False
while not game_over:
    # referesh the screen
    screen.update()
    time.sleep(0.1)
    snake.move()

    if is_collide(snake, food):
        scoreboard.update_score()
        snake.grow()
        food.new()

    if is_hit_wall(snake) or is_hit_body(snake):
        game_over = True
        scoreboard.game_over()


screen.exitonclick()
