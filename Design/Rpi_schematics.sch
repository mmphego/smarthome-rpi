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
Date "10 nov 2015"
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
U 1 1 55BCDFD0
P 5000 4300
F 0 "#PWR?" H 5000 4300 30  0001 C CNN
F 1 "GND" H 5000 4230 30  0001 C CNN
F 2 "" H 5000 4300 60  0000 C CNN
F 3 "" H 5000 4300 60  0000 C CNN
	1    5000 4300
	1    0    0    -1  
$EndComp
Text GLabel 5150 2700 0    39   Output ~ 0
Door Bell LED
Text GLabel 6600 3000 2    39   Output ~ 0
Door Bell Button
Text GLabel 5150 2500 0    39   Output ~ 0
Coffermaker
$Comp
L +3,3V #PWR?
U 1 1 55F08746
P 5400 2100
F 0 "#PWR?" H 5400 2060 30  0001 C CNN
F 1 "+3,3V" H 5400 2210 30  0000 C CNN
F 2 "" H 5400 2100 60  0000 C CNN
F 3 "" H 5400 2100 60  0000 C CNN
	1    5400 2100
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 55F0876B
P 6350 2100
F 0 "#PWR?" H 6350 2190 20  0001 C CNN
F 1 "+5V" H 6350 2190 30  0000 C CNN
F 2 "" H 6350 2100 60  0000 C CNN
F 3 "" H 6350 2100 60  0000 C CNN
	1    6350 2100
	1    0    0    -1  
$EndComp
Text GLabel 6600 2700 2    39   Output ~ 0
Closet Door Button
$Comp
L CONN_4 P?
U 1 1 55F0916F
P 7450 4050
F 0 "P?" V 7400 4050 50  0000 C CNN
F 1 "Ultrasonic Door" V 7600 4050 50  0000 C CNN
F 2 "" H 7450 4050 60  0000 C CNN
F 3 "" H 7450 4050 60  0000 C CNN
	1    7450 4050
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 55F091B0
P 7050 3800
F 0 "#PWR?" H 7050 3890 20  0001 C CNN
F 1 "+5V" H 7050 3890 30  0000 C CNN
F 2 "" H 7050 3800 60  0000 C CNN
F 3 "" H 7050 3800 60  0000 C CNN
	1    7050 3800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55F091D1
P 7000 4300
F 0 "#PWR?" H 7000 4300 30  0001 C CNN
F 1 "GND" H 7000 4230 30  0001 C CNN
F 2 "" H 7000 4300 60  0000 C CNN
F 3 "" H 7000 4300 60  0000 C CNN
	1    7000 4300
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55F09299
P 6750 4100
F 0 "R?" V 6830 4100 40  0000 C CNN
F 1 "R" V 6757 4101 40  0000 C CNN
F 2 "~" V 6680 4100 30  0000 C CNN
F 3 "~" H 6750 4100 30  0000 C CNN
	1    6750 4100
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 55F092B3
P 6750 4200
F 0 "R?" V 6830 4200 40  0000 C CNN
F 1 "R" V 6757 4201 40  0000 C CNN
F 2 "~" V 6680 4200 30  0000 C CNN
F 3 "~" H 6750 4200 30  0000 C CNN
	1    6750 4200
	0    -1   -1   0   
$EndComp
$Comp
L CONN_4 P?
U 1 1 55F09595
P 7900 3450
F 0 "P?" V 7850 3450 50  0000 C CNN
F 1 "TV Proximity Sensor" V 8050 3450 50  0000 C CNN
F 2 "" H 7900 3450 60  0000 C CNN
F 3 "" H 7900 3450 60  0000 C CNN
	1    7900 3450
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 55F0959B
P 7500 3200
F 0 "#PWR?" H 7500 3290 20  0001 C CNN
F 1 "+5V" H 7500 3290 30  0000 C CNN
F 2 "" H 7500 3200 60  0000 C CNN
F 3 "" H 7500 3200 60  0000 C CNN
	1    7500 3200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55F095A3
