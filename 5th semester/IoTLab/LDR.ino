int LED = 11;
int sensor = A0;
void setup(){
  pinMode(LED, OUTPUT);
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop(){
  int sensedValue = analogRead(sensor);
  Serial.println(sensedValue);
  delay(100);

//  if(sensedValue < 200){
//  
//    digitalWrite(LED, HIGH);
//    Serial.println(sensedValue);
//    delay(100);
//    
//  }
//  else
//  {
//    digitalWrite(LED, LOW);
//    Serial.println(sensedValue);
//    delay(100);
//  }
  
}
