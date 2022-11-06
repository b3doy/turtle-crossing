import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Assign the player
kuya = Player()

# Assign the cars
car_manager = CarManager()

# Assign the level
level = Scoreboard()

# Assign the player movement with keyboard
screen.listen()
screen.onkey(kuya.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # detect the collision with the wall
    if kuya.ycor() > 280:
        kuya.start_position()
        car_manager.increase_speed()
        level.update_level()

    # Create new car & set the movement
    car_manager.create_car()    
    car_manager.car_movement()

    # detect the collision with the car
    for car in car_manager.cars:
        if kuya.distance(car) < 20:
            level.game_over() 
            game_is_on = False

screen.exitonclick()