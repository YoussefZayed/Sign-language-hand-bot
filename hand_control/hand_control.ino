#include <AccelStepper.h>

#define FULLSTEP 4

const int stepsPerRev = 2048;

AccelStepper steppers[5] = {
  AccelStepper(FULLSTEP, 8, 10, 9, 11),
  AccelStepper(FULLSTEP, 8, 10, 9, 11),
  AccelStepper(FULLSTEP, 8, 10, 9, 11),
  AccelStepper(FULLSTEP, 8, 10, 9, 11),
  AccelStepper(FULLSTEP, 8, 10, 9, 11)
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
  for (int i = 0; i < 5; ++i) {
    steppers[sequence[i]].moveTo(positions[i][sequence[i]]);
    steppers[sequence[i]].run();
  }
}

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 5; ++i) {
    steppers[i].setMaxSpeed(1000.0);
    steppers[i].setAcceleration(50.0);
    steppers[i].setSpeed(400);
  }
}

void loop() {  
//  if (Serial.available() > 0) {
//    char letter = Serial.read();
//    Serial.println(letter);
//    move_fingers(letter);
//    delay(100);
//  }
}
