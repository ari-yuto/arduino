#include <SoftwareSerial.h>
#include <ArduinoESPAT.h>

ESPAT espat("Buffalo-G-6D27", "ncu78f6a83u7u");

void setup() {
  pinMode(7, INPUT);

  delay(1000);
  Serial.begin(9600);

  if(espat.begin()){
    Serial.println("Initialize OK");
  } else{
    Serial.println("Initialize Fail");
  }

  if(espat.tryConnectAP()){
    Serial.println("Connected");
  }else{
    Serial.println("Connect Failed");
  }

  Serial.println(espat.clientIP());

}

void loop() {
    if (digitalRead(7) == LOW){
        return;
    }
    // String URL = "https://hooks.zapier.com/hooks/catch/19686420/2471p8o/";
    // String Res = espat.get(URL);
    // Serial.println(Res);
    // bool res = espat.get("hooks.zapier.com","/hooks/catch/19686420/2471p8o/",80);
    // Serial.println(res);

    // Serial.println(espat.get("hooks.zapier.com","/hooks/catch/19686420/2471p8o/",80));
    espat.get("hook.eu2.make.com","/9y2qwyr6rdw26tmoqtlkkmke8xjgpc1k",80);

    delay(1000);
}