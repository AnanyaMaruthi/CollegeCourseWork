#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); //Pin9 RX , Pin 10 TX connected to--> Bluetooth TX,RX

int LED = 13;
int relay1 = 2;
int relay2 = 3;
int relay3 = 4;
int relay4 = 5;
char data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mySerial.begin(38400);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  digitalWrite(relay3, HIGH);
  digitalWrite(relay4, HIGH);
}

void loop() {
  while (Serial.available()){
    mySerial.write(Serial.read());
  }
  while (mySerial.available()){
    data = mySerial.read();
    Serial.write(data);
  }
//    if (data == '1'){
//      digitalWrite(LED, HIGH);
//    }
//    else if (data == '0'){
//      digitalWrite(LED, LOW);
//    }

   if (data == '1'){
    digitalWrite(relay1, LOW);
   }
   else if (data == '2'){
    digitalWrite(relay2, LOW);
   }
   else if (data == '3'){
    digitalWrite(relay3, LOW);
   }
   else if (data == '4'){
    digitalWrite(relay4, LOW);
   }
   else if (data == 'A'){
    digitalWrite(relay1, HIGH);
   }
   else if(data == 'B'){
    digitalWrite(relay2, HIGH);                  
   }


}
