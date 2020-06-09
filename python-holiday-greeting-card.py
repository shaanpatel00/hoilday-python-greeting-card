#-----------------------------------#
#Python Holiday Greeting Card Project
#Shaan Patel
#Class: Mrs. Herrmann
#12/12/2019
#-----------------------------------#

#-----SETUP-----#

from turtle import *
space = Screen()
santa = Turtle()
flash = Turtle()
flash.speed('fastest')
santa.speed('fastest')

backRepeatVarFlash = -400
backRepeatVarSanta = -380

#-----PROCEDURES-----#
def backgroundLine(turtle, dist):
    turtle.left(90)
    turtle.pendown()
    turtle.forward(dist)
    turtle.right(90)
    turtle.penup()
    
#To make this next procedure I needed to make a turtle face one way no matter the direction it is facing. I used the set heading command: turtle.seth(to_angle).
#0 would be east, 90 would be north, 180 would be west, and 270  would be south.

#I searched how to repeat parts of code online.
#You just have to put: for x in range of (value1, value 2).
#It is easiest to have value1 set to 1
#The difference between value1 and value2 should be one greater than the desired amount of repeats
#Ex. If I wanted to repeat 4 times, value1 = 1 and value2 = 5

#I had learned if statements sometime before this project and used them with boolean logic below.
def star(turtle, size, logic, pensize):
    turtle.pensize(pensize)
    turtle.seth(0)
    if(logic == 1):
        turtle.begin_fill()
    elif(logic == 0):
        turtle.seth(0)
    for x in range(1, 6):        
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        
    if(logic == 1):
        turtle.end_fill()
    elif(logic == 0):
        turtle.seth(0)
    
#-----COLORS-----#
#Dark Yellow: #EAAC57
#Light Yellow: #ECB161
#Brown: #AA5E2C
#Green: #4E7139
#Red: #ED1B24
#White: #FFFFFF

#-----Background-----#
#I searched how to use custom colors: turtle.pencolor('hex code')
    
flash.pencolor('#ECB161')
flash.pensize(20)
flash.penup()
santa.pencolor('#EAAC57')
santa.pensize(20)
santa.penup()

#I searched how to repeat parts of code online.
#You just have to put: for x in range of (value1, value 2).
#It is easiest to have value1 set to 1
#The difference between value1 and value2 should be one greater than the desired amount of repeats
#Ex. If I wanted to repeat 4 times, value1 = 1 and value2 = 5

for x in range(1,21):
    flash.goto(backRepeatVarFlash, -400)
    backgroundLine(flash, 805)
    backRepeatVarFlash = backRepeatVarFlash + 40

for x in range(1, 21):
    santa.goto(backRepeatVarSanta, -400)
    backgroundLine(santa, 805)
    backRepeatVarSanta = backRepeatVarSanta +40

#-----Tree-----#

#I searched how to fill in shapes online.
#Have to use turtle.begin_fill() before creating a closed shape and turtle.end_fill() after finished.
#-----Top Green-----#
flash.penup()
flash.pencolor('#4E7139')
flash.pensize(1)
flash.fillcolor('#4E7139')
flash.begin_fill()
flash.goto(-70, 200)
flash.pendown()
flash.goto(0, 350)
flash.goto(55, 240)
flash.goto(-70, 200)
flash.end_fill()

#-----Top Red-----#
santa.penup()
santa.pencolor('#ED1B24')
santa.pensize(1)
santa.fillcolor('#ED1B24')
santa.begin_fill()
santa.goto(-55, 195)
santa.pendown()
santa.goto(35, 218)
santa.goto(180, -20)
santa.goto(-155, 60)
santa.goto(-55, 195)
santa.end_fill()

#-----Bottom Green-----#
flash.penup()
flash.begin_fill()
flash.goto(-105, 40)
flash.pendown()
flash.goto(75, -10)
flash.goto(175, -200)
flash.goto(-250, -130)
flash.goto(-105, 40)
flash.end_fill()

#-----Bottom Red-----#

santa.penup()
santa.begin_fill()
santa.goto(-180, -160)
santa.pendown()
santa.goto(140, -205)
santa.goto(-230, -250)
santa.goto(-180, -160)
santa.end_fill()

#-----Trunk-----#

flash.penup()
flash.pencolor('#AA5E2C')
flash.fillcolor('#AA5E2C')
flash.begin_fill()
flash.goto(-30, -235)
flash.pendown()
flash.goto(10, -230)
flash.goto(20, -290)
flash.goto(-40, -290)
flash.goto(-30, -235)
flash.end_fill()

