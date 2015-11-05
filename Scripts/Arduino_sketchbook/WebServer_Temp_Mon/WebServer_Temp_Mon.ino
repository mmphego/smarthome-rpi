/*
  Web Server
 
 A simple web server that shows the temperature using an Arduino Wiznet Ethernet shield.
 
Parts list:

10k Thermistor
Breadboard/Veroboard
10k resistor
Arduino ( I use UNO)
Arduino Wiznet Ethernet shield

The Thermistor Circuit:
AREF---+3.3V----Therm----A0(Arduino)----10k res---> Gnd

Better Readings:
When doing analog readings, especially with a 'noisy' board like the arduino, we suggest two tricks to improve results.
One is to use the 3.3V voltage pin as an analog reference and the other is to take a bunch of readings in a row and average them.
The first trick relies on the fact that the 5V power supply that comes straight from your computer's USB does a lot of stuff on the Arduino, 
and is almost always much noisier than the 3.3V line (which goes through a secondary filter/regulator stage!) It's easy to use, simply connect 3.3V to AREF and use that as the VCC voltage. 
Because our calcuations don't include the VCC voltage, you don't have to change your equation. You do have to set the analog reference but that's a single line of code
Taking multiple readings to average out the result helps get slightly better results as well, since you may have noise or fluctuations, we suggest about 5 samples.

Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13

 
 */

#include <SPI.h>
#include <Ethernet.h>

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
 
// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(172,18,30,197);

// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
EthernetServer server(80);

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  // listen for incoming clients
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

  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
	  client.println("Refresh: 5");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          // output the value of each analog input pin
          //int analogChannel = 0;
          //for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
           // int sensorReading = analogRead(analogChannel);
           client.print("<CENTER><H1>");
           client.print("Temperature ");
            //client.print(analogChannel);
            client.print(" is ");
            client.print(steinhart);
            client.print(" &deg;C");
            client.print("</H1></CENTER>");
            client.println("<br />");       
          //}
          client.println("</html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } 
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(100);
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
  }
}

