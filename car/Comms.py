import threading, time, serial

class SerialComms(threading.Thread):
    def __init__(self, port, baud, delay):
        threading.Thread.__init__(self)
        self.ser = serial.Serial()
        self.port = port
        self.baud = baud
        self.message = ''
        self.delay = delay
        self.active = False

    def open(self):
        self.ser.baudrate = self.baud
        self.ser.port = self.port
        self.ser.open()

    def close(self):
        self.ser.close()

    def set_message(self, arg):
        self.message = arg

    def set_active(self, arg):
        self.active = arg

    def send(self):
        self.ser.write(str.encode(self.message))

    def send(self, arg):
        self.ser.write(str.encode(arg))

    def run(self):
        while self.active:
            self.send(self.message)
            time.sleep(self.delay)