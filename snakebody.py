from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The head of the snake

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a segment to the snake when it eats food."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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




# class Snake:
#     # Constructing the constructor
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head=self.segments[0] # Assing item 0 or the first square to be head.
#
#     # Snake shape and Snake body positioning
#     def create_snake(self):
#         for position in STARTING_POSITION:
#             new_segment = Turtle(shape="square")
#             new_segment.color("white")
#             new_segment.penup()
#             # new_segment.speed("slowest")
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#     # Moving the snake head from 3rd to 1st place and moving the body forward
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.fd(MOVE_DISTANCE)
#
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
