import pygame
import serial
import numpy as np

smartElex = serial.Serial(port='COM8', timeout=0)
smartElex.baudrate = 9600 # set Baud rate to 9600
smartElex.bytesize = 8    # Number of data bits = 8
smartElex.parity   ='N'    # No parity
smartElex.stopbits = 1     # Number of Stop bits = 1

# Define some colors.
BLACK = pygame.Color('white')
WHITE = pygame.Color('black')


#data = bytes(b'\0x2A\(1<<3)|(0<<2)\xFF\xFF\0x23')
forward = bytes([0x2A, (1<<3)|(0<<2), 0xFF, 0xFF, 0x23])
back = bytes([0x2A, (1<<3)|(1<<2), 0xFF, 0xFF, 0x23])
stop = bytes([0x2A, (0<<3)|(1<<2), 0x00, 0xFF, 0x23])

class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

screen = pygame.display.set_mode((300, 400))

#pygame.display.set_caption("My Game")

done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")


    screen.fill(WHITE)
    textPrint.reset()

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:

            jid = joystick.get_id()

        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))
        textPrint.tprint(screen, "")


        axes = joystick.get_numaxes()
        textPrint.indent()


        axis0 = joystick.get_axis(0)
        textPrint.tprint(screen, "Axis 1: {: .1f}".format(axis0))

        axis1 = joystick.get_axis(1)
        textPrint.tprint(screen, "Axis 2: {: .1f}".format(axis1))

        axis2 = joystick.get_axis(2)
        textPrint.tprint(screen, "Axis 3 Motion: {: .1f}".format(axis2))


        axis3 = joystick.get_axis(3)
        textPrint.tprint(screen, "Axis 4 Steer: {: .1f}".format(axis3))

        if 0.1< axis3:   smartElex.write(forward), print(forward)

        if -0.1> axis3:   smartElex.write(back), print(back)
        else :   smartElex.write(stop)

        textPrint.tprint(screen, "")

        axis4 = joystick.get_axis(4)
        textPrint.tprint(screen, "Axis L2: {: .1f}".format(axis4))

        axis5 = joystick.get_axis(5)
        textPrint.tprint(screen, "Axis R2: {: .1f}".format(axis5))


        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "")



        button0 = joystick.get_button(0)
        textPrint.tprint(screen,"Button A : {}".format(button0))


        button1 = joystick.get_button(1)
        textPrint.tprint(screen,"Button B : {}".format(button1))

        button2 = joystick.get_button(2)
        textPrint.tprint(screen,"Button X : {}".format(button2))

        button3 = joystick.get_button(3)
        textPrint.tprint(screen,"Button Y : {}".format(button3))
        textPrint.tprint(screen, "")

        button4 = joystick.get_button(4)
        textPrint.tprint(screen,"Button L1 : {}".format(button4))

        button5 = joystick.get_button(5)
        textPrint.tprint(screen,"Button R1 : {}".format(button5))
        textPrint.tprint(screen, "")

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))



        hatx = joystick.get_hat(0)
        textPrint.tprint(screen, "Hat value: {}".format(hatx))

        textPrint.unindent()



        textPrint.unindent()


    pygame.display.flip()


    clock.tick(20)


pygame.quit()
