import turtle
import math
bob= turtle.Turtle()
print(bob)
bob.fd

def polygon(t: turtle.Turtle, length: float, n: int):
    """Dibuja un poligono regular,
    de segmentos de tamaño length(in pixels), de n lados
    """
    assert length > 0, "length debe ser mayor que 0"
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
#polygon(bob, -50, n=3)

def square(t: turtle.Turtle, length: float):
    """Dibuja un cuadrado,
    de segmentos de tamaño length(in pixels)
    """
    polygon(t,length= length, n=4)
#square(bob, 50)

def circle(t: turtle.Turtle, r: int):
    """
    Dibuja un circulo de radio r.

    Como se hizo:
    Necesitamos utilizar la funcion polygon,
    La circunferencia= length * n,
    La circunferencia= 2*r*pi,
    Por conveniencia n=500,
    length= circunferencia/n.
    """
    n= 500
    c= 2*r*math.pi
    polygon(t,c/n, n)
#circle(bob, r=100)

def arc(t: turtle.Turtle, r: int, angle: int) -> None:
    """
    Dibuja un arco de radio r y angulo angle(in degrees).

    Como se hizo:
    Necesitamos utilizar la funcion polygon
    La circunferencia= length * n
    La circunferencia= 2*r*pi
    Por conveniencia n=500
    length= circunferencia/n
    """
    assert r > 0, "radio debe ser positivo"
    c= 2*r*math.pi
    n= round(c/5) +3
    length= c/n
    for i in range(round(angle/360*n)):
        t.fd(length)
        t.lt(360/n)
arc(bob, 100, angle= 360)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
#arc2(bob, 100, angle= 180)
turtle.mainloop() 