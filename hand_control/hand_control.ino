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

const int max_pos;

int positions[28][5] = {
  {max_pos, max_pos, max_pos, max_pos, 0},  // a
  {0, 0, 0, 0, max_pos},  // b
  {0, 0, 0, 0, 0},  // c
  {max_pos, 0, max_pos, max_pos, max_pos},  // d
  {0, 0, 0, 0, 0},  // e
  {50, 0, 0, 0, 0},  // f
  {0, 0, max_pos, max_pos, max_pos},  // g
  {0, 0, 0, max_pos, max_pos},  // h
  {0, max_pos, max_pos, max_pos, max_pos},  // i
  {0, max_pos, max_pos, max_pos, 0},  // j
  {0, 0, 0, max_pos, max_pos},  // k
  {0, 0, max_pos, max_pos, max_pos},  // l
  {max_pos, max_pos, max_pos, max_pos, max_pos},  // m
  {max_pos, max_pos, max_pos, max_pos, max_pos},  // n
  {max_pos, max_pos, max_pos, max_pos, max_pos},  // o
  {0, 0, 0, max_pos, max_pos},  // p
  {0, 0, max_pos, max_pos, max_pos},  // q
  {170, 0, 0, max_pos, max_pos},  // r
  {max_pos, max_pos, max_pos, max_pos, max_pos},  // s
  {max_pos, max_pos, max_pos, max_pos, max_pos},  // t
  {max_pos, 0, 0, max_pos, max_pos},  // u
  {max_pos, 0, 0, max_pos, max_pos},  // v
  {max_pos, 0, 0, 0, max_pos},  // w
  {0, 0, max_pos, max_pos, max_pos},  // x
  {0, 0, 0, 0, 0},  // y
  {0, 0, 0, 0, 0},  // z
  {0, 0, 0, 0, 0},  // nothing
  {0, 0, 0, 0, 0}  // space
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
  int i = letter-'A';
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
    move_fingers(letter);
    delay(100);
  }
}
