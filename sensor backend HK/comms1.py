import serial
from threading import Thread

class Communications:
    def __init__(self, port,baud_rate):
        self.ser = serial.Serial(port, baud_rate)
        self.start_thread()

    def start_thread(self):
        self.connection = threading.Thread(self.read)
        self.connection.start()

    def read(self):
        while(True):
            cache = ""
            while(self.ser.in.waiting > 0):
                cache.append(self.ser.read().decode("latin"))
            messages = cache.split(chr(9))
            for m in messages:
                if len(m) == 4:
                    continue
                
            
