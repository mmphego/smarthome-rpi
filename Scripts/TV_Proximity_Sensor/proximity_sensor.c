#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>


#define TRIG 28
#define ECHO 29

void setup() {
        wiringPiSetup();
        pinMode(TRIG, OUTPUT);
        pinMode(ECHO, INPUT);

        //TRIG pin must start LOW
        digitalWrite(TRIG, LOW);
        delay(30);
}

int getCM() {
        //Send trig pulse
        digitalWrite(TRIG, HIGH);
        delayMicroseconds(10);
        digitalWrite(TRIG, LOW);

        //Wait for echo start
        while(digitalRead(ECHO) == LOW);
        //Wait for echo end
        float startTime = micros();

        while(digitalRead(ECHO) == HIGH);
        float travelTime = micros() - startTime;
        //Get distance in cm
        //int distance = travelTime / 58;
        float distance = travelTime / 57.9995;

        printf ("%f", distance);
        return distance;
}

int main(void) {
        setup();
        delay(0.5);
        getCM();
        delay(0.5);
        return 0;
}
