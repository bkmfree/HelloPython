
import turtle as t

#정오각형
n=5
t.shape("turtle")
t.color("purple")
t.begin_fill()
for x in range(n):
    t.fd(50)
    t.lt(360/n)
t.end_fill()

