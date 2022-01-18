void setup() {
  // put your setup code here, to run once:
  
}

void loop() {
  // put your main code here, to run repeatedly:  

  int8_t m = Serial.read();

  if (m == 0){
    m = 1500;
  }
  else if (m < 0){ //[-127,0) / [1000,1500)
    m = map(m, -127, -1, 1000, 1499);
  }
  else if (m > 0){ //(0,127] / (1500,2000]
    m = map(m, 1, 127, 1501, 2000);
  }

}
