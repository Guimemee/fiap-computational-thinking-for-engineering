import RPi.GPIO as gpio
import time

sensor1 = 12
sensor2 = 15
sensor3 = 16
sensor4 = 18
motor = 13

gpio.setmode(gpio.BOARD)

gpio.setup(sensor1, gpio.IN)
gpio.setup(motor, gpio.OUT)
gpio.setup(sensor2, gpio.IN)
gpio.setup(sensor3, gpio.IN)
gpio.setup(sensor4, gpio.IN)

def aquecimento():
    gpio.output(motor, gpio.LOW)
    time.sleep(3)
    gpio.output(motor, gpio.HIGH)
    return

def resfriamento():
    gpio.output(motor, gpio.LOW)
    time.sleep(4)
    gpio.output(motor, gpio.HIGH)
    return

while 1:
    s1 = gpio.input(sensor1)
    if s1 == 0:
        gpio.output(motor, gpio.HIGH)
    s2 = gpio.input(sensor2)
    if s2 == 0:
        aquecimento()
    s3 = gpio.input(sensor3)
    if s3 == 0:
        resfriamento()
    s4 = gpio.input(sensor4)
    if s4 == 0:
        gpio.output(motor, gpio.LOW)
