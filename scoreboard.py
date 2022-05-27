from turtle import Turtle
import time

class Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.point = 0
        self.ht()
        self.penup()
        self.color('white')
        self.goto(135,-290)
        self.write(f"{self.point}", font=('Arial', 18, 'normal'))
        
    def getpoint(self):
        self.point += 20
        self.write_point()
    
    def write_point(self):
        self.goto(135,-290)
        self.clear()
        self.write(f"{self.point}", font=('Arial', 18, 'normal'))
        
    def next_level(self):
        self.goto(-50,0)
        self.clear()
        self.write(f"Next Level", font=('Arial', 18, 'normal'))
        time.sleep(0.5)
        self.write_point()
        
    def game_over(self):
        self.goto(-50,0)
        self.write(f"You Lose!", font=('Arial', 18, 'normal'))