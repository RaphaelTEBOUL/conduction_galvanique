#include <WiFi.h>
#include <Wire.h>
#include <WiFiUDP.h>
// Variable
bool test = true;    // switch
long periode = 10; // periode
long LastTime = 0;   // last Switch


void setup() {
  // Init Serial
  Serial.begin(9600);

  // Init Pins and Time
  pinMode(16, OUTPUT);
  LastTime = millis();

  int test=0;
}

void loop() {
  long TDelta = millis()-LastTime;
  
  if (TDelta > periode)
  {
    test = !test;
    LastTime = millis();
  }
  
  if (test){
    digitalWrite(16, HIGH);
    int Value = analogRead(39);
    Serial.println(Value);
    delay(500);
  }
  else{
    digitalWrite(16, LOW);
    int Value = analogRead(39);
    Serial.print(Value);
  } 
  
}
