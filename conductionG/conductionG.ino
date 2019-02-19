//Lib
#include <WiFi.h>
#include <Wire.h>
#include "SSD1306Wire.h"
#include <WiFiUDP.h>
//#include <ArduinoOTA.h>
#include <OSCMessage.h>
#include <OSCBundle.h>
#include <OSCData.h>

#define PIN_MODE 100
#define DIGITAL_WRITE 101
#define DIGITAL_READ 102
#define ANALOG_WRITE 103
#define ANALOG_READ 104

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
  Serial.flush();
  c = 0;
  Serial.write(c);
  c = 255;
  Serial.write(c);
  c = 0;
  Serial.write(c);

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

  char commande;  
  if (Serial.available()>0) {
     commande = Serial.read();
     if (commande==PIN_MODE) commande_pin_mode();
     else if (commande==DIGITAL_WRITE) commande_digital_write();
     else if (commande==DIGITAL_READ) commande_digital_read();
     else if (commande==ANALOG_WRITE) commande_analog_write();
     else if (commande==ANALOG_READ) commande_analog_read();
  }

  void commande_pin_mode() {
    char pin,mode;
    while (Serial.available()<2);
    pin = Serial.read(); // pin number
    mode = Serial.read(); // 0 = INPUT, 1 = OUTPUT
    pinMode(pin,mode);
}

void commande_digital_write() {
   char pin,output;
   while (Serial.available()<2);
   pin = Serial.read(); // pin number
   output = Serial.read(); // 0 = LOW, 1 = HIGH
   digitalWrite(pin,output);
}

void commande_digital_read() {
   char pin,input;
   while (Serial.available()<1);
   pin = Serial.read(); // pin number
   input = digitalRead(pin);
   Serial.write(input);
}

void commande_analog_write() {
   char pin,output;
   while (Serial.available()<2);
   pin = Serial.read(); // pin number
   output = Serial.read(); // PWM value between 0 and 255
   analogWrite(pin,output);
}

void commande_analog_read() {
   char pin;
   int value;
   while (Serial.available()<1);
   pin = Serial.read(); // pin number
   value = analogRead(pin);
   Serial.write((value>>8)&0xFF); // 8 bits de poids fort
   Serial.write(value & 0xFF); // 8 bits de poids faible
}

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
