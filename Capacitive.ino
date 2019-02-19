//Lib
#include <WiFi.h>
#include <Wire.h>
#include "SSD1306Wire.h"
#include <WiFiUDP.h>
//#include <ArduinoOTA.h>
#include <OSCMessage.h>
#include <OSCBundle.h>
#include <OSCData.h>



//Wifi connection Adress
const char *ssid = "WifiIOT";
const char *password = "WifiIOT2019";
WiFiUDP UDP;
const IPAddress outIp(192,168,0,2);          // remote IP (not needed for receive)
const unsigned int outPort = 12000;          // remote port (not needed for receive)
const unsigned int localPort = 10000;        // local port to listen for UDP packets (here's where we send the packets)

// Screen
//SSD1306Wire  display(0x3c, 5, 4); //I2C: Pin 4=SDA et Pin 5=SCL

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

  // Init WIFI
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  int test=0;
  while (WiFi.status() != WL_CONNECTED  && test <= 20) {
    delay(500);
    Serial.print(".");
   
    test++;
  }
  
  Serial.println();
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  
  
  // Launche UDP Connection
  //LaunchUDP(localPort);
}

void loop() {
  // put your main code here, to run repeatedly:
  long TDelta = millis()-LastTime;
  
  if (TDelta > DeltaTime)
  {
    //Serial.println("Switch");
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
  if (test){
    Serial.println(Value);
  }
}
