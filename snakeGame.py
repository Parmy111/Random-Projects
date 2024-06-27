import turtle
import time
import random

delay = 0.1

#Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Light Blue")
wn.setup(width=600, height=600) #height and width of the screen
wn.tracer(0) #Turns off the animation on the screen

#Snake Head
head = turtle.Turtle()
head.speed(0) #gives the snake's head the fastest animation speed
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Functions
def goDown():
    if head.direction != "up":
        head.direction = "down"
def goUp():
    if head.direction != "down":
        head.direction = "up"
def goLeft():
    if head.direction != "right":
        head.direction = "left"
def goRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


food = turtle.Turtle()
food.speed(0) #gives the snake's head the fastest animation speed
food.shape("square")
food.color("dark green")
food.penup()
food.goto(0, 100)

#other Bodyparts
segments = []
#Keyboard Functions
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goLeft, "a")
wn.onkeypress(goRight, "d")

#Main Game Loop
while True:
    wn.update() #every time you go through the loop it updates the screen

    #Check for collison with wall
    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for i in segments:
            i.goto(1000,1000)
        #clear segments list
        segments.clear()

    #checking collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)   
    #Move the segments with the snake (Moving end segments first)
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #Move Segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    
    #check for body colisions
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for i in segments:
                i.goto(1000,1000)
        #clear segments list
            segments.clear()

    time.sleep(delay)
wn.mainloop() #keeps window open for us