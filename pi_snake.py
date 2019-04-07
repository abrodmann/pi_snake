#!/usr/bin/python3

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

def pushed_up(event):
	global direction
	if event.action == ACTION_RELEASED:
		direction = "up"

def pushed_down(event):
	global direction
	if event.action == ACTION_RELEASED:
		direction = "down"

def pushed_left(event):
	global direction
	if event.action == ACTION_RELEASED:
		direction = "left"

def pushed_right(event):
	global direction
	if event.action == ACTION_RELEASED:
		direction = "right"

def clamp(num):
	if num < 0:
		num = 0
	elif num > 7:
		num = 7
	return num

snakeColor = [ 255, 255, 255 ]
O = [ 0, 0, 0 ]
delay = 0.2
x = 4
y = 4
direction = "" # up, down, left, right

screen = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O
]

screen[y*8+x] = snakeColor

sense = SenseHat()
sense.clear
sense.set_pixels(screen)
sleep(delay)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

try:
	while True:
		screen[y*8+x] = O
		if direction == "up":
			y = clamp(y - 1)
		elif direction == "down":
			y = clamp(y + 1)
		elif direction == "left":
			x = clamp(x - 1)
		elif direction == "right":
			x = clamp(x + 1)
		screen[y*8+x] = snakeColor
		sense.set_pixels(screen)
		sleep(delay)
finally:
	sense.clear()

