#include <KeyboardController.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int val=analogRead(39);
  int a;
  int z;

  Serial.println(val);
  Serial.println(keyboard.getKey());

}
