FONT = ("Courier", 24, "normal")
from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.penup()
        self.goto(-100, 270)
        self.color('black')
        self.hideturtle()
        self.write (f"Level: {self.level}", False, 'center', FONT)
    
    def update_level(self):
        self.clear()
        self.goto(-100, 270)
        self.level+=1
        self.write (f"Level: {self.level}", False, 'center', FONT)
        self.hideturtle()
       
    
    def game_over(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Game Over, Highest Level: {self.level}!", False, 'center', FONT)
        self.hideturtle()
    
    def reset(self):
        self.clear()
        self.level=0
        self.penup()
        self.goto(-100, 270)
        self.color('black')
        self.hideturtle()
        self.write (f"Level: {self.level}", False, 'center', FONT)
        


        
