from turtle import Turtle

class Spaceship(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.goto(0,-250)
        
    def left(self):
        self.goto( self.xcor() - 20, self.ycor() )
        
    def right(self):
        self.goto( self.xcor() + 20, self.ycor() )
        
        