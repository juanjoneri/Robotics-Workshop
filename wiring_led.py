import wiringpi as wPi
from time import sleep

pin = 18
wPi.wiringPiSetupGpio()

wPi.pinMode(pin, 2)

try:
    for i in range(50):
        
        print(i)
        
        for j in range(0, 1024):
            wPi.pwmWrite(pin, j)
            sleep(0.0005)
            
        for j in range(0, 1024):
            wPi.pwmWrite(pin, 1024-j)
            sleep(0.0005)

except KeyboardInterrupt:
    print("killing")
    wPi.pwmWrite(pin, 0)
    wPi.pinMode(pin, 0)
