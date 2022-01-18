



#include <Servo.h>
char header = 1
char FR = 2
char FL = 3
char BR = 4
char BL = 5
char Right = 6
char Left = 7
char Servo_rotate = 8
char Servo_grab = 9
char footer = 10
int motorused
Servo mythruster_FR;
Servo mythruster_BR;
Servo mythruster_BL;
Servo mythruster_FL;
Servo mythruster_R;
Servo mythruster_L;
Servo myservo_rotate;
Servo myservo_grab;  


void setup() {
  myservo_rotate.attach(13);
  myservo_grab.attach(14);
  
  mythruster_FR.attach(7,1000,2000);
  mythruster_FR.writeMicroseconds(1500);
  
  mythruster_BR.attach(8,1000,2000);
  mythruster_BR.writeMicroseconds(1500);
  
  mythruster_BL.attach(9,1000,2000);
  mythruster_BL.writeMicroseconds(1500);
  
  mythruster_FL.attach(10,1000,2000);
  mythruster_FL.writeMicroseconds(1500);
  
  mythruster_R.attach(11,1000,2000);
  mythruster_R.writeMicroseconds(1500);
  
  mythruster_L.attach(12,1000,2000);
  mythruster_L.writeMicroseconds(1500);
  
  delay(200);
  Serial.begin(9600);
}

void loop() {


   if (Serial.available==4); {
      byte packetheader = Serial.read();
   if (packetheader==header);
      byte motor = Serial.read();
  
      motor = incomingByte[2];
      int incomingByte = Serial.parseInt(); 
    }
    
  
    if (incomingByte[1] == 2){
       mythruster_FR.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 3){
      mythruster_FL.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 4){
      mythruster_BR.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 5){
      mythruster_BL.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 6){
      mythruster_R.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 7){
      mythruster_L.writeMicroseconds(motor_speed);
    } else if (incomingByte[1] == 8){
      myservo_rotate.write(motor_speed);
    } else if (incomingByte[1] == 9){
      myservo_grab.write(motor_speed);
    }



      
}
               
/*void mythruster_setup() {
  mythruster_BL.writeMicroseconds((int (incomingByte[2])/255)*500+1500));
}
  
  
