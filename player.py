STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        print('Player turtle created')
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def player_reset(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    