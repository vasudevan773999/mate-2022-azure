

#include <Servo.h>
int thruster_Speed_FR = 1500;
int thruster_Speed_BR = 1500;
int thruster_Speed_BL = 1500;
int thruster_Speed_FL = 1500;
int thruster_Speed_R = 1500;
int thruster_Speed_L = 1500;

Servo mythruster_FR;
Servo mythruster_BR;
Servo mythruster_BL;
Servo mythruster_FL;
Servo mythruster_R;
Servo mythruster_L;

void setup() {
  mythruster_FR.attach(7,1000,2000);
  mythruster_FR.writeMicroseconds(1500);
  
  mythruster_BR.attach(7,1000,2000);
  mythruster_BR.writeMicroseconds(1500);
  
  mythruster_BL.attach(7,1000,2000);
  mythruster_BL.writeMicroseconds(1500);
  
  mythruster_FL.attach(7,1000,2000);
  mythruster_FL.writeMicroseconds(1500);
  
  mythruster_R.attach(7,1000,2000);
  mythruster_R.writeMicroseconds(1500);
  
  mythruster_L.attach(7,1000,2000);
  mythruster_L.writeMicroseconds(1500);
  
  delay(200);
  Serial.begin(9600);
}

void loop() {

   if (Serial.available()); {
      int motor_speed = incomingByte[2];
      String incomingByte = Serial.read(); 
    }
    
  
    if (incomingByte[1] == char(2){
       mythruster_L.writeMicroseconds(1800);
    } else if (incomingByte[1] == char(3){
      mythruster_setup();
    } else if (incomingByte[1] == char(4){
      mythruster_setup();
    } else if (incomingByte[1] == char(5){
      mythruster_setup();
    } else if (incomingByte[1] == char(6){
      mythruster_setup();
    } else if (incomingByte[1] == char(7){
      mythruster_setup();
    }


        if (incomingByte[2] == char(2){
      mythruster_setup();
    } else if (incomingByte[2] == char(3){
      mythruster_setup();
    } else if (incomingByte[2] == char(4){
      mythruster_setup();
    } else if (incomingByte[2] == char(5){
      mythruster_setup();
    } else if (incomingByte[2] == char(6){
      mythruster_setup();
    } else if (incomingByte[2] == char(7){
      mythruster_setup();
    }
      
}

void mythruster_setup() {
  Serial.print("Enter thruster speed: ");
  int temp = Serial.parseInt();
  if (temp != 0) thruster_Speed = temp;
  //changing the fan speed
  Serial.print("thruster_speed = ");
  Serial.println(thruster_Speed);
  mythruster.writeMicroseconds(thruster_Speed);
  Serial.write(9600);
  delay(300);
}
  
  

 
