#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main (void) {
  int c,x,re[1000],med=0;
  int NUMREADINGS=50;
  printf ("Raspberry Pi wiringPi Capacitor reading \n") ;

  if (wiringPiSetup () == -1)
    exit (1) ;

for (;;) {

  for (x=0;x<NUMREADINGS;x++) {
      pinMode (27, OUTPUT);
      digitalWrite (27, LOW);
      delay(16);
      c=0;
      pinMode (27, INPUT);
      while (digitalRead(27)==LOW)
        c++;
      re[x]=c;
    }
    med=0;
    for (x=0;x<NUMREADINGS;x++)
      med+=re[x];
    printf("%d\n",med/NUMREADINGS);
}
}
