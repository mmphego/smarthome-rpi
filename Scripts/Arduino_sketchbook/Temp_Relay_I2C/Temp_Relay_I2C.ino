#include <Wire.h>
 
#define SLAVE_ADDRESS 0x04
#define THERMISTORPIN A0         
// resistance at 25 degrees C
#define THERMISTORNOMINAL 10000      
// temp. for nominal resistance (almost always 25 C)
#define TEMPERATURENOMINAL 25   
// how many samples to take and average, more takes longer
// but is more 'smooth'
#define NUMSAMPLES 25
// The beta coefficient of the thermistor (usually 3000-4000)
#define BCOEFFICIENT 3950
// the value of the 'other' resistor
#define SERIESRESISTOR 10000  

const int led1 = 2;
const int led2 = 3;
const int led3 = 5;
const int led4 = 6;
const int buzzer = 9;
const int buttonPin = 8;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int number = 0;
int state = 0;
int samples[NUMSAMPLES]; 
String readString;
double temp;
 
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  Serial.println("Initialising GPIO's as Outputs");  
  //Initialising GPIO's.
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(buzzer, OUTPUT);      
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);  
 
  Serial.println("Initialising I2C as Slave");  
 // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  Serial.println("Define callbacks for i2c communication");
 // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Initialization Completed!!!");
}
 
void loop() {
  delay(100);
  temp = GetTemp();
//  Serial.println(temp);
// read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {     
    delay(50);
    digitalWrite(buzzer, HIGH);      // turn buzzer on:
    delay(2000);
  } 
  else {
    digitalWrite(buzzer, LOW);     // turn buzzer off:
  }
}
 
// callback for received data
void receiveData(int byteCount){
 
 while(Wire.available()) {

  number = Wire.read();
  uint8_t i;
  float average;
 
  // take N samples in a row, with a slight delay
  for (i=0; i< NUMSAMPLES; i++) {
   samples[i] = analogRead(THERMISTORPIN);
   delay(10);
  }
 
  // average all the samples out
  average = 0;
  for (i=0; i< NUMSAMPLES; i++) {
     average += samples[i];
  }
  average /= NUMSAMPLES;
 
//  Serial.print("Average analog reading "); 
//  Serial.println(average);
 
  // convert the value to resistance
  average = 1023 / average - 1;
  average = SERIESRESISTOR / average;
//-------------------------------------------
// To display on Serial monitor
//  Serial.print("Thermistor resistance "); 
//  Serial.println(average);

// Read about the Steinhart–Hart equation
// http://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation

  float steinhart;
  steinhart = average / THERMISTORNOMINAL;     // (R/Ro)
  steinhart = log(steinhart);                  // ln(R/Ro)
  steinhart /= BCOEFFICIENT;                   // 1/B * ln(R/Ro)
  steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15); // + (1/To)
  steinhart = 1.0 / steinhart;                 // Invert
  steinhart -= 273.15;                         // convert to C


  if (number == 1){
   if (state == 0){
    digitalWrite(led1, HIGH); // set the LED on
    Serial.println("LED1 On");
    state = 1;
   } else{
    digitalWrite(led1, LOW); // set the LED off
    Serial.println("LED1 Off");
    state = 0;
   }
  }
  if (number == 2){
   if (state == 0){
    digitalWrite(led2, HIGH); // set the LED on
    Serial.println("LED2 On");
    state = 1;
   } else{
    digitalWrite(led2, LOW); // set the LED off
    Serial.println("LED2 Off");
    state = 0;
   }
  }
   if (number == 3){
   if (state == 0){
    digitalWrite(led3, HIGH); // set the LED on
    Serial.println("LED3 On");
    state = 1;
   }
   else{
    digitalWrite(led3, LOW); // set the LED off
    Serial.println("LED3 Off");
    state = 0;
   }
  }
  if (number == 4){
    if (state == 0){
      digitalWrite(led4, HIGH); // set the LED on
      Serial.println("LED4 On");
      state = 1;
    } 
    else{
      digitalWrite(led4, LOW); // set the LED off
      Serial.println("LED4 Off");
       state = 0;
    }
  }
   if (number == 5){
   if (state == 0){
    digitalWrite(led1, HIGH); // set the LED on
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    digitalWrite(led4, HIGH);  
    Serial.println("All LED's On");
    state = 1;
   } else{
     digitalWrite(led1, LOW);
     digitalWrite(led2, LOW);
     digitalWrite(led3, LOW);
     digitalWrite(led4, LOW);
     Serial.println("All LED's Off");     
     state = 0;
   }
  }
 
  if(number == 6) {
    number = (float)temp; 
    //Serial.println(number);
  }
  if(number == 7) {
  Serial.print("Temp : ");
  Serial.print(steinhart);
  Serial.println("\176C");
  number = (float)steinhart;
  }
 }
}


// callback for sending data
void sendData(){
 Wire.write(number);
} 

// Get the internal temperature of the arduino
double GetTemp(void)
{
 unsigned int wADC;
 double t;
 ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
 ADCSRA |= _BV(ADEN); // enable the ADC
 delay(20); // wait for voltages to become stable.
 ADCSRA |= _BV(ADSC); // Start the ADC
 while (bit_is_set(ADCSRA,ADSC));
 wADC = ADCW;
// t = ADCW;
// Serial.println(wADC);
 t = ((wADC - 324.31 ) / 1.22 ); 
 //t = int(t);
 //t =  (5.0 / 9.)*(t - 32.0);//farheinheit to celcius
 //Serial.println(t);
 return (t);
}


