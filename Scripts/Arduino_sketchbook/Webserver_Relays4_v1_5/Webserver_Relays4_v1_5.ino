/*
 Created by Mpho Mphego
 
 Arduino with Ethernet Shield, Quad Relay ,Temperature Monitor and NTP client
 */

#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>

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
 
int led = 2, led2 = 3, led3 = 8, led4 = 6;
int samples[NUMSAMPLES]; 
String readString;

unsigned int localPort = 8888;      // local port to listen for UDP packets
const int NTP_PACKET_SIZE= 48; // NTP time stamp is in the first 48 bytes of the message
byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets 
EthernetUDP Udp; // A UDP instance to let us send and receive packets over UDP
/* Set this to the offset (in seconds) to your local time
   This example is GMT +3 */
const int timeZoneOffset = 3;
const int minuteOffset = 1;

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };   //physical mac address
byte ip[] = { 172, 18, 30, 197 };                      // ip in lan (that's what you need to use in your browser. ("192.168.1.178")
byte gateway[] = { 172, 18, 30, 10 };                   // internet access via router
byte subnet[] = { 255, 255, 255, 0 };                  //subnet mask

IPAddress timeServer(172,18,30,100); // time-a.timefreq.bldrdoc.gov NTP server
// IPAddress timeServer(132, 163, 4, 102); // time-b.timefreq.bldrdoc.gov NTP server
// IPAddress timeServer(132, 163, 4, 103); // time-c.timefreq.bldrdoc.gov NTP server
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
  Udp.begin(localPort);
  server.begin();
  Serial.print("Server is at ");
  Serial.println(Ethernet.localIP());
  // initialise all led's off
  //digitalWrite(led, LOW);
  //digitalWrite(led2, LOW);
  //digitalWrite(led3, LOW);
  //digitalWrite(led4, LOW);
}


