

from threading import Thread
import serial
import controls

class Comms:
    def __init__(self, port: int, baud_rate: int):
        self.port = port
        self.baud_rate = baud_rate
        ser = serial.Serial(self.port, self,baud_rate)
        self.ser.close()
        self.ser.open()


    def run(self):
        while True: 
            packetControls = controls.Controls() #change later
            
            
            packetControls.split(chr())
            left_bumper = packetControls[1] #and repeat... will finalize once I know what values will come
            

    def start_thread(self):
        start_thread = Thread(target = self.run)  
        start_thread.start()
        

