//int LED = 11;

void setup(){
  pinMode(LED, OUTPUT);
}

void loop(){

  int i;
  for(i = 0; i <= 255; i += 5){
    analogWrite(LED, i);
    delay(100);
  }
  for(i = 255; i >= 0; i -= 5){
    analogWrite(LED, i);
    delay(100);
  }
}
