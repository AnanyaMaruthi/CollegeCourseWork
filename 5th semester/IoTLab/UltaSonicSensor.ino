#include<LiquidCrystal.h>
LiquidCrystal lcd(8,9,4,5,6,7);
int trigPin=2;
int echoPin=3;
void setup() {

lcd.begin(16,2);
lcd.setCursor(0,0);
pinMode(trigPin,OUTPUT);
pinMode(echoPin,INPUT);
Serial.begin(9600);
}

void loop() {
  long duration,inches,cm;
  lcd.setCursor(0,1);
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  duration=pulseIn(echoPin,HIGH);
  inches=microsecondsToInches(duration);
  cm=microsecondsToCentimeters(duration);
  lcd.print(inches);
  lcd.print("in , ");
  lcd.print(cm);
  lcd.print("cm");
  Serial.print(inches);
  Serial.println("in , ");
  Serial.print(cm);
  Serial.println("cm");
  delay(1000);
  }
  long microsecondsToInches(long microseconds)
  {
    return microseconds/74/2;
  }
  long microsecondsToCentimeters(long microseconds)
  {
    return microseconds/29/2;
  }
