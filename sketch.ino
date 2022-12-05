#include<Servo.h>
int i;
Servo servo;
void setup() {
  servo.attach(8);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() > 0){
  i = Serial.readString().toInt();
  servo.write(i);
  Serial.println(i);
  delay(500);
  servo.write(0);
  }
}
