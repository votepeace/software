

#play the game song
from pygame import mixer
mixer.init()
mixer.music.load(r"C:\Users\votepeace\Desktop\t.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()

screen.title("Peace's Turtle Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player() #player turtle 
carmanager=CarManager() #cars
scoreboard=Scoreboard() #scoreboard

screen.listen() #event & listen for the up arrow key 
screen.onkey(player.move_up, "Up") 
screen.onkey(player.move_down, "Down")


game_is_on = True


while game_is_on:
    time.sleep(0.1) #whenever while loop refreshes, .1 second delay before screen updates for pace of game 
    screen.update() #since screen.tracer(0), screen.update() is necessary to refresh the screen 
    
    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars: #if player crashes 
        if car.distance(player) <30:
            scoreboard.game_over()
            time.sleep(5)     
            scoreboard.reset()
            player.player_reset()
        
        elif player.distance((0, 280)) <5: #if player passes 
            scoreboard.update_level()
            player.player_reset()
            carmanager.move_cars_level_up()
        
            
screen.exitonclick()
