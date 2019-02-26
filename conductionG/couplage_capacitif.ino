#include <WiFi.h>
#include <Wire.h>
#include <WiFiUDP.h>
// Variable
bool test = true;    // switch
long DeltaTime = 10; // periode
long LastTime = 0;   // last Switch


void setup() {
  // Init Serial
  Serial.begin(115200);

  // Init Pins and Time
  pinMode(16, OUTPUT);
  LastTime = millis();

  int test=0;
}

void loop() {
  // put your main code here, to run repeatedly:
  long TDelta = millis()-LastTime;
  
  if (TDelta > DeltaTime)
  {
    test = !test;
    LastTime = millis();
  }

  if (test){
    digitalWrite(16, HIGH);
  }
  else{
    digitalWrite(16, LOW);
  } 
  int Value = analogRead(39); //39 = SVN Pin
  Serial.println(Value);
}
