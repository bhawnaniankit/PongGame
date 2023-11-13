from turtle import Turtle
class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=[]
        self.score.append(0)
        self.score.append(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,190)
        x=Turtle()
        x.penup()
        x.color('white')
        x.hideturtle()
        x.goto(0,250)
        x.setheading(270)
        while(x.ycor()<=250 and x.ycor()>=-250):
            x.pendown()
            x.forward(20)
            x.penup()
            x.forward(20)
        self.write(f"{self.score[0]}  {self.score[1]}", True, align="center",font=("Arial",40,"normal"))
            
    def inc_score(self,index):
        self.goto(0,190)
        self.score[index]+=1
        self.write(f"{self.score[0]}  {self.score[1]}", True, align="center",font=("Arial",40,"normal"))
        
if __name__=="__main__":
    from turtle import Screen
    screen=Screen()
    screen.setup(800,500)
    screen.bgcolor('black')
    scrore=scoreBoard()
    screen.exitonclick()