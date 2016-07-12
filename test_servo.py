from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
servo = GPIO.PWM(37, 50)
servo.start(6)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=6, to_=12, orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, angle):
        duty = float(angle)
        print(duty)
        servo.start(duty)

root = Tk()
root.wm_title("servo control")
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()

print('killing')
servo.stop()
GPIO.cleanup()
