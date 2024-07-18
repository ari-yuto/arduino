const int VOL_PIN = A0;

void setup()                    
{
   Serial.begin(9600);
   pinMode(12, OUTPUT);
}

void loop()                    
{

    int value;
    float volt;
  	float sound;


    // Serial.print(millis() - start);        // check on performance in milliseconds
    // Serial.print("\t");                    // tab character for debug windown spacing

    // Serial.print(total1);                  // print sensor output 1
    // Serial.println("\t");

    value = analogRead( VOL_PIN );

    volt = value * 5000.0 / 1023.0;
  	sound = 262 + (volt/5000.0)*232;

    Serial.print( "Value: " );
    Serial.print( value );
    Serial.print( "  Volt: " );
    Serial.print( volt );
    Serial.println("mV");
  
  	tone(12, sound);

    delay(100);                             // arbitrary delay to limit data to serial port 
}