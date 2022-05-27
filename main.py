from turtle import Turtle, Screen
from spaceship import Spaceship
from invader import Invaders
from scoreboard import Board
from bullet import Bullet
import time


screen = Screen()
screen.setup(width=410, height=600)
screen.title("Space Invader")
screen.bgcolor('black')
game_on = True
screen.tracer(0)

user = Spaceship()
bullet = Bullet()
invaders = Invaders()
board = Board()

screen.listen()
screen.onkeypress(key="Right", fun=user.right)
screen.onkeypress(key="Left", fun=user.left)

while game_on:
    
    time.sleep(0.05)
    invaders.move_h()
    
    if bullet.fire == True:
        bullet.move()
    else:
        screen.onkeypress(key="space", fun=lambda x=user.xcor():bullet.shoot(x))
    screen.update()
        
    for invader in invaders.invaders:
        
        if invader.ycor() < -240:
            game_on = False
            board.game_over()
            
        if invader.xcor() < -180 or invader.xcor() > 180:
            invaders.move_v()
                          
        if bullet.distance(invader) < 30:
            board.getpoint()
            invaders.delete(invader)
            bullet.delete()
            
    if bullet.ycor() > 280:
        bullet.delete()
        
    if invaders.invaders == []:
        board.next_level()
        invaders.new()
        
screen.exitonclick()