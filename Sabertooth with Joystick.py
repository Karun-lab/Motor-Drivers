import pygame
import serial


sabertooth = serial.Serial(port='COM8', timeout=0)
sabertooth.baudrate = 9600 # set Baud rate to 9600
sabertooth.bytesize = 8     # Number of data bits = 8
sabertooth.parity   ='N'    # No parity
sabertooth.stopbits = 1     # Number of Stop bits = 1

# Define some colors.
BLACK = pygame.Color('white')
WHITE = pygame.Color('black')


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
        if 0.1< axis2 <0.25:    sabertooth.write(b"\x30"), sabertooth.write(b"\xB0")  # M1 48 M2 176 25% speed clock wise
        elif 0.25< axis2 <0.5:  sabertooth.write(b"\x20"), sabertooth.write(b"\xA0")  # M1 32 M2 160 50% speed clock wise
        elif 0.5< axis2 <0.75:  sabertooth.write(b"\x10"), sabertooth.write(b"\x90")  # M1 16 M2 144 75%  speed  clock wise
        elif 0.75< axis2 <1:    sabertooth.write(b"\x01"), sabertooth.write(b"\x80")  # M1 1  M2 128 100%  speed  clock wise

        if -0.1> axis2 >-0.25:   sabertooth.write(b"\x50"), sabertooth.write(b"\xD0")  # M1 80  M2 208 25% speed anticlock wise
        elif -0.25> axis2 >-0.5: sabertooth.write(b"\x60"), sabertooth.write(b"\xE0")  # M1 96  M2 224 50% speed  anticlock wise
        elif -0.5> axis2 >-0.75: sabertooth.write(b"\x70"), sabertooth.write(b"\xF0")  # M1 112 M2 240 75% speed  anticlock wise
        elif -0.75> axis2 >-1:   sabertooth.write(b"\x7F"), sabertooth.write(b"\xFF")  # M1 127 M2 255 100% speed  anticlock wise

        elif axis2 == 0.0:       sabertooth.write(b"\x40"),sabertooth.write(b"\xc0")   # M1 64 M2 192 Stop all motors


        axis3 = joystick.get_axis(3)
        textPrint.tprint(screen, "Axis 4 Steer: {: .1f}".format(axis3))


        if 0.1< axis3 <0.25:    sabertooth.write(b"\x50"), sabertooth.write(b"\xB0")  # M1 80  M2 176 25% speed anticlock wise
        elif 0.25< axis3 <0.5:  sabertooth.write(b"\x60"), sabertooth.write(b"\xA0")  # M1 96  M2 160 50% speed  anticlock wise
        elif 0.5< axis3 <0.75:  sabertooth.write(b"\x70"), sabertooth.write(b"\x90")  # M1 112 M2 144 75% speed  anticlock wise
        elif 0.75< axis3 <1:    sabertooth.write(b"\x7F"), sabertooth.write(b"\x80")  # M1 127 M2 128 100% speed  anticlock wise

        if -0.1> axis3 >-0.25:   sabertooth.write(b"\x30"), sabertooth.write(b"\xD0")  # M1 48 M2 208 25% speed clock wise
        elif -0.25> axis3 >-0.5: sabertooth.write(b"\x20"), sabertooth.write(b"\xE0")  # M1 32 M2 224 50% speed clock wise
        elif -0.5> axis3 >-0.75: sabertooth.write(b"\x10"), sabertooth.write(b"\xF0")  # M1 16 M2 240 75%  speed  clock wise
        elif -0.75> axis3 >-1:   sabertooth.write(b"\x01"), sabertooth.write(b"\xFF")  # M1 1  M2 255 100%  speed  clock wise

        elif axis3 == 0.0:       sabertooth.write(b"\x40"),sabertooth.write(b"\xc0")   # M1 64 M2 192 Stop all motors

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
