
#include "Adafruit_VL53L1X.h"

#define IRQ_PIN 2
#define XSHUT_PIN 3
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


Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);

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
  void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println(F("Adafruit VL53L1X sensor demo"));

  Wire.begin();
  if (! vl53.begin(0x29, &Wire)) {
    Serial.print(F("Error on init of VL sensor: "));
    Serial.println(vl53.vl_status);
    while (1)       delay(10);
  }
  Serial.println(F("VL53L1X sensor OK!"));

  Serial.print(F("Sensor ID: 0x"));
  Serial.println(vl53.sensorID(), HEX);

  if (! vl53.startRanging()) {
    Serial.print(F("Couldn't start ranging: "));
    Serial.println(vl53.vl_status);
    while (1)       delay(10);
  }
  Serial.println(F("Ranging started"));

  // Valid timing budgets: 15, 20, 33, 50, 100, 200 and 500ms!
  vl53.setTimingBudget(50);
  Serial.print(F("Timing budget (ms): "));
  Serial.println(vl53.getTimingBudget());
}

void loop() {
  sensors_event_t orientationData , angVelocityData , linearAccelData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);

  Serial.write(&orientationData);
  Serial.write(&angVelocityData);
  Serial.write(&linearAccelData);
  
  if (vl53.dataReady()) {
    // new measurement for the taking!
    distance = vl53.distance();
    if (distance == -1) {
      // something went wrong!
      Serial.print(F("Couldn't get distance: "));
      Serial.println(vl53.vl_status);
      return;
    }
    Serial.print(F("Distance: "));
    Serial.print(distance);
    Serial.println(" mm");

    // data is read out, time for another reading!
    vl53.clearInterrupt();

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
        } else if (incomingByte[2] == 9){
            myservo_grab.writeMicroseconds(servo_speed_convert);
        } else if ( incomingByte[2] == 10){
            myservo_rotate.writeMicroseconds(1500);
            myservo_grab.writeMicroseconds(1500);
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

