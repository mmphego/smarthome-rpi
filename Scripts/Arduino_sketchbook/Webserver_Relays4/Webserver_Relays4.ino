/*

 Arduino with Ethernet Shield
 */

#include <SPI.h>
#include <Ethernet.h>
int led = 2, led2 = 3, led3 = 5, led4 = 6;
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };   //physical mac address
byte ip[] = { 172, 18, 30, 197 };                      // ip in lan (that's what you need to use in your browser. ("192.168.1.178")
byte gateway[] = { 172, 18, 30, 10 };                   // internet access via router
byte subnet[] = { 255, 255, 255, 0 };                  //subnet mask
EthernetServer server(80);                             //server port     
String readString;

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

  // Create a client connection
  EthernetClient client = server.available();
  if (client) {
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
         if (c == '\n') {          
           Serial.println(readString); //print to serial monitor for debuging
     
           client.println("HTTP/1.1 200 OK"); //send new page
           client.println("Content-Type: text/html");
           client.println();    
           client.println("Connection: close");  // the connection will be closed after completion of the response
	   client.println("Refresh: 5");  // refresh the page automatically every 5 sec
           client.println();
           client.println("<!DOCTYPE HTML>"); 
           client.println("<HTML>");
           client.println("<CENTER><HEAD>");
           client.println("<TITLE>Simple Home Automation</TITLE>");
           client.println("</HEAD>");
           client.println("<BODY>");
           client.println("<H1>Simple Home Automation</H1>");
           client.println("<hr />");
           client.println("<br />");  
           client.println("<H2>Arduino with Ethernet Shield</H2>");
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

