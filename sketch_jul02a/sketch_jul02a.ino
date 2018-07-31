int p1 = 13;
int p2 = 11;
int p3 = 9;
int p4 = 6;
void setup() {
  // put your setup code here, to run once:
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(p1, HIGH);
  digitalWrite(p3, LOW);
  digitalWrite(p2, LOW);
  digitalWrite(p4, LOW);
  delay(500);
  digitalWrite(p1, LOW);
  digitalWrite(p3, HIGH);
  digitalWrite(p2, LOW);
  digitalWrite(p4, LOW);
  delay(500);
  digitalWrite(p1, LOW);
  digitalWrite(p3, LOW);
  digitalWrite(p2, HIGH);
  digitalWrite(p4, LOW);
  delay(500);
  digitalWrite(p1, LOW);
  digitalWrite(p3, LOW);
  digitalWrite(p2, LOW);
  digitalWrite(p4, HIGH);
  delay(500);
  
}





