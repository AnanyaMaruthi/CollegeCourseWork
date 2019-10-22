int ledPin = 13;
int pushButton = 2;
void setup()
{
	pinMode(pushButton, INPUT);
	pinMode(ledPin, OUTPUT);
}

void loop()
{
	if (digitalRead(pushButton) == LOW)
	{
		digitalWrite(ledPin, LOW);
	}
	else
	{
		digitalWrite(ledPin, HIGH);
	}
}
