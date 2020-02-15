#include <Servo.h>

Servo finger1;
Servo finger2;
Servo finger3;
Servo finger4;
Servo finger5;

const int finger1_pin = 4;
const int finger2_pin = 5;
const int finger3_pin = 6;
const int finger4_pin = 7;
const int finger5_pin = 8;

void setup() {
  Serial.begin(115200);
  finger1.attach(finger1_pin);
  finger2.attach(finger2_pin);
  finger3.attach(finger3_pin);
  finger4.attach(finger4_pin);
  finger5.attach(finger5_pin);
}

void loop() {
  if (Serial.available() > 0) {
    char data[5];
    Serial.readBytes(data, 4);
    data[4] = '\0';
    Serial.print(data);
    delay(500);
  }
}
