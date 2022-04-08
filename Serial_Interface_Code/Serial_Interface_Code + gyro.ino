#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <Servo.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

Servo motFR;
Servo motBR;
Servo motBL;
Servo motFL;
Servo motR;
Servo motL;
Servo claw_rotate;
Servo claw_grab;

char header = 1;
char footer = 10;

void setup() {
  Serial.begin(9600);
  
  motFR.attach(A5, 1000, 2000);
  motBR.attach(A2, 1000, 2000);
  motBL.attach(A4, 1000, 2000);
  motFL.attach(A3, 1000, 2000);
  motR.attach(10,1000, 2000);
  motL.attach(5, 1000, 2000);
  claw_grab.attach(11,0,120);

  motFR.writeMicroseconds(1500);
  motBR.writeMicroseconds(1500);
  motBL.writeMicroseconds(1500);
  motFL.writeMicroseconds(1500);
  motR.writeMicroseconds(1500);
  motL.writeMicroseconds(1500);

  delayMicroseconds(5000);
  while (!Serial);
}

void loop() {
  if(Serial.available() >= 1){
    //byte header = Serial.parseInt();
    //if (header == 1){
    int val = Serial.parseInt();
      int motor = val / 1000;
      int m = val % 1000;
      if (m == 0){
        m = 1500;
      }
      else if (m < 0 || m > 127){ 
        if (m > 127) { m -= 0xFF; }
        m = map(m, -127, -1, 1000, 1499);
      }
      else if (m > 0){
        m = map(m, 1, 127, 1501, 2000);
      }
      Serial.println(m);
      if (motor == 2){
        Serial.print("Motor FR");
        motFR.writeMicroseconds(m);
      } 
      else if (motor == 3){
        Serial.print("Motor FL");
        motFL.writeMicroseconds(m);
      } 
      else if (motor == 4){
        Serial.print("Motor BR");
        motBR.writeMicroseconds(m);
      } 
      else if (motor == 5){
        Serial.print("Motor BL");
        motBL.writeMicroseconds(m);
      } 
      else if (motor == 6){
        Serial.print("Motor R");
        motR.writeMicroseconds(m);
      } 
      else if (motor == 7){
        Serial.print("Motor L");
        motL.writeMicroseconds(m);
      }
      else if (motor==9){
        claw_grab.write(m);
      }
      else if (motor == 14){
          motFR.writeMicroseconds(1500);
          motFL.writeMicroseconds(1500);
          motBR.writeMicroseconds(1500);
          motBL.writeMicroseconds(1500);
          motR.writeMicroseconds(1500);
          motL.writeMicroseconds(1500);
          claw_grab.write(9000);
        
      }
      else if (motor == 13){
        if (m == 127){
          Serial.print("Top Motor Down");
          motFR.writeMicroseconds(1700);
          motFL.writeMicroseconds(1700);
          motBR.writeMicroseconds(1700);
          motBL.writeMicroseconds(1700);
        }
        else if (m == 254){
          Serial.print("Top Motor Up");
          motFR.writeMicroseconds(1300);
          motFL.writeMicroseconds(1300);
          motBR.writeMicroseconds(1300);
          motBL.writeMicroseconds(1300);
        }
      }
  }
}

