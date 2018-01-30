import time
from Comms import SerialComms
from msvcrt import getch, kbhit
from Input import Keys
from Packet import PacketSpeed, PacketSteer

# Keyboard input parameters.
steer = 0.5
speed = 0.5
keyboard_delay = 0.01 # seconds

# Serial communication parameters.
car_id = 'Y'
port = 'COM1'
baud = 115200
send_delay = 0.1  # seconds

# Initialise the serial communication port.
comms = SerialComms(port, baud, send_delay)
comms.open()
comms.set_message(PacketSpeed(car_id, speed).__str__() +
                  PacketSteer(car_id, steer).__str__())
comms.set_active(True)
comms.start()

# Read input from the keyboard.
key = Keys.NULL
while key != Keys.ESCAPE:
    if kbhit():
        key = Keys(ord(getch()))
        if key == Keys.SPECIAL:
            key = Keys(ord(getch()))
            if key == Keys.ARROW_UP:
                speed += 0.05
                speed = speed if speed <= 1 else 1
            elif key == Keys.ARROW_DOWN:
                speed -= 0.05
                speed = speed if speed >= 0 else 0
            elif key == Keys.ARROW_RIGHT:
                steer += 0.05
                steer = steer if steer <= 1 else 1
            elif key == Keys.ARROW_LEFT:
                steer -= 0.05
                steer = steer if steer >= 0 else 0

            comms.set_message(PacketSpeed(car_id, speed).__str__() +
                              PacketSteer(car_id, steer).__str__())

    time.sleep(keyboard_delay)

# Free resources and exit.
comms.set_active(False)
print('Waiting for serial comms thread to join ...')
comms.join()
print('Done!')
comms.close()