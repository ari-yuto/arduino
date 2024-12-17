#include <Arduino_LSM9DS1.h>
#include <Arduino_JSON.h>

const int SENSOR_1_OUT = 2;
const int SENSOR_1_IN = 3;
const int threshold = 30;

unsigned long time_data = 0;
unsigned long second = 0;
unsigned long Time = 0;

JSONVar doc;

void setup() {
  pinMode(SENSOR_1_OUT, OUTPUT);
  pinMode(SENSOR_1_IN, INPUT);
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
  delay(10);
  float x_accel, y_accel, z_accel, x_gyro, y_gyro, z_gyro;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x_accel, y_accel, z_accel);
  }

  time_data = millis();
  Time = time_data / 15;

  doc["time"] = Time;
  doc["DO"] = analogRead(A0); //センサの値を辞書に登録
  doc["X_accel"] = x_accel;
  doc["Y_accel"] = y_accel;
  doc["Z_accel"] = z_accel;
  Serial.println(doc); //Jsonが出力される

}