import pygame
import RPi.GPIO as GPIO
import time

def killClicked():
    print('killing')
    motorR.stop()
    motorL.stop()
    GPIO.cleanup()
    pygame.joystick.quit()
    pygame.quit()

def configureGpio():
    right = 15 #Derecha 15    (->)
    left = 13  #Izquierda 13  (<-)
    freq = 60
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(right, GPIO.OUT)
    motorR = GPIO.PWM(right, freq)
    motorR.start(0)

    GPIO.setup(left, GPIO.OUT)
    motorL = GPIO.PWM(left, freq)
    motorL.start(0)

    print("pines {} and {} set up for PWM at {}Hz\n".format(right, left, freq))
    return motorR, motorL

def configurePigame():
    pygame.init()
    ###############################
    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    ###############################
    pygame.joystick.init()

def configureController():    

    joystick_count = pygame.joystick.get_count()
    print("Number of joysticks: {}".format(joystick_count) )
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    name = joystick.get_name()
    print("Joystick name: {}".format(name) )
    axes = joystick.get_numaxes()
    print("Number of axes: {}".format(axes) )
    buttons = joystick.get_numbuttons()
    print("Number of buttons: {}".format(buttons) )

    ###############################
    for i in range( buttons ):
        button = joystick.get_button( i )
        print("Button {:>2} value: {}".format(i,button) )
    ###############################
    return joystick

def updateMotors(axisLeft, axisRight, motorR, motorL):
    if axisLeft > 0:
        baseDuty = axisLeft*15
        rightCycle = baseDuty
        leftCycle = baseDuty

        #axisRight > 0 when turning right and < 0 when turning left
        #RIGHT -> leftCycle  += (+)
        #      -> rightCycle -= (+)
        #
        #LEFT  -> leftCycle  += (-)
        #      -> rightCycle -= (-)
        leftCycle += baseDuty*axisRight
        rightCycle -= baseDuty*axisRight

        motorR.ChangeDutyCycle(rightCycle)
        motorL.ChangeDutyCycle(leftCycle)

###########  MAIN METHOD ############
if __name__ == '__main__':
    #SETUP
    motorR, motorL = configureGpio()
    configurePigame()
    analogLPlace, analogRPlace = 1, 2
    print("\nSetup complete")
    
    #Main Loop
    running = True
    refreshRate = 20
    try:
        while running == True:
            joystick = configureController()
            axisLeft = -joystick.get_axis( 1 ) #  _0 : 1^
            axisRight = joystick.get_axis( 2 ) # <-1 : 1>
            btnO = joystick.get_button( 2 )
            
            updateMotors(axisLeft, axisRight, motorR, motorL)            
            
            joystick_count = pygame.joystick.get_count()
            if btnO == 1 | joystick_count < 1:
                #O pressed or connection lost QUIT
                running = False
            
            time.sleep(1/refreshRate)
    except KeyboardInterrupt:
        #Finalmente cerramos y nos vamos
        killClicked()
        print("THE END")
