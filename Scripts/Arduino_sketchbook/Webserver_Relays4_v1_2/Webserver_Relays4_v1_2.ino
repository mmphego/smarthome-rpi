/*
 Created by Mpho Mphego
 
 Arduino with Ethernet Shield, Quad Relay and Temperature Monitor
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
 
const int led = 2, led2 = 3, led3 = 5, led4 = 6;
int samples[NUMSAMPLES]; 
String readString;

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };   //physical mac address
byte ip[] = { 172, 18, 30, 197 };                      // ip in lan (that's what you need to use in your browser. ("192.168.1.178")
byte gateway[] = { 172, 18, 30, 10 };                   // internet access via router
byte subnet[] = { 255, 255, 255, 0 };                  //subnet mask
EthernetServer server(80);                             //server port     


void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip, gateway, subnet);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}


void loop() {
  
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

  // Create a client connection
  EthernetClient client = server.available();
  if (client) {
     Serial.println("new client");
    boolean currentLineIsBlank = true;
    while (client.connected()) {   
      if (client.available()) {
        char c = client.read();
     
        //read char by char HTTP request
        if (readString.length() < 100) {
          //store characters to string
          readString += c;
          //Serial.print(c);
         }

         //if HTTP request has ended
         if (c == '\n' && currentLineIsBlank) {          
           Serial.println(readString); //print to serial monitor for debuging
     
           client.println("HTTP/1.1 200 OK");
           client.println("Content-Type: text/html");
           client.println("Connection: close");  // the connection will be closed after completion of the response
  	   client.println("Refresh: 5");  // refresh the page automatically every 5 sec
           client.println();
           client.println("<!DOCTYPE HTML>");
           client.println("<html>");
           client.println("<CENTER><HEAD>");
           //client.println("<meta name='apple-mobile-web-app-capable' content='yes' />");
           //client.println("<meta name='apple-mobile-web-app-status-bar-style' content='black-translucent' />");
           //client.println("<link rel='stylesheet' type='text/css' href='http://randomnerdtutorials.com/ethernetcss.css' />");
           client.println("<TITLE>Simple Home Automation</TITLE>");
           client.println("</HEAD>");
           client.println("<BODY>");

           client.println("<H1>Simple Home Automation : Arduino</H1>");
           client.println("<br />");  

           client.println("<H2>");
           client.print("Current Temperature ");
           client.print(" is ");
           client.print(steinhart);
           client.print(" &deg;C");
           client.print("</H2>");

           client.println("<hr />");
           client.println("<br />");  
           client.println("<a href=\"/button1on\"\">Turn On LED 1</a>");
           client.println("<a href=\"/button1off\"\">Turn Off LED 1</a><br />");   
           client.println("<a href=\"/button2on\"\">Turn On LED 2</a>");
           client.println("<a href=\"/button2off\"\">Turn Off LED 2</a><br />");   
           client.println("<a href=\"/button3on\"\">Turn On LED 3</a>");
           client.println("<a href=\"/button3off\"\">Turn Off LED 3</a><br />");   
           client.println("<a href=\"/button4on\"\">Turn On LED 4</a>");
           client.println("<a href=\"/button4off\"\">Turn Off LED 4</a><br />"); 
           client.println("<br />");     
           client.println("<br />"); 
           client.println("<a href=\"/buttonson\"\">All on LED</a>");
           client.println("<a href=\"/buttonsoff\"\">All Off LED</a><br />"); 
           client.println("<br />");     
           client.println("<br />"); 
           
           //client.println("<p>Created by Rui Santos. Visit http://randomnerdtutorials.com for more projects!</p>");  
           client.println("<br /></CENTER>"); 
           client.println("</BODY>");
           client.println("</HTML>");
     
           delay(1);
           //stopping client
           client.stop();
           //controls the Arduino if you press the buttons
           if (readString.indexOf("button1on") > 0){
               digitalWrite(led, HIGH);
           }
           if (readString.indexOf("button1off") > 0){
               digitalWrite(led, LOW);
           }
           if (readString.indexOf("button2on") > 0){
               digitalWrite(led2, HIGH);
           }
           if (readString.indexOf("button2off") > 0){
               digitalWrite(led2, LOW);
           }
           if (readString.indexOf("button3on") > 0){
               digitalWrite(led3, HIGH);
           }
           if (readString.indexOf("button3off") > 0){
               digitalWrite(led3, LOW);
           }
           if (readString.indexOf("button4on") > 0){
               digitalWrite(led4, HIGH);
           }
           if (readString.indexOf("button4off") > 0){
               digitalWrite(led4, LOW);
           }
           if (readString.indexOf("buttonson") > 0){
             //int i;
             //for (i = 0; i < 4; i++){
               digitalWrite(led, HIGH);
               digitalWrite(led2, HIGH);
               digitalWrite(led3, HIGH);
               digitalWrite(led4, HIGH);
             //}
           }
           if (readString.indexOf("buttonsoff") > 0){
               digitalWrite(led, LOW);
               digitalWrite(led2, LOW);
               digitalWrite(led3, LOW);
               digitalWrite(led4, LOW);
           }
          //clearing string for next read
           readString="";  
           
         }
       }
    }
}
}

