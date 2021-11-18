

from threading import Thread
import serial

class Comms:
    def __init__(self, port: int, baud_rate: int):
        self.port = port
        self.baud_rate = baud_rate
        ser = serial.Serial(self.port, self,baud_rate)
        self.ser.close()
        self.ser.open()


    def run(self):
        while True: 
            packetControls =  self.ser.read() #the output from the controls will be an array of values
            left_bumper = packetControls[0] #and repeat... will finalize once I know what values will come




    def start_thread(self):
        start_thread = Thread(target = self.run)  
        start_thread.start()



