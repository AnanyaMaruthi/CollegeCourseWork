#include <Servo.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetooth(9, 10);
Servo fan;
int LED = 13;
int motorPin = 3;
int fanMode = 0;
char data;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(motorPin, OUTPUT);
  fan.attach(motorPin);
  Serial.begin(9600);
  bluetooth.begin(38400);
}

void loop() {
  if (Serial.available()){
    bluetooth.print(Serial.read());
  }

  if (bluetooth.available()){
    data = bluetooth.read();
    Serial.println(data);

    if (data == '0'){
      digitalWrite(LED, LOW);
    }

    else if(data == '1'){
      digitalWrite(LED, HIGH);
    }

    else if(data == '2'){
      fanMode = 1;
      Serial.println("Fan ON");
    }

    else if(data == '3'){
      fanMode = 0;
      Serial.println("Fan OFF");
    }
  }
  
  if (fanMode == 1){
    for(int i = 0; i <= 180; i++){
      fan.write(i);
      delay(10);
    }
    for(int i = 180; i >= 0; i--){
      fan.write(i);
      delay(10);
    }
  }


}
