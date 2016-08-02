import pygame

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

# pygame rubish
pygame.init()
size = [360, 120]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adrometeo")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

# -------- WHERE THE MAGIC HAPPENS ----------- #
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # DRAWING STEP
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

    axisL = joystick.get_axis( 1 )
    axisR = joystick.get_axis( 2 )
    textPrint.print(screen, "Axis L value: {:>6.3f}".format(axisL))
    textPrint.print(screen, "Axis R value: {:>6.3f}".format(axisR)) 
    textPrint.unindent()

    # Buttons
    textPrint.print(screen, "Buttons" )
    textPrint.indent()
    
    button0 = joystick.get_button( 2 )
    textPrint.print(screen, "Button 0 value: {}".format(button0))
    textPrint.unindent()

    # S'more pygame magic
    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
