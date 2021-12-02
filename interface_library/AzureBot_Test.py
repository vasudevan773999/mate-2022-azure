

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
            leftJoy_LR = packetControls.packet[0] #and repeat... will finalize once I know what values will come
            leftJoy_UD = packetControl.packet[1]
            rightJoy_LR = packetControls.packet[2]
            rightJoy_UD = packetControls.packet[3]

            
            while True:
                
                #coding the Left thruster
                
                if leftJoy_LR < [43,43]
                    packet_leftJoy_stopped = chr(1) + chr(7) + chr((leftJoy_LR = 0).encode("latin")) + chr(8)
                    self.ser.write(packet_leftJoy_stopped)
                else:
                    packet_leftJoy = chr(1) + chr(7) + chr((leftJoy_LR).encode("latin")) + chr(8) 
                    self.ser.write(packet_leftJoy)

                #coding the Right thruster
                if rightJoy_LR < [43,43]
                    packet_rightJoy_stopped = chr(1) + chr(6) + chr((rightJoy_LR=0).encode("latin")) + chr(8)
                    self.ser.write(packet_rightJoy_stopped)
                else:
                    packet_rightJoy = chr(1) + chr(6) + chr((rightJoy_LR).encode("latin")) + chr(8) 
                    self.ser.write(packet_rightJoy)

                    



                #create serial connection computer and mc
                #read data
                #test and figure out what each byte means
                #take data, convert it, and send to systems
                #[-127,127]

    def start_thread(self):
        start_thread = Thread(target = self.run)  
        start_thread.start()
        



