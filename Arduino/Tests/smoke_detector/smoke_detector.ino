const int gasPin = A0; //GAS sensor output pin to Arduino analog A0 pin
String sensor_val = "Sensor value: ";

void setup(){
    Serial.println("Initialising GPIO's as Outputs");
    pinMode(gasPin, INPUT);
    Serial.begin(9600);
}


void loop(){
    String smoke_level = sensor_val + analogRead(gasPin);
    Serial.println(smoke_level);
    delay(500);
}
