class Packet:
    min = 0
    max = 512

    def __init__(self, car_id, command, value):
        self.car_id = car_id
        self.command = command
        self.value = value

    def inflate(self):
        return round(self.value * (Packet.max - Packet.min) + Packet.min)

    def __str__(self):
        return self.car_id + self.command + str(self.inflate()).zfill(3) + "!"


class PacketSpeed(Packet):
    command = '1'

    def __init__(self, car_id, value):
        super(PacketSpeed, self).__init__(car_id, PacketSpeed.command, value)


class PacketSteer(Packet):
    command = '2'

    def __init__(self, car_id, value):
        super(PacketSteer, self).__init__(car_id, PacketSteer.command, value)
