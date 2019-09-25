#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);

int count = 0;
char input[12];
boolean flag;
char check[12] = {'5', '1','0','0','9','3','E','0','2','A','0','8'};
  
void setup(){
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("Here");

}

void loop(){
  
  if(mySerial.available()){
    
    count = 0;
    flag = true;
    while(mySerial.available() && count < 12){
      
      input[count] = mySerial.read();
      if(input[count] != check[count]){
       
        //Serial.println("Access denied");
        flag = false;
        //break;
      }
      count++;
      delay(5);
    }
    Serial.print(input);
    if(flag){
      Serial.println("Access granted");
    }
    else{
      Serial.println("Access denied");
    }
  }
}
