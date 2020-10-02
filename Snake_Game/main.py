import os
import turtle
import time
import random
hız = 0.1

#score
score = 0
high_score = 0

#pencere olusturma

pencere = turtle.Screen()
pencere.title("Snake Game by gogizer")
pencere.bgcolor("lightblue")
pencere.setup(width=600, height=600)
pencere.tracer(0) #Ekran yenılemeyı kapatır

#Yılan kafası xd

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("circle") #kafa seklını kare yaptık 'square yazarak'
kafa.color("black")
kafa.penup()
kafa.goto(0, 0)
kafa.direction = "stop"

#food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))

#fonksiyonlar

def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"

def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"

def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"

def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)

    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)

    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)

    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)


#klavye baglantısı

pencere.listen()
pencere.onkeypress(go_up, "w")
pencere.onkeypress(go_down, "s")
pencere.onkeypress(go_right, "d")
pencere.onkeypress(go_left, "a")

#main game loop

while True:
    pencere.update()

    if kafa.xcor() > 290 or kafa.xcor() < -290 or kafa.ycor() > 290 or kafa.ycor() < -290:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        hız = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    if kafa.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        hız -= 0.001

        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            hız = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))



    time.sleep(hız)





pencere.mainloop()


© 2020
GitHub






