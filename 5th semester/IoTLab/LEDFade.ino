int LED = 11;

void setup()
{
    pinMode(LED, OUTPUT);
}

void loop()
{
    for (int i = 0; i <= 255; i += 5)
    {
        analogWrite(LED, i);
        delay(100);
    }
    for (int i = 255; i >= 0; i -= 5)
    {
        analogWrite(LED, i);
        delay(100);
    }
}
