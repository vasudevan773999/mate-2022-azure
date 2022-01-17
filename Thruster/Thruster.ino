#include <Servo.h>


Servo myservo_rotate;
Servo myservo_grab; 

int thruster_Speed = 1500;
Servo mythruster_FR;
Servo mythruster_BR;
Servo mythruster_BL;
Servo mythruster_FL;
Servo mythruster_R;
Servo mythruster_L;
int pos = 0;
void setup() {
  mythruster_FR.attach(1);
  mythruster_BR.attach(2);
  mythruster_BL.attach(3);
  mythruster_FL.attach(4);
  mythruster_R.attach(5);
  mythruster_L.attach(6);
  myservo_rotate.attach(7); 
  myservo_grab.attach(8);// attaches the servo on pin 9 to the servo object
  mythruster_FR.writeMicroseconds(1500);
  mythruster_BR.writeMicroseconds(1500);
  mythruster_FL.writeMicroseconds(1500);
  mythruster_BL.writeMicroseconds(1500);
  mythruster_R.writeMicroseconds(1500);
  mythruster_L.writeMicroseconds(1500);
  delay(200);
  Serial.begin(9600);

 
}

void loop() {
  myservo_grab.write(0);              // tell servo to go to position in variable 'pos'
  myservo_rotate.write(0);     

  Serial.print("Enter thruster speed: ");
  int temp = Serial.parseInt();
  if (temp != 0) thruster_Speed = temp;
  //changing the fan speed
  Serial.print("thruster_speed = ");
  Serial.println(thruster_Speed);
  mythruster_FR.writeMicroseconds(thruster_Speed);
  mythruster_BR.writeMicroseconds(thruster_Speed);
  mythruster_BL.writeMicroseconds(thruster_Speed);
  mythruster_FL.writeMicroseconds(thruster_Speed);
  mythruster_R.writeMicroseconds(thruster_Speed);
  mythruster_L.writeMicroseconds(thruster_Speed);
  Serial.write(9600);
  Serial.available();
  myservo_rotate.write(45);  
  myservo_grab.write(45);// tell servo to go to position in variable 'pos'
  delay(300);
 
}
