#include <SoftwareSerial.h>
#include "ArduinoESPAT.h"

ESPAT espat("Buffalo-G-6D27", "ncu78f6a83u7u");

void setup() {
  Serial.begin(9600);

  // pinMode( 13, OUTPUT);
  if(espat.begin()){
    Serial.println("Initialize OK");
  } else{
    Serial.println("Initialize Fail");
  }

  if(espat.changeMode(1)){
    Serial.println("Mode OK");
  } else{
    Serial.println("Mode not OK");
  }

  if(espat.tryConnectAP()){
    Serial.println("Connected");
  }else{
    Serial.println("Connect Failed");
  }

  Serial.println(espat.clientIP());

  Serial.println(espat.get("gihyo.jp","/book/",80));

}

void loop() {
}