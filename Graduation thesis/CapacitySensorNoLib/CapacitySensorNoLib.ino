
/*
  Created by Toshihiko Arai.
  https://101010.fun/iot/arduino-diy-touch-sensor.html
*/

const int SENSOR_1_OUT = 8;
const int SENSOR_1_IN = 9;
const int LED_PIN = 10;
const int threshold = 5;

void setup() {
  pinMode(SENSOR_1_OUT, OUTPUT);
  pinMode(SENSOR_1_IN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int counter = 0;
  digitalWrite(SENSOR_1_OUT, HIGH);
  while (digitalRead(SENSOR_1_IN)!=HIGH) counter++;
  digitalWrite(SENSOR_1_OUT, LOW);  
  delay(1);

  if (counter > threshold) {
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}