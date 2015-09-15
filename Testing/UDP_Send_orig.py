try:
    import android
except:
    import androidhelper as android
import socket
# Android API Object SL4A Specific
droid = android.Android();

# Hostname or IP
hostname = "192.168.9.201";
# Port
port = 5005;
data = "";
# Creating a UDP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
# Connecting to Host (Usually not required since it is UDP)
s.connect((hostname,port));
print "Connected!";

exit = False;
while not exit:
#while True:
    # Using Android API for Google Voice and Recognizing command
    data = droid.recognizeSpeech().result;
    droid.ttsSpeak(data)
    droid.makeToast(data)
    #print data
    # Command is open or close proceding it to the Server else Error message
    if data == "1" or data == "one" or data == "2" or data == "two" :
        # Sending command
        print data
        s.sendto(data,(hostname,port));
        # Recieving an ACK since UDP is unreliable
        data = s.recvfrom(1024);
        print "Ack ", data[0];
        # If ACK is success ending the program
        if data[0] == "success":
            continue;

    else:
        exit = True;
        droid.ttsSpeak('Exiting program!')
        break;

    #else:
    #    print "Invalid Command";
