 Import RPi.GPIO as GPIO
  import time




  GPIO.setwarnings (False)
  GPIO.setmode (GPIO.BCM)

  pin_in = 8
  GPIO.setup (pin_in, GPIO.IN) # GPIO8 (= Hardware Rest pin24) will be used to read the signal length Echo

  pin_out = 7 # GPIO7 (= Hardware Rest pin26) - generator Actuation
  Frequency = 20 # signal frequency
  Strida = 1 # signal will be 1% of the time in a logical "1" and 99% of the time in a logical "0"
  GPIO.setup (pin_out, GPIO.OUT) # GPIO output switches on
  SIGNAL1 = GPIO.PWM (pin_out, frequency) # setting pin to PWM output mode
  signal1.start (alternate)


  while True:
    total = 0
    for i in range (10) # 10 will Averaging Sample
       while GPIO.input (pin_in) == False: # until the output of "0" and waits ...
         time.sleep (0.00000001)
       time.time start = () # When you switch output to "1" to record the start time
       while GPIO.input (pin_in) == True: # again and waits until the output falls back to "0"
         time.sleep (0.00000001)
       cas = time.time () - start # at that moment to find out the difference between current and starting time
       sum + = total time of all time # 10 sample SCIT

  #for i in range(10): # prumerovani 10 vzorku
     #GPIO.wait_for_edge(pin_in, GPIO.RISING) # cekani na nabeznou hranu na GPIO vstupu
     #start= time.time() # zaznam casu startu
     #GPIO.wait_for_edge(pin_in, GPIO.FALLING) # cekani na sestupnou hranu na GPIO vstupu
     #cas= time.time() - start # vypocet delky impulzu
     #suma = suma + cas

  prumer = suma / 10 # vypocteni prumerneho casu z 10 vzorku
  print "Cas = " + str(prumer) + " ... tomu odpovida vzdalenost : " + str(int((prumer * 340 / 2) * 100)) + " cm"
  .
  .
  average = sum / 10 # Calculated average time of 10 sample
  print "Time =" + str (diameter) + "... it corresponds to the distance:" + str (int ((Diameter * 340/2) * 100)) + "cm"
  .
  .
  .

    average = sum / 10 # Calculated mean time
    print "Time =" + str (diameter) + "... it corresponds to the distance:" + str (int ((Diameter * 340/2) * 100)) + "cm"
    time.sleep (0.3)

 #Import RPi.GPIO as GPIO
  #import time




  #GPIO.setwarnings (False)
  #GPIO.setmode (GPIO.BCM)

  #pin_in = 8
  #GPIO.setup (pin_in, GPIO.IN) # GPIO8 (= Hardware Rest pin24) will be used to read the signal length Echo

  #pin_out = 7 # GPIO7 (= Hardware Rest pin26) - generator Actuation
  #Frequency = 20 # signal frequency
  #Strida = 1 # signal will be 1% of the time in a logical "1" and 99% of the time in a logical "0"
  #GPIO.setup (pin_out, GPIO.OUT) # GPIO output switches on
  #SIGNAL1 = GPIO.PWM (pin_out, frequency) # setting pin to PWM output mode
  #signal1.start (alternate)


  #while True:
    #total = 0
    #for i in range (10) # 10 will Averaging Sample
       #while GPIO.input (pin_in) == False: # until the output of "0" and waits ...
         #time.sleep (0.00000001)
       #time.time start = () # When you switch output to "1" to record the start time
       #while GPIO.input (pin_in) == True: # again and waits until the output falls back to "0"
         #time.sleep (0.00000001)
       #cas = time.time () - start # at that moment to find out the difference between current and starting time
       #sum + = total time of all time # 10 sample SCIT


    #average = sum / 10 # Calculated mean time
    #print "Time =" + str (diameter) + "... it corresponds to the distance:" + str (int ((Diameter * 340/2) * 100)) + "cm"
    #time.sleep (0.3)
