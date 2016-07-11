import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 60) #PIN, freq
servo.start(0) #duty

print('#entering loop, master')
try:
    while True:
        for i in range(0, 100, 10):
            print('duty cycle = %{0}'.format(i))
            servo.ChangeDutyCycle(i)
            time.sleep(0.5)
except:
    KeyboardInterrupt:
        print('#cleaning, master')
        servo.stop()
        GPIO.clenup()
            
            
