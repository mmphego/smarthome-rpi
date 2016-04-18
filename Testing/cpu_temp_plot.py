import os
#import matplotlib.pyplot as plt
#from drawnow import *

#tempC = []

#plt.ion()
#cnt=0

#def plotTempC():
    #plt.ylim(20,80)
    #plt.title('Raspberry Pi core temperture')
    #plt.grid(True)
    #plt.ylabel('Temp C')
    #plt.plot(tempC, 'rx-', label='Degrees C')
    #plt.legend(loc='upper right')
    #plt.savefig('test.png')

##pre-load dummy data
#for i in range(0,26):
    #tempC.append(0)

##while True:

ostemp = os.popen('vcgencmd measure_temp').readline()
temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
print(temp)
#tempC.append(temp)
#tempC.pop(0)
##drawnow(plotTempC)
#plotTempC()
#plt.pause(.5)
