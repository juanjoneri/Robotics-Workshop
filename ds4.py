import pygame
import RPi.GPIO as GPIO

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# Class to output to the scren
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

# pygame rubbish
pygame.init()
size = [360, 120]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adrometeo I")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

# -------- WHERE THE MAGIC HAPPENS ----------- #
# ------------- MY FUNCTIONS ----------------- #
class GpioAccess:
    def __init__(self, motorL, motorR):
        self.motorL = motorL
        self.motorR = motorR

    def changeLPwm(self, pwm):
        self.motorL.ChangeDutyCycle(pwm)

    def changeRPwm(self, pwm):
        self.motorR.ChangeDutyCycle(pwm)

def configureGpio():
    right = 15 #Derecha   15 (->)
    left = 13  #Izquierda 13 (<-)
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

def kill():
    motorR.stop()
    motorL.stop()
    GPIO.cleanup()
    pygame.joystick.quit()
    pygame.quit()
    print('killing successful')

# ---------- FUNCTION EXCECUTION ------------- #
motorR, motorL = configureGpio()
gpioaccess = GpioAccess(motorL, motorR)
# --------------- MAIN LOOP ------------------ #
while done==False:
    
    # Check for exit |X|
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Redraw screen
    screen.fill(WHITE)
    textPrint.reset()

    #Joystick setup
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    name = joystick.get_name()
    textPrint.print(screen, name )

    # Axes
    textPrint.print(screen, "Axes" )
    textPrint.indent()

    axisL = -joystick.get_axis( 1 )   #  _0 : 1^
    axisR = joystick.get_axis( 2 )    # <-1 : 1>
    if axisL <= 0:
        axisL = 0
    
    textPrint.print(screen, "Axis L value: {:>6.3f}".format(axisL))
    textPrint.print(screen, "Axis R value: {:>6.3f}".format(axisR)) 
    textPrint.unindent()
    
    ##### CALCULATE AND CHANGE THE PWM OF THE MOTORS ---
    baseDuty = axisL * 15.0
    rightCycle = baseDuty
    leftCycle = baseDuty

    #axisRight > 0 when turning right and < 0 when turning left
    #RIGHT -> leftCycle  += (+)
    #      -> rightCycle -= (+)
    #
    #LEFT  -> leftCycle  += (-)
    #      -> rightCycle -= (-)
    leftCycle += (baseDuty*axisR)/2
    rightCycle -= (baseDuty*axisR)/2
        
    gpioaccess.changeLPwm(leftCycle)
    gpioaccess.changeRPwm(rightCycle)
    #### -----------------------------------------------
    
    # Buttons
    textPrint.print(screen, "Buttons" )
    textPrint.indent()
    
    button0 = joystick.get_button( 2 )
    textPrint.print(screen, "Button 0 value: {}".format(button0))
    textPrint.unindent()
    if button0 == 1:
        done = True

    # S'more pygame magic
    pygame.display.flip()
    clock.tick(20)

kill()
