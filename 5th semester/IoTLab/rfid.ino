#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);

int count = 0;
char input[12];
boolean flag;
char check[12] = "510093E02A0B";

void setup()
{
	Serial.begin(9600);
	mySerial.begin(9600);
}

void loop()
{
	if (mySerial.available())
	{
		count = 0;
		flag = true;
		while (mySerial.available() && count < 12)
		{
			input[count] = mySerial.read();
			if (input[count] != check[count])
			{
				Serial.println("Access denied");
				flag = false;
				break;
			}
			count++;
		}
		if (flag)
		{
			Serial.println("Access granted");
		}
	}
}
