from turtle import Turtle

class Invaders():
    
    def __init__(self):
        self.invaders = []
        self.x_pos = [ -135, -90, -45, 0, 45, 90, 135]
        self.y_pos = [ 155, 180, 205, 230]
        self.move_x = 1
        self.move_y = 5
        self.create_enemy()
    
    def create_enemy(self):
        for i in range(len(self.y_pos)):
            for j in range(len(self.x_pos)):
                self.enemy = Turtle()
                self.enemy.shape('square')
                self.enemy.color('red')
                self.enemy.shapesize(stretch_wid=1, stretch_len=1.5)
                self.enemy.penup()
                self.enemy.goto(self.x_pos[j], self.y_pos[i])
                self.invaders.append(self.enemy)
    
    def move_h(self):
        for enemy in self.invaders:
            enemy.goto(enemy.xcor() - self.move_x, enemy.ycor())
    
    def move_v(self):
        self.move_x *= -1
        for enemy in self.invaders:
            enemy.goto(enemy.xcor() - self.move_x, enemy.ycor() - self.move_y)
        
    def new(self):
        self.create_enemy()
        self.move_x += 2
        self.move_y += 5
    
    def delete(self, block):
        block.ht()
        self.invaders.remove(block)