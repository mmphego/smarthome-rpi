#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main (void) {
  int pin,c;

  printf ("Raspberry Pi wiringPi Capacitor reading \n") ;

  if (wiringPiSetup () == -1)
    exit (1) ;

  for (pin = 0 ; pin < 8 ; ++pin) {
    pinMode (pin, OUTPUT) ;
    digitalWrite (pin, LOW) ;
  }

for (;;) {
  pinMode (1, OUTPUT);
  digitalWrite (1, LOW);
  delay(50);
  c=0;
  pinMode (1, INPUT);
  while (digitalRead(1)==LOW)
    c++;
  printf("%d\n",c);
  delay(100);
}                         

}
