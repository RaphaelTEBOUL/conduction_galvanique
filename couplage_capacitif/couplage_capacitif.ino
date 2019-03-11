#include <Wire.h>

// Variable
bool test = true;    // switch
long DeltaTime = 10; // periode
long LastTime = 0;   // last Switch
long vitesse =0;
long temps;
int cpt= 0;

void setup() {
  // Init Serial
  Serial.begin(115200);

  // Init Pins and Time
  pinMode(16, OUTPUT);
  LastTime = millis();

  int test=0;
}

void loop() {
  
  long TDelta = millis()-LastTime;
  
  if (TDelta > DeltaTime)
  {
    test = !test;
    LastTime = millis();
  }

  if (test){
    digitalWrite(16, HIGH);
    //Serial.println(5);
  }
  else{
    digitalWrite(16, LOW);
    //Serial.println(0);
  } 

  temps=millis();
  while(cpt<50){
    int Value = analogRead(39); //39 = SVN Pin
    Serial.println((Value));
    cpt++;
  }
 
  Serial.println(10000);
  cpt=0;
 
}