void loop() {
  
  EthernetClient client = server.available();
  sendNTPpacket(timeServer); // send an NTP packet to a time server
  // wait to see if a reply is available
  delay(100); 
  
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
//  EthernetClient client = server.available();
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
  	   //client.println("Refresh: 5");  // refresh the page automatically every 5 sec
           client.println();
           client.println("<!DOCTYPE HTML >");
           client.println("<html>");
           client.println("<HEAD> ");
           client.println("<meta http-equiv='refresh' content ='5; url=http://172.18.30.197/ '>");
//           client.println("<meta http-equiv='refresh' content ='5' > ");
           client.println("<meta name='HandheldFriendly' content='true' /> ");
           client.println("<meta name='viewport' content='width=device-width, height=device-height, user-scalable=no' />");
           client.println("<meta name='apple-mobile-web-app-capable' content='yes' />");
           client.println("<meta name='apple-mobile-web-app-status-bar-style' content='black-translucent' />");
           client.println("<link rel='stylesheet' type='text/css' href='http://172.18.30.110/ethernetcss.css' />"); //direct css to dropbox
           client.println("<TITLE>Simple Home Automation</TITLE>");
           client.println("</HEAD>");
           client.println("<BODY>");
           
           //client.println("<div id='Header' style='float:left;height:80px;width:1810px;'");
           //client.println("<p 'Stable_Images/SANSA_Header_main2.jpg' width='890' height='80' class ='text'>");
           //client.println("<p id='time' style='float:right;'>DATE:  24-04-2013 <br>TIME:  07:11 <br>DOY:   114</p>");
           //client.println("</div>");
           
           client.println("<H1>Simple Home Automation : Arduino</H1>");
           client.println("<H2>");
           //client.println("<div id="Header" style="float:left;height:80px;width:1810px;">");
           //client.println("<img src="http://172.18.30.100/SANSA_Systems/Stable_Images/SANSA_Header_main2.jpg" width="890" height="80" class ="Image">");
           //client.println("<p id="time" style="float:right;">DATE:  24-04-2013 <br>TIME:  07:11 <br>DOY:   114</p>");
           //client.println("</div>");

            if ( Udp.parsePacket() ) {  
              // We've received a packet, read the data from it
              Udp.read(packetBuffer,NTP_PACKET_SIZE);  // read the packet into the buffer
          
              //the timestamp starts at byte 40 of the received packet and is four bytes,
              // or two words, long. First, esxtract the two words:
          
              unsigned long highWord = word(packetBuffer[40], packetBuffer[41]);
              unsigned long lowWord = word(packetBuffer[42], packetBuffer[43]);  
              // combine the four bytes (two words) into a long integer
              // this is NTP time (seconds since Jan 1 1900):
              unsigned long secsSince1900 = highWord << 16 | lowWord;  
              //Serial.print("Seconds since Jan 1 1900 = " );
              //Serial.println(secsSince1900);               
          
              // now convert NTP time into everyday time:
              //Serial.print("Unix time = ");
              // Unix time starts on Jan 1 1970. In seconds, that's 2208988800:
              const unsigned long seventyYears = 2208988800UL;     
              // subtract seventy years:
              unsigned long epoch = secsSince1900 - seventyYears;  
              // print Unix time:
              //Serial.println(epoch);                               
          
              unsigned long hours = ((epoch  % 86400L) / 3600) + timeZoneOffset ;
              unsigned long minutes = ((epoch  % 3600) / 60) + minuteOffset ;
             
              // print the hour, minute and/or second:
             
              client.println("Time :  "); // UTC is the time at Greenwich Meridian (GMT)
              client.print(hours); // print the hour (86400 equals secs per day)
              Serial.println(hours);
              client.print(':');  
              
              // In the first 10 minutes of each hour, we'll want a leading '0'
              if ( ((epoch % 3600) / 60) < 10 ) {                
                client.print('0');           
              }
              
              client.print(minutes); //print the minute (3600 equals secs per minute)
              Serial.print(minutes); // print the minute (3600 equals secs per minute)
              client.println();            
              /*
              client.print(':'); 
              if ( (epoch % 60) < 10 ) {
                // In the first 10 seconds of each minute, we'll want a leading '0'
                client.print('0');
              }
              client.println(epoch %60); // print the second
              */
            }
             if (timeZoneOffset > 0){
               client.print(" UTC +"); 
               client.println(timeZoneOffset); 
             }
             else if (timeZoneOffset == 0){
               client.print(" UTC "); 
               client.println(timeZoneOffset); 
             }
             else{
               client.print(" UTC "); 
               client.println(timeZoneOffset); 
            }
 /*
            if (hours > 20){ // Autoswitch On all leds at 8pm.
              digitalWrite(led, HIGH);
              digitalWrite(led2, HIGH);
              digitalWrite(led3, HIGH);
              digitalWrite(led4, HIGH);           
           }
*/

           
          // print Temperature
           client.println("<br />");  
           client.print("Temperature : ");
           client.print(steinhart);
           client.print("&deg;C");
           client.print("</H2>");

           // print buttons
           client.println("<hr />");
           client.println("<br />");  
           client.println("<a href=\"/button1on\"\">LED 1 ON</a>");
           client.println("<a href=\"/button1off\"\">LED 1 OFF</a><br />");   
           client.println("<br />"); 
           client.println("<a href=\"/button2on\"\"> LED 2 ON</a>");
           client.println("<a href=\"/button2off\"\">LED 2 OFF</a><br />");   
           client.println("<br />"); 
           client.println("<a href=\"/button3on\"\"> LED 3 ON</a>");
           client.println("<a href=\"/button3off\"\">LED 3 OFF</a><br />");   
           client.println("<br />"); 
           client.println("<a href=\"/button4on\"\"> LED 4 ON</a>");
           client.println("<a href=\"/button4off\"\">LED 4 OFF</a><br />"); 
           client.println("<br />");     
           client.println("<a href=\"/buttonson\"\">All on LED</a>");
           client.println("<a href=\"/buttonsoff\"\">All Off LED</a><br />"); 
           client.println("<br />");
           client.println("<hr />");          
          //client.print("<p>Created by Mpho Mphego. Visit http://mpho112.wordpress.com for more projects!</p>");  
          //client.println("<br />"); 
          
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
               digitalWrite(led, HIGH);
               digitalWrite(led2, HIGH);
               digitalWrite(led3, HIGH);
               digitalWrite(led4, HIGH);   
               Serial.print("All on"); 
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
    client.stop();
   Serial.println("client disonnected");
}
  // delay(1000);
}


// Do not edit code below
// send an NTP request to the time server at the given address 
unsigned long sendNTPpacket(IPAddress& address)
{

  // set all bytes in the buffer to 0
  memset(packetBuffer, 0, NTP_PACKET_SIZE); 
  // Initialize values needed to form NTP request
  // (see URL above for details on the packets)
  packetBuffer[0] = 0b11100011;   // LI, Version, Mode
  packetBuffer[1] = 0;     // Stratum, or type of clock
  packetBuffer[2] = 6;     // Polling Interval
  packetBuffer[3] = 0xEC;  // Peer Clock Precision
  // 8 bytes of zero for Root Delay & Root Dispersion
  packetBuffer[12]  = 49; 
  packetBuffer[13]  = 0x4E;
  packetBuffer[14]  = 49;
  packetBuffer[15]  = 52;

  // all NTP fields have been given values, now
  // you can send a packet requesting a timestamp: 		   
  Udp.beginPacket(address, 123); //NTP requests are to port 123
  Udp.write(packetBuffer,NTP_PACKET_SIZE);
  Udp.endPacket(); 
  
}


