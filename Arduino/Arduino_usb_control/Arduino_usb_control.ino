const int ledPin = 12; // Testing

/*
const int led1 = 2;
const int led2 = 3;
const int led3 = 5;
const int led4 = 6;
const int buzzer = 9;
const int buttonPin = 8;     // the number of the pushbutton pin

const int gasPin = A0; //GAS sensor output pin to Arduino analog A0 pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int number = 0;
int state = 0;
int samples[NUMSAMPLES];
String readString;
double temp;
*/


void setup(){
    Serial.println("Initialising GPIO's as Outputs");
    pinMode(ledPin, OUTPUT);
/*
    //Initialising GPIO's.
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(buzzer, OUTPUT);
    // initialize the pushbutton pin as an input:
    pinMode(buttonPin, INPUT);
*/
    Serial.begin(9600);
}

void loop(){
    if (Serial.available()) {
        light(Serial.read() - '0');
    }

    smoke_level = analogRead(gasPin);
    Serial.println(smoke_level);
    /*
    buttonState = digitalRead(buttonPin);
    // check if the pushbutton is pressed.
    // if it is, the buttonState is HIGH:
    if (buttonState == HIGH) {
        delay(50);
        digitalWrite(buzzer, HIGH);      // turn buzzer on:
        delay(2000);
        }
    else{
        digitalWrite(buzzer, LOW);     // turn buzzer off:
    }
    */
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
