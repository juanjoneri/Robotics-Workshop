#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO

#FUNCIONES PRINCIPALES ------------------------
#----------------------------------------------

def rightClicked(val):
    print("right") 
    motor1.ChangeDutyCycle( (3/2) * baseDuty )
    

def rightReleased(val):
    print("right")
    motor1.ChangeDutyCycle(baseDuty)

def leftClicked(val):
    print("left")
    motor2.ChangeDutyCycle( (3/2) * baseDuty )

def leftReleased(val):
    print("left")
    motor2.ChangeDutyCycle(baseDuty)

def killClicked():
    print('killing')
    motor1.stop()
    motor2.stop()
    GPIO.cleanup()

def sliderChanged(value):
    global baseDuty
    baseDuty = float(value)/2
    motor1.ChangeDutyCycle(baseDuty)
    motor2.ChangeDutyCycle(baseDuty)

#CONFIGURATION AND SETUP ----------------------
#COSAS ABURRIDAS ------------------------------

def configureGpio():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(15, GPIO.OUT)
    motor1 = GPIO.PWM(15, 60)
    motor1.start(0)

    GPIO.setup(13, GPIO.OUT)
    motor2 = GPIO.PWM(13, 60)
    motor2.start(0)
    
    return motor1, motor2

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
    motor1, motor2 = configureGpio()
    baseDuty = 0
    configureWindow(root)
    makeWidgets(root)
    root.mainloop()
    killClicked()
