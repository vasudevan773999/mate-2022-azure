
#include <Servo.h>
Servo myservo;

int thruster_Speed = 1500;

void setup() {

  myservo.attach(9);
  myservo.writeMicroseconds(1500);
  delay(200);
  Serial.begin(9600);
 
}

void loop() {

  Serial.print("Enter thruster speed: ");
  int temp = Serial.parseInt();
  if (temp != 0) thruster_Speed = temp;
  //changing the fan speed
  Serial.print("thruster_speed = ");
  Serial.println(thruster_Speed);
  myservo.writeMicroseconds(thruster_Speed);
  Serial.write(9600);
  Serial.available();

}
