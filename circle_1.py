
import turtle as t

#여러개의 원 그리기

n=10
t.shape("arrow")
t.bgcolor("black")
t.color("green")
t.pensize(1)
t.speed(0)

for x in range(n):
    t.circle(80)
    t.lt(360/n)

