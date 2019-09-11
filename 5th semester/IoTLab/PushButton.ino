int ledPin = 13;
int push = 2;
void setup() {
  // put your setup code here, to run once:
  pinMode(push, INPUT);
  pinMode(ledPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(push)==LOW){
    digitalWrite(ledPin,LOW);
  }
  else{
    digitalWrite(ledPin,HIGH);
  }

}
