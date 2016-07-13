import wiringpi as wPi
from time import sleep

pin = 18
wPi.wiringPiSetupGpio()

wPi.pinMode(pin, 2)
wPi.pwmSetMode(wPi.PWM_MODE_MS)
wPi.pwmSetClock(1920)
wPi.pwmSetRange(200)

def killing():
    print("killing")
    wPi.pwmWrite(pin, 0)
    wPi.pinMode(pin, 0)

try:
    for i in range(10):
        print(i)
        wPi.pwmWrite(pin, 15)
        sleep(0.5)
        wPi.pwmWrite(pin, 20)
        sleep(0.5)
        wPi.pwmWrite(pin, 10)
        sleep(0.5)
    killing()

except KeyboardInterrupt:
    killing()
