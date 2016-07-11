#for bash and LED

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #BOARD or BMC
GPIO.setup(13, GPIO.OUT) #[pin, mode]

led = GPIO.PWM(13, 60) #[pin, freq]

led.start(25) #%duty
led.ChangeDutyCycle(50)
led.ChangeFrequency(24)

led.stop()
GPIO.cleanup()
