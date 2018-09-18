# multiturt.py nrg

import turtle
tina = turtle.Turtle()
tina.shape("turtle")
molly = turtle.Turtle()
molly.shape("turtle")
wilson = turtle.Turtle()
wilson.shape("turtle")
turtle.bgcolor('black')

for x in range(300):

	tina.color('white')
	tina.forward(300)
	tina.speed(0)
	tina.left(151)
	tina.forward(x)	

	molly.speed(0)
	molly.left(60)	
	molly.color('navy')
	molly.forward(100)
	molly.left(256)
	molly.forward(x)	

	
	wilson.speed(0)
	wilson.left(359)
	wilson.color('red')
	wilson.forward(400)
	wilson.right(90)
	wilson.forward(x)
	
