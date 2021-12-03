


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
Servo myservo_rotate;
Servo myservo_grab;  

void setup() {
  myservo_rotate.attach(9);
  myservo_grab.attach(9);
  
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
       mythruster_FR.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(3){
      mythruster_FL.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(4){
      mythruster_BR.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(5){
      mythruster_BL.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(6){
      mythruster_R.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(7){
      mythruster_L.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(8)){
      myservo_rotate.write((int (incomingByte[2])/255)*500+1500));
    } else if (incomingByte[1] == char(8)){
      myservo_grab.write((int (incomingByte[2])/255)*500+1500));
    }



      
}

/*void mythruster_setup() {
  mythruster_BL.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
}
  
  

 
