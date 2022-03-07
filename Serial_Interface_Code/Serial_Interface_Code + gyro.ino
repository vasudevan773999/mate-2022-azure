

import serial
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <Servo.h>
char header = 1
char footer = 10

  
Servo mythruster_FR;
Servo mythruster_BR;
Servo mythruster_BL;
Servo mythruster_FL;
Servo mythruster_R;
Servo mythruster_L;
Servo myservo_rotate;
Servo myservo_grab;  


void printEvent(sensors_event_t* event) {
  double x = -1000000, y = -1000000 , z = -1000000; 
  else if (event->type == SENSOR_TYPE_ORIENTATION) {
    Serial.print("Orient:");
    x = event->orientation.x;
    y = event->orientation.y;
    z = event->orientation.z;
  }
  else if (event->type == SENSOR_TYPE_ROTATION_VECTOR) {
    Serial.print("Rot:");
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
  }
  else if (event->type == SENSOR_TYPE_LINEAR_ACCELERATION) {
    Serial.print("Linear:");
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
  }
  else {
    Serial.print("Unk:");
  }

  Serial.print("\tx= ");
  Serial.print(x);
  Serial.print(" |\ty= ");
  Serial.print(y);
  Serial.print(" |\tz= ");
  Serial.println(z);
}



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
  sensors_event_t orientationData , angVelocityData , linearAccelData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);

  Serial.write(&orientationData);
  Serial.write(&angVelocityData);
  Serial.write(&linearAccelData);


    if (Serial.available>=4){
      byte packetheader = Serial.read();
      if (packetheader==header){
        byte motor = Serial.read();
        int8_t speed = Serial.read();
        int motor_speed = (int) (1500 + speed * (500 / 127));
        byte motor_servo = serial.read();
        int8_t servo_speed = Serial.read();
        int servo_speed_convert = (int)((servo_speed * 0.73)-255);
        
        if (incomingByte[2] == 2){
          mythruster_FR.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 3){
            mythruster_FL.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 4){
            mythruster_BR.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 5){
            mythruster_BL.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 6){
            mythruster_R.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 7){
            mythruster_L.writeMicroseconds(motor_speed);
        } else if (incomingByte[2] == 8){
            myservo_rotate.writeMicroseconds(servo_speed_convert);
            if (incomingByte[3] == 12){
              myservo_rotate.writeMicroseconds(180)
            } else if (incomingByte[3] == 11){
              myservo_rotate.writeMicroseconds(0)
              }
        } else if (incomingByte[2] == 9){            
          myservo_grab.writeMicroseconds(servo_speed_convert);
            if (incomingByte[3] == 12){
              myservo_rotate.writeMicroseconds(180)
            } else if (incomingByte[3] == 11){
              myservo_rotate.writeMicroseconds(0)
              }
        }
          
              
        } 
        }
      
      
      }
    }


   reportIMUData();
}

void reportIMUData() {
    sensors_event_t orientation , gyro , accel;
    bno.getEvent(&orientation, Adafruit_BNO055::VECTOR_EULER);
    bno.getEvent(&gyro, Adafruit_BNO055::VECTOR_GYROSCOPE);
    bno.getEvent(&accel, Adafruit_BNO055::VECTOR_LINEARACCEL);
  
    Serial.write(gyro->orientation.x);
    Serial.write(gyro->orientation.y);
    Serial.write(gyro->orientation.z);
    Serial.write(gyro->gyro.x);
    Serial.write(gyro->gyro.y);
    Serial.write(gyro->gyro.z);
    Serial.write(gyro->accel.x);
    Serial.write(gyro->accel.y);
    Serial.write(gyro->accel.z);
  
}

