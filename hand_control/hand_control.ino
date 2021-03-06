#include <Servo.h>

Servo servos[5] = {
  Servo(),
  Servo(),
  Servo(),
  Servo(),
  Servo()
};

int positions[28][5] = {
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
  {0, 0, 0, 0, 0},  // z
  {0, 0, 0, 0, 0},  // nothing
  {0, 0, 0, 0, 0}   // space
};

int sequences[28][5] = {
  {0,1,2,3,4},  // a
  {0,1,2,3,4},  // b
  {0,1,2,3,4},  // c
  {0,1,2,3,4},  // d
  {0,1,2,3,4},  // e
  {0,1,2,3,4},  // f
  {0,1,2,3,4},  // g
  {0,1,2,3,4},  // h
  {0,1,2,3,4},  // i
  {0,1,2,3,4},  // j
  {0,1,2,3,4},  // k
  {0,1,2,3,4},  // l
  {0,1,2,3,4},  // m
  {0,1,2,3,4},  // n
  {0,1,2,3,4},  // o
  {0,1,2,3,4},  // p
  {0,1,2,3,4},  // q
  {0,1,2,3,4},  // r
  {0,1,2,3,4},  // s
  {0,1,2,3,4},  // t
  {0,1,2,3,4},  // u
  {0,1,2,3,4},  // v
  {0,1,2,3,4},  // w
  {0,1,2,3,4},  // x
  {0,1,2,3,4},  // y
  {0,1,2,3,4},  // z
  {0,1,2,3,4},  // nothing
  {0,1,2,3,4}   // space
};

void move_fingers(char letter) {
  int i = letter - 'A';
  for (int j = 0; i < 5; ++j)
    servos[sequences[i][j]].write(positions[i][sequences[i][j]]);
}

void setup() {
  Serial.begin(115200);

  servos[0].attach(4);
  servos[1].attach(5);
  servos[2].attach(6);
  servos[3].attach(7);
  servos[4].attach(8);

  for (int i = 0; i < 5; ++i)
    servos[i].write(0);
}

void loop() {  
  if (Serial.available() > 0) {
    char letter = Serial.read();
    Serial.println(letter);
    move_fingers(letter);
    delay(100);
  }
}
