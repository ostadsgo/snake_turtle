from turtle import Turtle

# init position
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # all parts of snake
        self.segments = []
        self.create()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.body = self.segments[1:]


    def create(self):
        # create snake (head, body, tail)
        for pos in starting_pos:
            self.add_segment(pos)

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def grow(self):
        self.add_segment(self.tail.position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # head move forward
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
