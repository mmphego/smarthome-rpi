const int buttonPin = 7;     // the number of the pushbutton pin
const int buzzer = 8;
const int led1 = 9;
const int led2 = 10;
const int led3 = 11;
const int led4 = 12;

const int gasPin = A0; //GAS sensor output pin to Arduino analog A0 pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int state = 0;
String readString;
String sensor_val = "Sensor value: ";
double temp;
byte number = 0;

void setup(){
    Serial.println("Initialising GPIO's as Outputs");
    //Initialising GPIO's output.
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(buzzer, OUTPUT);
    // initialize the inputs
    pinMode(buttonPin, INPUT);
    pinMode(gasPin, INPUT);
    Serial.begin(9600);
}

void loop(){
  if (Serial.available() > 0) {
        light(Serial.read() - '0');
    }
    String smoke_level = sensor_val + analogRead(gasPin);
    Serial.println(smoke_level);

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
    delay(1000);
}

void light(int n){

    if (n == 1){
        digitalWrite(led1, HIGH);
        Serial.print(String('led1_1'));
        //delay(500);
      }
    if (n == 2){
        digitalWrite(led1, LOW);
        Serial.print('led1_0');
        //delay(500);
      }

    if (n == 3){
        digitalWrite(led2, HIGH);
        Serial.println(String('led2_1'));
        //delay(500);
      }
    if (n == 4){
        digitalWrite(led2, LOW);
        Serial.println(String('led2_0'));
        //delay(500);
      }

    if (n == 5){
        digitalWrite(led3, HIGH);
        Serial.println(String('led3_1'));
        //delay(500);
      }
    if (n == 6){
        digitalWrite(led3, LOW);
        Serial.println(String('led3_0'));
        //delay(500);
      }
    if (n == 7){
        digitalWrite(led4, HIGH);
        Serial.println(String('led4_1'));
        //delay(500);
      }
    if (n == 8){
        digitalWrite(led4, LOW);
        Serial.println(String('led4_0'));
        //delay(500);
      }
}
