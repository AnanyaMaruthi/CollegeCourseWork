int red = 2;
int green = 3;
int blue = 4;

void setup()
{
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  for (int i = 0; i <= 255; i = i + 25)
  {
    for (int j = 0; j <= 255; j = j + 25)
    {
      for (int k = 0; k <= 255; k = k + 25)
      {
        analogWrite(red, i);
        analogWrite(green, j);
        analogWrite(blue, k);
        Serial.print(i);
        Serial.print(" ");
        Serial.print(j);
        Serial.print(" ");
        Serial.println(k);
        delay(10);
      }
    }
  }
}
