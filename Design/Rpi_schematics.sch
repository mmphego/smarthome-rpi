EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:Rpi_schematics-cache
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "9 sep 2015"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_4 P?
U 1 1 55BCDDBB
P 4350 4050
F 0 "P?" V 4300 4050 50  0000 C CNN
F 1 "DHT11" V 4400 4050 50  0000 C CNN
F 2 "" H 4350 4050 60  0000 C CNN
F 3 "" H 4350 4050 60  0000 C CNN
	1    4350 4050
	-1   0    0    -1  
$EndComp
$Comp
L BPLUS_GPIO PI?
U 1 1 55BCDEE0
P 6000 2950
F 0 "PI?" H 5900 3800 60  0000 C CNN
F 1 "BPLUS_GPIO" V 5900 2750 50  0000 C CNN
F 2 "~" H 5900 2750 60  0000 C CNN
F 3 "~" H 5900 2750 60  0000 C CNN
	1    6000 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 4000 5500 4000
$Comp
L +3.3V #PWR?
U 1 1 55BCDFAE
P 4850 3750
F 0 "#PWR?" H 4850 3710 30  0001 C CNN
F 1 "+3.3V" H 4850 3860 30  0000 C CNN
F 2 "" H 4850 3750 60  0000 C CNN
F 3 "" H 4850 3750 60  0000 C CNN
	1    4850 3750
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55BCDFC1
P 4750 4300
F 0 "#PWR?" H 4750 4300 30  0001 C CNN
F 1 "GND" H 4750 4230 30  0001 C CNN
F 2 "" H 4750 4300 60  0000 C CNN
F 3 "" H 4750 4300 60  0000 C CNN
	1    4750 4300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55BCDFD0
P 5450 4200
F 0 "#PWR?" H 5450 4200 30  0001 C CNN
F 1 "GND" H 5450 4130 30  0001 C CNN
F 2 "" H 5450 4200 60  0000 C CNN
F 3 "" H 5450 4200 60  0000 C CNN
	1    5450 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 4200 4750 4200
Wire Wire Line
	4750 4200 4750 4300
Wire Wire Line
	5500 4100 5450 4100
Wire Wire Line
	5450 4100 5450 4200
Wire Wire Line
	4700 3900 4850 3900
Wire Wire Line
	4850 3900 4850 3750
Text GLabel 5150 2700 0    39   Output ~ 0
Door Bell LED
Wire Wire Line
	5500 2700 5150 2700
Text GLabel 6600 3000 2    39   Output ~ 0
Door Bell Button
Wire Wire Line
	6600 3000 6300 3000
Text GLabel 5150 2500 0    39   Output ~ 0
Coffermaker
Wire Wire Line
	5150 2500 5500 2500
$EndSCHEMATC
