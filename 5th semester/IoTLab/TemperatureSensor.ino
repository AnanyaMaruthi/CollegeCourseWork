int sensor = 2;
void setup()
{
	Serial.begin(9600);
}

void loop()
{
	int rawVoltage = analogRead(sensor);
	float millivolts = (rawVoltage / 1024.0) * 5000;
	float celsius = millivolts / 10;
	Serial.print(celsius);
	Serial.print(" degree celsius \n");
	Serial.print((celsius * 9) / 5 + 32);
	Serial.print(" degree farenheit\n");
	delay(5000);
}
