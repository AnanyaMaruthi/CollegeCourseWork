int LED = 11;
int potentiometer = 2;

void setup()
{
    pinMode(LED, OUTPUT);
    pinMode(potentiometer, INPUT); //Not required
    Serial.begin(9600);
}

void loop()
{
    int sensedValue = analogRead(potentiometer);
    //  sensedValue = (sensedValue / 1024) * 256;
    int brightness = map(sensedValue, 0, 1023, 0, 255);
    Serial.print("Input");
    Serial.print(sensedValue);
    Serial.print("Converted value");
    Serial.println(brightness);
    delay(2000);
    analogWrite(LED, brightness);
}