P 7450 3700
F 0 "#PWR?" H 7450 3700 30  0001 C CNN
F 1 "GND" H 7450 3630 30  0001 C CNN
F 2 "" H 7450 3700 60  0000 C CNN
F 3 "" H 7450 3700 60  0000 C CNN
	1    7450 3700
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55F095AC
P 7200 3500
F 0 "R?" V 7280 3500 40  0000 C CNN
F 1 "R" V 7207 3501 40  0000 C CNN
F 2 "~" V 7130 3500 30  0000 C CNN
F 3 "~" H 7200 3500 30  0000 C CNN
	1    7200 3500
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 55F095B2
P 7200 3600
F 0 "R?" V 7280 3600 40  0000 C CNN
F 1 "R" V 7207 3601 40  0000 C CNN
F 2 "~" V 7130 3600 30  0000 C CNN
F 3 "~" H 7200 3600 30  0000 C CNN
	1    7200 3600
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR?
U 1 1 55F09674
P 6450 3800
F 0 "#PWR?" H 6450 3800 30  0001 C CNN
F 1 "GND" H 6450 3730 30  0001 C CNN
F 2 "" H 6450 3800 60  0000 C CNN
F 3 "" H 6450 3800 60  0000 C CNN
	1    6450 3800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55F096A8
P 5350 2600
F 0 "#PWR?" H 5350 2600 30  0001 C CNN
F 1 "GND" H 5350 2530 30  0001 C CNN
F 2 "" H 5350 2600 60  0000 C CNN
F 3 "" H 5350 2600 60  0000 C CNN
	1    5350 2600
	1    0    0    -1  
$EndComp
Text GLabel 5150 2300 0    39   Output ~ 0
Arduino SDA
Text GLabel 5150 2400 0    39   Output ~ 0
Arduino SCL
$Comp
L CONN_3 K?
U 1 1 5642521C
P 4350 3350
F 0 "K?" V 4300 3350 50  0000 C CNN
F 1 "IR" V 4400 3350 40  0000 C CNN
F 2 "" H 4350 3350 60  0000 C CNN
F 3 "" H 4350 3350 60  0000 C CNN
	1    4350 3350
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4700 4000 5500 4000
Wire Wire Line
	4700 4200 5000 4200
Wire Wire Line
	5000 4100 5500 4100
Wire Wire Line
	4700 3900 4850 3900
Wire Wire Line
	4850 3900 4850 3750
Wire Wire Line
	5500 2700 5150 2700
Wire Wire Line
	6600 3000 6300 3000
Wire Wire Line
	5150 2500 5500 2500
Wire Wire Line
	5400 2100 5400 2200
Wire Wire Line
	5400 2200 5500 2200
Wire Wire Line
	6350 2100 6350 2300
Wire Wire Line
	6350 2200 6300 2200
Wire Wire Line
	6350 2300 6300 2300
Connection ~ 6350 2200
Wire Wire Line
	6600 2700 6300 2700
Wire Wire Line
	7050 3800 7050 3900
Wire Wire Line
	7050 3900 7100 3900
Wire Wire Line
	7000 4300 7000 4200
Wire Wire Line
	7000 4200 7100 4200
Wire Wire Line
	7100 4000 6300 4000
Wire Wire Line
	7000 4100 7100 4100
Wire Wire Line
	6300 4100 6500 4100
Wire Wire Line
	6500 4200 6450 4200
Wire Wire Line
	6450 4200 6450 4100
Connection ~ 6450 4100
Wire Wire Line
	7500 3200 7500 3300
Wire Wire Line
	7500 3300 7550 3300
Wire Wire Line
	7450 3700 7450 3600
Wire Wire Line
	7450 3600 7550 3600
Wire Wire Line
	7550 3400 6750 3400
Wire Wire Line
	7450 3500 7550 3500
Connection ~ 6950 3600
Wire Wire Line
	6950 3500 6950 3900
Wire Wire Line
	6950 3900 6300 3900
Wire Wire Line
	6750 3400 6750 3700
Wire Wire Line
	6750 3700 6300 3700
Wire Wire Line
	6450 3800 6300 3800
Wire Wire Line
	5150 2400 5500 2400
Wire Wire Line
	5150 2300 5500 2300
Wire Wire Line
	5350 2600 5500 2600
Wire Wire Line
	4950 3900 5500 3900
Wire Wire Line
	4800 3250 4700 3250
Wire Wire Line
	4800 3050 4800 3250
Wire Wire Line
	4950 3900 4950 3450
Wire Wire Line
	4950 3450 4700 3450
Wire Wire Line
	4700 3350 5000 3350
$Comp
L +3.3V #PWR?
U 1 1 56425445
P 4800 3100
F 0 "#PWR?" H 4800 3060 30  0001 C CNN
F 1 "+3.3V" H 4800 3210 30  0000 C CNN
F 2 "" H 4800 3100 60  0000 C CNN
F 3 "" H 4800 3100 60  0000 C CNN
	1    4800 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3350 5000 4300
Connection ~ 5000 4200
Connection ~ 5000 4100
$EndSCHEMATC
