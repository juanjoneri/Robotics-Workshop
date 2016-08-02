#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO

#FUNCIONES PRINCIPALES ------------------------
#----------------------------------------------


def rightClicked(val):
    servo.ChangeDutyCycle(10)

def rightReleased(val):
    servo.ChangeDutyCycle(8)

def leftClicked(val):
    servo.ChangeDutyCycle(6)

def leftReleased(val):
    servo.ChangeDutyCycle(8)

def killClicked():
    print('killing')
    motor.stop()
    servo.stop()
    GPIO.cleanup()

def sliderChanged(value):
    motor.ChangeDutyCycle(float(value))

#CONFIGURATION AND SETUP ----------------------
#COSAS ABURRIDAS ------------------------------

def configureGpio():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(15, GPIO.OUT)
    motor = GPIO.PWM(15, 60)
    motor.start(20)
    
    GPIO.setup(36, GPIO.OUT)
    servo = GPIO.PWM(36, 50)
    servo.start(8) # 1-8-16
    return motor, servo

def configureWindow(root):
    root.title("Control Remoto")
    root.geometry("800x400")
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 2)
    root.rowconfigure(2, weight = 1)
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)

def makeWidgets(root):
    slider = Scale(root, from_ = 0, to = 100, resolution = 1, orient = HORIZONTAL)
    slider.grid(row = 0, column = 0, columnspan = 2 , padx=20 , stick = 'ew')
    slider.config(command = sliderChanged)

    leftBtn = ttk.Button(root, text = "Left")
    leftBtn.grid(row = 1, column = 0, padx=30, pady=20, stick = 'nsew')
    leftBtn.bind('<ButtonPress-1>', leftClicked)
    leftBtn.bind('<ButtonRelease-1>', leftReleased)

    rightBtn = ttk.Button(root, text = "Right")
    rightBtn.grid(row = 1, column = 1, padx=30, pady=20, stick = 'nsew')
    rightBtn.bind('<ButtonPress-1>', rightClicked)
    rightBtn.bind('<ButtonRelease-1>', rightReleased)

    killBtn = Button(root, text = "Kill", background='red')
    killBtn.grid(row = 2, column = 0, padx=50, pady=50, columnspan = 2, stick = 'nsew')
    killBtn.config(command = killClicked)

#Ejecutamos todo el codigo
if __name__ == '__main__':
    root = Tk()
    motor, servo = configureGpio()
    configureWindow(root)
    makeWidgets(root)
    root.mainloop()
    killClicked()
