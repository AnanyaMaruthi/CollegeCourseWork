#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); //Pin9 RX , Pin 10 TX connected to--> Bluetooth TX,RX

int LED = 13;
char data;

void setup()
{
	Serial.begin(9600);
	mySerial.begin(38400);
	pinMode(LED, OUTPUT);
}

void loop()
{
	while (Serial.available())
	{
		mySerial.write(Serial.read());
	}
	while (mySerial.available())
	{
		data = mySerial.read();
		Serial.write(data);
	}
	if (data == '1')
	{
		digitalWrite(LED, HIGH);
	}
	else if (data == '0')
	{
		digitalWrite(LED, LOW);
	}
}
