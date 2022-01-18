

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



    def send_value(self,value):
        #preq: -100<=value<=100
        value = round(value*1.27)
        if value<0:
            value = 255+value
        return value 


    def run(self):
        while True: 
            packetControls = controls.Controls() #change later
            leftJoy_LR = packetControls.packet[0] #and repeat... will finalize once I know what values will come
            leftJoy_UD = packetControl.packet[1]
            rightJoy_LR = packetControls.packet[2]
            rightJoy_UD = packetControls.packet[3]
            clawButton = packetControls.packet[4]

            
            while True:
                
                #coding the Left thruster (sendSystemsLes)
                
                if leftJoy_LR < [43,43]:
                    value = send_value(leftJoy_LR)
                    packet_leftJoy_stopped = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(10)
                    self.ser.write(packet_leftJoy_stopped)
                else:
                    value = send_value(leftJoy_LR)
                    packet_leftJoy = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(10) 
                    self.ser.write(packet_leftJoy)


                #coding the Right thruster
                if rightJoy_LR < [43,43]:
                    value = send_value(rightJoy_LR)
                    packet_rightJoy_stopped = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(10)
                    self.ser.write(packet_rightJoy_stopped)
                else:
                    packet_rightJoy = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(10) 
                    self.ser.write(packet_rightJoy)

                #servo claw code - to be finalized
                if clawButton == True:
                    packet_servo = chr(1) + chr(7) + chr() + chr(10)
                    self.ser.write(packet_servo)

                else:
                    if clawButton == False
                    packet_servo = chr(1) + chr(7) + #add info


                #create serial connection computer and mc
                #read data
                #test and figure out what each byte means
                #take data, convert it, and send to systems
                #[-127,127]

    def start_thread(self):
        start_thread = Thread(target = self.run)  
        start_thread.start()
        
