COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(): #didn't inherit Turtle Class because nature of inheritance doesn't offer multiple different turtle instances 
    def __init__(self):
        self.all_cars=[]
        
    
        
    def create_car(self):    
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            turtle=Turtle('square') #didn't inherit Turtle Class because nature of inheritance doesn't offer multiple different turtle instances 
            turtle.penup()
            turtle.setheading(180)
            turtle.shapesize(stretch_wid=1,stretch_len=2)
            turtle.color(random.choice(COLORS))
            y_point=random.randint(-100, 250)
            x_point=random.randint(270,290)
            turtle.goto(x_point, y_point)
            self.all_cars.append(turtle)
            
    
        
    def move_cars(self):
        for i in self.all_cars:
            i.forward(STARTING_MOVE_DISTANCE) 
 
    
        

    
        
            
        
        