#-----BANNER-----#

#-----Banner Background-----#

flash.penup()
flash.begin_fill()
flash.goto(-250, -310)
flash.pendown()
flash.goto(250, -310)
flash.goto(290, -380)
flash.goto(-290, -380)
flash.goto(-250, -310)
flash.end_fill()

#-----Banner Writing-----#
#-----H-----#
santa.penup()
santa.pensize(5)
santa.pencolor('#FFFFFF')
santa.goto(-190, -320)
santa.pendown()
santa.goto(-190, -370)
santa.goto(-190, -345)
santa.goto(-210, -345)
santa.goto(-210, -370)
santa.goto(-210, -320)

#-----A-----#
santa.penup()
santa.goto(-180, -370)
santa.pendown()
santa.goto(-170, -320)
santa.goto(-160, -370)
santa.goto(-165, -345)
santa.goto(-175, -345)

#-----P-----#
santa.penup()
santa.goto(-150, -370)
santa.pendown()
santa.goto(-150, -320)
santa.goto(-130, -320)
santa.goto(-130, -345)
santa.goto(-150, -345)

#-----P-----#
santa.penup()
santa.goto(-120, -370)
santa.pendown()
santa.goto(-120, -320)
santa.goto(-100, -320)
santa.goto(-100, -345)
santa.goto(-120, -345)

#-----Y-----#
santa.penup()
santa.goto(-90, -370)
santa.pendown()
santa.goto(-70, -320)
santa.penup()
santa.goto(-80, -345)
santa.pendown()
santa.goto(-90, -320)

#-----H-----#
santa.penup()
santa.goto(-20, -320)
santa.pendown()
santa.goto(-20, -370)
santa.goto(-20, -345)
santa.goto(-40, -345)
santa.goto(-40, -370)
santa.goto(-40, -320)

#-----O-----#
santa.penup()
santa.goto(-10, -320)
santa.pendown()
santa.goto(-10, -370)
santa.goto(10, -370)
santa.goto(10, -320)
santa.goto(-10, -320)
#-----L-----#
santa.penup()
santa.goto(20, -320)
santa.pendown()
santa.goto(20, -370)
santa.goto(40, -370)
#-----I-----#
santa.penup()
santa.goto(50, -320)
santa.pendown()
santa.goto(70, -320)
santa.goto(60, -320)
santa.goto(60, -370)
santa.goto(70, -370)
santa.goto(50, -370)
#-----D-----#
santa.penup()
santa.goto(80, -320)
santa.pendown()
santa.goto(100, -320)
santa.goto(100, -370)
santa.goto(80, -370)
santa.goto(85, -370)
santa.goto(85, -320)
#-----A-----#
santa.penup()
santa.goto(110, -370)
santa.pendown()
santa.goto(120, -320)
santa.goto(130, -370)
santa.goto(125, -345)
santa.goto(115, -345)
#-----Y-----#
santa.penup()
santa.goto(140, -370)
santa.pendown()
santa.goto(160, -320)
santa.penup()
santa.goto(150, -345)
santa.pendown()
santa.goto(140, -320)
#-----S-----#
santa.penup()
santa.goto(190, -320)
santa.pendown()
santa.goto(170, -320)
santa.goto(170, -345)
santa.goto(190, -345)
santa.goto(190, -370)
santa.goto(170, -370)
#-----!-----#
santa.penup()
santa.goto(200, -320)
santa.pendown()
santa.goto(200, -355)
santa.penup()
santa.goto(200, -365)
santa.pendown()
santa.goto(200, -370)


#-----Stars-----#
flash.penup()
flash.goto(200, 200)
flash.pencolor('#FFFFFF')
flash.fillcolor('#FFFFFF')
flash.pendown()
star(flash, 25, 0, 3)
flash.penup()
flash.goto(-200, 15)
flash.pendown()
star(flash, 15, 0, 3)
flash.penup()
flash.goto(-280, 250)
flash.pendown()
star(flash, 25, 1, 3)
flash.penup()
flash.goto(-320, -220)
flash.pendown()
star(flash, 25, 0, 3)
flash.penup()
flash.goto(180, -55)
flash.pendown()
star(flash, 15, 1, 3)
flash.penup()
flash.goto(280, -250)
flash.pendown()
star(flash, 25, 1, 3)

#-----Move Turtles-----#
flash.penup()
santa.penup()
flash.goto(-410, -410)
santa.goto(-410, -410)
