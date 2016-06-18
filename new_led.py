import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

led = GPIO.PWM(13, 60)

led.start(0)
print('start')

for time in range(10):
    print('sube {0}'.format(time))
    for var in range(0, 100, 2):
        led.ChangeDutyCycle(var)
        sleep(0.01)

    print('baja {0}'.format(time))
    for var in range(0, 100, 2):
        led.ChangeDutyCycle(100-var)
        sleep(0.01)

led.stop()
GPIO.cleanup()
    
