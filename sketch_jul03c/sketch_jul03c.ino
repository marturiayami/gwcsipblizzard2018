#include <Servo.h>                           // Include servo library

int p1 = 13;
int p2 = 11;
int p3 = 9;
int p4 = 6;
Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int PIEZOPIN = 5;                            // Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
  // Attach LED pins here.
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  
}  
 
void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  dance();
  delay(1000);
  back();
  delay(1000);
}

void dance()
{
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1300);            
}
/*     
void spin_left()
{
  servoLeft.writeMicroseconds(1000);        
  servoRight.writeMicroseconds(900);
}

void spin_right()
{
  servoLeft.writeMicroseconds(900);        
  servoRight.writeMicroseconds(100);
}*/

void back()
{
  servoLeft.writeMicroseconds(-1700);        
  servoRight.writeMicroseconds(-1300);
}





