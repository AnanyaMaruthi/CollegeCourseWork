int LED = 11;
int resistor = 2;

void setup(){
  pinMode(LED, OUTPUT);
  pinMode(resistor, INPUT);
  Serial.begin(9600);
}

void loop(){
  int resistance = analogRead(resistor);
//  resistance = (resistance / 1024) * 256;
  int brightness = map(resistance, 0, 1023, 0, 255);
  Serial.print("Input");
  Serial.print(resistance);
  Serial.print("Converted value");
  Serial.print(brightness);
  delay(2000);
  analogWrite(LED, brightness);
}
