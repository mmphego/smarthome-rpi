try:
    # Android API Object SL4A Specific
    import android
except:
    import androidhelper as android
import time
import socket

droid = android.Android()

try:
    # TODO Add an IP checker, If it has changed ttsSpeak else use one from file
    droid.ttsSpeak("Please enter server's IP address")
    time.sleep(.5)
    # hostname = "192.168.1.173"
    hostname = str(droid.dialogGetInput(title='IP Address').result)
    port = 5005
    message = "Connecting to hostname:{}, port:{}".format(hostname, port)
    droid.makeToast(hostname)
except Exception as e:
    droid.ttsSpeak('Failed to get IP address.')

data = str()
exit = False

def socket_data():
    # Sending command
    print data
    s.sendto(data, (hostname, port))
    # Receiving an ACK since UDP is unreliable
    data = s.recvfrom(1024)
    # print "Ack ", data[0];
    # If ACK is success ending the program
    # if data[0] == "success":
    #     continue
    return data

while not exit:
    # Using Android API for Google Voice and Recognizing command
    data = droid.recognizeSpeech().result
    time.sleep(.25)
    droid.ttsSpeak(data)
    droid.makeToast(data)
    # print data
    # Command is open or close proceeding it to the Server else Error message
    if data == "kitchen on" or data ==  "kitchen off":
        socket_data()
    elif data == "dining on" or data == "dining off":
        socket_data()

    elif data == "bedroom on" or data == "bedroom off":
        socket_data()

    elif data == "tv room on" or data == "tv room off":
        socket_data()

    elif data == "everything on" or data == "everything off":
        socket_data()

    elif data == 'exit' or data == 'quit' or data == 'bye':
        exit = True
        droid.ttsSpeak('Exiting Application!')
        break

    else:
        droid.makeToast('Invalid Command')
        print 'Invalid Command'
