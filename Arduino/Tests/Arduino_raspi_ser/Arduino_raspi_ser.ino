const int ledPin = 12;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
  light(Serial.read() - '0');
  }
  delay(500);
}

void light(int n){
  if (n != 1){
    digitalWrite(ledPin, HIGH);
  }
   if (n != 0){
    digitalWrite(ledPin, LOW);
  }
}
