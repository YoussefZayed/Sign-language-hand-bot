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


int positions[26][5] = {
  {0, 0, 0, 0, 0},  // a
  {0, 0, 0, 0, 0},  // b
  {0, 0, 0, 0, 0},  // c
  {0, 0, 0, 0, 0},  // d
  {0, 0, 0, 0, 0},  // e
  {0, 0, 0, 0, 0},  // f
  {0, 0, 0, 0, 0},  // g
  {0, 0, 0, 0, 0},  // h
  {0, 0, 0, 0, 0},  // i
  {0, 0, 0, 0, 0},  // j
  {0, 0, 0, 0, 0},  // k
  {0, 0, 0, 0, 0},  // l
  {0, 0, 0, 0, 0},  // m
  {0, 0, 0, 0, 0},  // n
  {0, 0, 0, 0, 0},  // o
  {0, 0, 0, 0, 0},  // p
  {0, 0, 0, 0, 0},  // q
  {0, 0, 0, 0, 0},  // r
  {0, 0, 0, 0, 0},  // s
  {0, 0, 0, 0, 0},  // t
  {0, 0, 0, 0, 0},  // u
  {0, 0, 0, 0, 0},  // v
  {0, 0, 0, 0, 0},  // w
  {0, 0, 0, 0, 0},  // x
  {0, 0, 0, 0, 0},  // y
  {0, 0, 0, 0, 0}   // z
};


void setup() {
  Serial.begin(115200);
  finger1.attach(finger1_pin);
  finger2.attach(finger2_pin);
//  finger3.attach(finger3_pin);
//  finger4.attach(finger4_pin);
//  finger5.attach(finger5_pin);

  finger1.write(0);
  finger2.write(0);
  finger3.write(0);
  finger4.write(0);
  finger5.write(0);
}

void move_fingers(char letter) {
  int i = letter-'0';
  
  finger1.write(positions[i][0]);
  finger2.write(positions[i][1]);
  finger3.write(positions[i][2]);
  finger4.write(positions[i][3]);
  finger5.write(positions[i][4]);
}

void loop() {
  
  if (Serial.available() > 0) {
    char letter = Serial.read();
    Serial.println(letter);
    // move_fingers(letter);
    finger1.write(90);
    delay(100);
  }
}
