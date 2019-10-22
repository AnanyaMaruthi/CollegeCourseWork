int RED = 4;
int YELLOW = 5;
int GREEN = 6;

void setup()
{
    pinMode(RED, OUTPUT);
    pinMode(YELLOW, OUTPUT);
    pinMode(GREEN, OUTPUT);
}

void loop()
{
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, HIGH);
    delay(5000);
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, HIGH);
    delay(2000);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, HIGH);
    delay(6000);
}
