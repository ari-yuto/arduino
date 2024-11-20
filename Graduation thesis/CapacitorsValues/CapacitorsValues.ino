/*
  Created by Toshihiko Arai.
  https://101010.fun/iot/arduino-measure-capacitance.html
*/
#include <Arduino.h>

const int PULSE_PIN = 2;
const int DIGITAL_READ_PIN = 3;
const int ANALOG_READ_PIN = 5;

const double E = 5.06; // GPIO電圧実測値
const double R = 2000000.0; // 2MΩ
const double V = E * 0.632;

void setup()
{
  Serial.begin(9600);
  pinMode(PULSE_PIN, OUTPUT);
  digitalWrite(PULSE_PIN, LOW);
}

void discharge() { 
  pinMode(DIGITAL_READ_PIN, OUTPUT);
  digitalWrite(DIGITAL_READ_PIN, LOW);
  delay(500);
  pinMode(DIGITAL_READ_PIN, INPUT);
  delay(10);
}

unsigned long charge() {
  digitalWrite(PULSE_PIN, HIGH);
  return micros();
}

void loop() {
  discharge();

  unsigned long time_start = charge();

  double volts = 0;
  while (volts < V)
  {
    volts = double(analogRead(ANALOG_READ_PIN)) / 1023.0 * E;
  }

  double T = micros() - time_start; // T: 時定数
  double c;
  char *farad = "uF";

  if (T < 2500)
  {
    c = T / R * 1000000; // pFに対応
    farad = "pF";
  }
  else if (T < 50000)
  {
    c = T / R * 1000; // nFに対応
    farad = "nF";
  }
  else
  {
    c = T / R; // uF
  }

  
  Serial.print(c);
  Serial.print(farad);

  Serial.println();
  digitalWrite(PULSE_PIN, LOW);
  discharge();

}