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
  straight();
  delay(250);
  Serial.print("A3 = ");                     // Display "A3 = "
  Serial.print(volts(A3));                    // Display measured A3 volts
  Serial.println(" volts");                  // Display " volts" & newline
  delay(1000);     
  if (right_value == 0 && left_value == 0) {
    Serial.println("both");
    back();
    delay(1000);
    spin_left;
    delay(1000);
    spin_right();
    delay(1000);
    straight();
  }
  
  else if (left_value == 0) {
    Serial.println("left");
    back();
    delay(1000);
    spin_right();
    delay(1000);
    straight();
  }
  
  else if (right_value == 0) {
    Serial.println("right");
    back();
    delay(1000);
    spin_left();
    delay(1000);
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
  servoLeft.writeMicroseconds(1300);         
  servoRight.writeMicroseconds(1300);
}

void spin_right()
{
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1700);
}

void back()
{
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1300);
}

float volts(int adPin)                       // Measures volts at adPin
{                                            // Returns floating point voltage
 return float(analogRead(adPin)) * 5.0 / 1024.0;
}    
