#include <Arduino_LSM9DS1.h>
#include <Arduino_JSON.h>

/*
  Created by Toshihiko Arai.
  https://101010.fun/iot/arduino-diy-touch-sensor.html
*/

const int SENSOR_1_OUT = 2;
const int SENSOR_1_IN = 3;
const int LED_PIN = 5;
const int threshold = 30;

unsigned long time_data = 0;
unsigned long second = 0;
unsigned long Time = 0;

JSONVar doc;


void setup() {
  pinMode(SENSOR_1_OUT, OUTPUT);
  pinMode(SENSOR_1_IN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

    Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in g's");
  Serial.println("X\tY\tZ");
}

void loop() {
  int counter = 0;
  digitalWrite(SENSOR_1_OUT, HIGH);
  while (digitalRead(SENSOR_1_IN)!=HIGH) counter++;
  // Serial.println(counter);
  digitalWrite(SENSOR_1_OUT, LOW);  
  delay(50);

  if (counter > threshold) {
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }

  float x_accel, y_accel, z_accel, x_gyro, y_gyro, z_gyro;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x_accel, y_accel, z_accel);
  }

  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x_gyro, y_gyro, z_gyro);
  }

  // Serial.println(analogRead(A0));

  time_data = millis();
  Time = time_data / 53;
  // second = time_data / 1000L;
  // Serial.println(second);

  doc["time"] = Time;
  doc["DO"] = analogRead(A0); //センサの値を辞書に登録
  doc["D1"] = counter;
  doc["X_accel"] = x_accel;
  doc["Y_accel"] = y_accel;
  doc["Z_accel"] = z_accel;
  doc["X_gyro"] = x_gyro;
  doc["Y_gyro"] = y_gyro;
  doc["Z_gyro"] = z_gyro;
  Serial.println(doc); //Jsonが出力される

}