import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50) #PIN, freq

print('duty = 1')
servo.start(1) #duty
sleep(1)

print('duty = 16')
servo.start(16) #duty
sleep(1)

print('cleaning, master')
servo.stop()
GPIO.cleanup()
