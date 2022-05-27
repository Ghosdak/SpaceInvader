from turtle import Turtle

class Bullet(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.ht()
        self.shapesize(stretch_wid=0.8, stretch_len=0.3)
        self.color('white')
        self.goto(0,-250)
        self.move_speed = 0.05
        self.fire = False
        
    def move(self):
        self.goto( self.x, self.ycor() + 10)
        
    def shoot(self, x):
        self.x = x
        self.st()
        self.fire = True
        self.move()
    
    def delete(self):
        self.ht()
        self.fire = False
        self.goto(0,-250)
        
        