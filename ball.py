from turtle import Turtle
import random
# from turtle import Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move =10
        self.y_move=10
        
    
    def start(self):
        x=0
        y=random.randint(-240,240)
        self.goto(x,y)
        if self.ycor()>0:
            self.setheading(random.randint(210,330))
        else:
            self.setheading(random.randint(30,150))
            
    def move(self):
        self.goto(self.xcor() + self.x_move,self.ycor() + self.y_move)
        
    def bounce_wall(self):
        self.y_move*=-1
    def bounce_paddle(self):
        self.x_move*=-1
if __name__=="__main__":
    from turtle import Screen
    screen=Screen()
    screen.bgcolor('black')
    screen.setup(800,500)
    ball=Ball()
    while True:
        ball.start()
        ball.forward(10)
    screen.exitonclick()