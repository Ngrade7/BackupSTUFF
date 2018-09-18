# etur   cwc
from turtle import *
color("#00cc00", "#dddd00")
begin_fill()
while True:
    forward(200)
    left(170)
    speed(0)
    print (pos)
    if abs(pos()) < 1:
        break
end_fill()
done()
