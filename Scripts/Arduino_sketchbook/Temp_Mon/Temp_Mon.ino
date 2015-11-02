/*
Arduino thermometer, LCD Display, Thermistor

Its an arduino project, creating a temperature measurer, with a thermistor, and outputs to an lcd display.

Parts list:
16x2 LCD
10k Thermistor
10k Variable Resistor
Breadboard/Veroboard
10k resistor
Arduino ( I use UNO)

How I did it:

The LCD circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)

The Thermistor Circuit:
AREF---+3.3V----Therm----A0(Arduino)----10k res---> Gnd

Better Readings:
When doing analog readings, especially with a 'noisy' board like the arduino, we suggest two tricks to improve results. One is to use the 3.3V voltage pin as an analog reference and the other is to take a bunch of readings in a row and average them.
The first trick relies on the fact that the 5V power supply that comes straight from your computer's USB does a lot of stuff on the Arduino, and is almost always much noisier than the 3.3V line (which goes through a secondary filter/regulator stage!) It's easy to use, simply connect 3.3V to AREF and use that as the VCC voltage. Because our calcuations don't include the VCC voltage, you don't have to change your equation. You do have to set the analog reference but that's a single line of code
Taking multiple readings to average out the result helps get slightly better results as well, since you may have noise or fluctuations, we suggest about 5 samples.

Here's the code 
*/
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
// which analog pin to connect
#define THERMISTORPIN A0         
// resistance at 25 degrees C
#define THERMISTORNOMINAL 10000      
// temp. for nominal resistance (almost always 25 C)
#define TEMPERATURENOMINAL 25   
// how many samples to take and average, more takes longer
// but is more 'smooth'
#define NUMSAMPLES 5
// The beta coefficient of the thermistor (usually 3000-4000)
#define BCOEFFICIENT 3950
// the value of the 'other' resistor
#define SERIESRESISTOR 10000    
 
int samples[NUMSAMPLES];
 
void setup(void) {
  lcd.begin(16, 2);
  lcd.clear();
  Serial.begin(9600);
  analogReference(EXTERNAL);
}
 
void loop(void) {
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

//-------------------------------------------
// To display on Serial monitor 
//  Serial.print("Temperature "); 
//  Serial.print(steinhart);
//  Serial.println(" *C");
  //delay(1000);
  lcd.setCursor(0, 0);
  lcd.print("Temp : ");
  lcd.print(steinhart);
  lcd.print("\337C");
  //lcd.print(" *C");
  lcd.setCursor(0, 1);
  lcd.print("SANSA Office");  
  delay(1000);
  lcd.clear();
}
