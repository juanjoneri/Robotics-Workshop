import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.OUT)
servo = GPIO.PWM(15, 50) #PIN, freq
servo.start(2)

#min 100/20 = 5
#max (2*100)/20 = 10

try:
    for i in range(10):
        position = i

        print("duty = {}".format(position))
        servo.ChangeDutyCycle(2+position) #duty
        sleep(.8)
except KeyboardInterrupt:
    print('cleaning, master')
    servo.stop()
    GPIO.cleanup()
    
print('cleaning, master')
servo.stop()
GPIO.cleanup()
