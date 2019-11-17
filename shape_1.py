
import turtle as t

#여러개의 도형 그리기

angle=89
t.bgcolor("black")
t.color("yellow")
t.pensize(1)
t.speed(0)

for x in range(200):
    t.fd(x)
    t.lt(angle)

