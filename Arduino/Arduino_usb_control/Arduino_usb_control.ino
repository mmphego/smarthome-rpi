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
//for (int i = 0; i < n; i++) {
  if (n == 60){
    digitalWrite(ledPin, HIGH);
  //delay(100);
  }
  if (n == 61){
  digitalWrite(ledPin, LOW);
  //delay(100);
  }
//}
}
