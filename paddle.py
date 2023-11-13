from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,side):
        super().__init__()
        self.alive=True
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        x= -360 if side=="left" else 360
        y= 0 
        self.goto(x,y)
        self.setheading(90)
            
    def up(self):
        self.forward(20)
            
    def down(self):
        self.backward(20)
        
    # def did_lose(self):
    #     self.alive=False
