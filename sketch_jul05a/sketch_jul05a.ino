#include <Servo.h>
int leftWhisker = 5;
int rightWhisker = 7;
Servo servoLeft;
Servo servoRight; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  servoLeft.attach(13);                     
  servoRight.attach(12);                     
  servoLeft.writeMicroseconds(1500);        
  servoRight.writeMicroseconds(1500);
}
   
void loop() {
  int left_value = digitalRead(leftWhisker);
  int right_value = digitalRead(rightWhisker);
  // put your main code here, to run repeatedly:
 /* straight();
  delay(500);*/
  
  if (rightWhisker == 0 && leftWhisker == 0) {
    Serial.println("both");
    back();
    delay(1500);
    spin_left;
    delay(500);
    spin_right();
    delay(500);
    straight();
  }
  
  else if (leftWhisker == 0) {
    Serial.println("left");
    back();
    delay(1500);
    spin_right();
    delay(500);
    straight();
  }
  
  else if (rightWhisker == 0) {
    Serial.println("right");
    back();
    delay(1500);
    spin_left();
    delay(500);
    straight();
  }
  delay(500);

}

void straight()
{
  servoLeft.writeMicroseconds(1300);        
  servoRight.writeMicroseconds(1700);            
}
    
void spin_left()
{
  servoLeft.writeMicroseconds(1000);        
  servoRight.writeMicroseconds(900);
}

void spin_right()
{
  servoLeft.writeMicroseconds(900);        
  servoRight.writeMicroseconds(100);
}

void back()
{
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1300);
}
