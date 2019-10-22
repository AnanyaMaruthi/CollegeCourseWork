int LED = 11;
int lightSensor = A0;
void setup()
{
    pinMode(LED, OUTPUT);
    // pinMode(lightSensor, INPUT);
    Serial.begin(9600);
}

void loop()
{
    int sensedValue = analogRead(lightSensor);
    Serial.println(sensedValue);
    if (sensedValue < 200)
    {
        digitalWrite(LED, HIGH);
        Serial.println(sensedValue);
        delay(100);
    }
    else
    {
        digitalWrite(LED, LOW);
        Serial.println(sensedValue);
        delay(100);
    }
}
