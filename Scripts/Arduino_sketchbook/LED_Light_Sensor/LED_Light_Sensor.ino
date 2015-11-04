
#define READ A1
#define LED 6
int basis = 0;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(57600);
}

void loop() {
  int sens = readLED(50);
  basis = sens - 20;                 // setting sensitivity - now it will react if the LED is 20 lower than the setting above
  for(int y = 0; y < 1000; y++) {    // after every 1000 tests the program will reset the led to cope with changing light
    sens = readLED(50);
    Serial.println(sens);
    if (sens < basis)                // testing is the led was in the dark
      digitalWrite(LED, HIGH);     
    else 
      digitalWrite(LED, LOW);
  }
}

int readLED(int number) {            // Read analog value n times and avarage over those n times
  int totaal = 0;
  for(int x = 0; x < number; x++) {
    totaal += analogRead(READ);
    delay(10);
  }
  return totaal/number;
}
