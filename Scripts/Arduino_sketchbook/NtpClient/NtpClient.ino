/*

 Udp NTP Client
 
 Get the time from a Network Time Protocol (NTP) time server
 Demonstrates use of UDP sendPacket and ReceivePacket 
 For more on NTP time servers and the messages needed to communicate with them, 
 see http://en.wikipedia.org/wiki/Network_Time_Protocol
 
 Warning: NTP Servers are subject to temporary failure or IP address change.
 Plese check 

    http://tf.nist.gov/tf-cgi/servers.cgi

 if the time server used in the example didn't work.

 */

#include <SPI.h>         
#include <Ethernet.h>
#include <EthernetUdp.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield

//byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };   //physical mac address
//byte ip[] = { 172, 18, 30, 197 };                      // ip in lan (that's what you need to use in your browser. ("192.168.1.178")
//byte gateway[] = { 172, 18, 30, 10 };                   // internet access via router
//byte subnet[] = { 255, 255, 255, 0 };                  //subnet mask
//EthernetServer server(80);                             //server port     


byte mac[] = {  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

unsigned int localPort = 8888;      // local port to listen for UDP packets
IPAddress ip(172,18,30,177);
IPAddress timeServer(172,18,30,100); // time-a.timefreq.bldrdoc.gov NTP server
// IPAddress timeServer(132, 163, 4, 102); // time-b.timefreq.bldrdoc.gov NTP server
// IPAddress timeServer(132, 163, 4, 103); // time-c.timefreq.bldrdoc.gov NTP server

const int NTP_PACKET_SIZE= 48; // NTP time stamp is in the first 48 bytes of the message

byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets 

// A UDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

/* Set this to the offset (in seconds) to your local time
   This example is GMT +3 */
const int timeZoneOffset = 3;
EthernetServer server(80);  

void setup() 
{
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  // start Ethernet and UDP
 /* if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // no point in carrying on, so do nothing forevermore:
    for(;;)
      ;
  }*/
  
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}


void loop()
{
  EthernetClient client = server.available();
  sendNTPpacket(timeServer); // send an NTP packet to a time server
  // wait to see if a reply is available
  delay(100); 
    if (client) {
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
	  client.println("Refresh: 30");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          
  //delay(50);  
 // delay(100);  
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


    // print the hour, minute and second:
   
    client.println("The Current Time is ");       // UTC is the time at Greenwich Meridian (GMT)
    client.print((epoch  % 86400L) / 3600 + timeZoneOffset); // print the hour (86400 equals secs per day)
    Serial.print((epoch  % 86400L) / 3600 + timeZoneOffset); // print the hour (86400 equals secs per day)
    client.print(':');  
    Serial.print(':');
    if ( ((epoch % 3600) / 60) < 10 ) {
      // In the first 10 minutes of each hour, we'll want a leading '0'
      client.print('0');
    }
    client.print((epoch  % 3600) / 60); // print the minute (3600 equals secs per minute)
    Serial.print((epoch  % 3600) / 60); // print the minute (3600 equals secs per minute)
    Serial.println();
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
        Serial.print("Timezone UTC +"); 
        Serial.println(timeZoneOffset); 
      }
      else if (timeZoneOffset == 0){
        Serial.print("Timezone UTC "); 
        Serial.println(timeZoneOffset); 
      }
      else{
        Serial.print("Timezone UTC "); 
        Serial.println(timeZoneOffset); 
      }
 

       //delay(500);
    
//  if (client) {
   // Serial.println("new client");
    // an http request ends with a blank line
/*    boolean currentLineIsBlank = true;
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
  */
          // output the value of each analog input pin
          //for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
          //  int sensorReading = analogRead(analogChannel);
           // client.print("analog input ");
            //client.print(analogChannel);
           // client.print(" is ");
            //client.print(sensorReading);
            //client.println("<br />");       
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
    delay(1);
    // close the connection:
    client.stop();
    //Serial.println("client disonnected");
  }
   delay(1000);
 
}




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










