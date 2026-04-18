from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait


m_left = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
m_right = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
s = ColorSensor(Port.C)

r0 = 50
e1 = 0
e2 = 0
kp = 4.5
kd = 0.7
speed = 150
l_speed = 0
r_speed = 0

while True:
    r = s.reflection()
    e1 = e2
    e2 = r0 - r

    mv = kp * e2 + kd * (e2 - e1)

    if mv > 0:
        l_speed = speed
        r_speed = speed * (100 - mv) / 100
    else:
        l_speed = speed * (100 + mv) / 100
        r_speed = speed
    print(f"r = {r}, mv = {mv}, l_speed = {l_speed}, r_speed = {r_speed}")
    m_left.run(l_speed)
    m_right.run(r_speed)
