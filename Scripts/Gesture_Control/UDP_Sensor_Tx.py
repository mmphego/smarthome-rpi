try:
    # Android API Object SL4A Specific
    import android
except:
    import androidhelper as android
import time
import socket

droid = android.Android()

options = ["Gesture Control", "Voice Recognition"]
data = str()
ts = 100  # max sampling time 100ms
time_out = 0.5
Accelerometer = 2
port = 5005
nbytes = 1024

def radioButtonDialog(droid, question, options):
    droid.dialogCreateAlert(question)
    droid.dialogSetSingleChoiceItems(options)
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogSetNegativeButtonText("Cancel")
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    if "which" in response:
        result = response["which"]
    if result == "negative":
        raise Exception("Aborted")
    selectedItems = droid.dialogGetSelectedItems().result
    droid.dialogDismiss()
    return selectedItems.pop()

try:
    result = radioButtonDialog(droid, "Choose a gesture.", options)
except Exception:
    message = "Exiting application."

if options[result] == options[0]:

    try:
        droid.ttsSpeak("Please enter server's IP address")
        time.sleep(time_out)
        #hostname = "192.168.1.173"
        # TODO save IP to file and compare, if changed request user to input IP
        #with open('/sdcard/com.hipipal.qpyplus/scripts/ip.txt', 'w') as f:
            #Prev_IP = str(droid.dialogGetInput(title='IP Address').result)
            #f.write(Prev_IP)
        hostname = str(droid.dialogGetInput(title='IP Address').result)
        message = "Connecting to hostname:{}, port:{}".format(hostname, port)
        droid.makeToast(hostname)
    except Exception as e:
        droid.ttsSpeak('Failed to get IP address.')


    try:
        # Creating a UDP Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connecting to Host (Usually not required since it is UDP)
        s.connect((hostname, port))
        droid.makeToast("Connected to server!")
    except Exception as e:
        droid.ttsSpeak('Not connected to host due to {}!'.format(e))
        droid.makeToast('Failed: {}'.format(e))

    # start sensing Accelerometer at 100ms
    droid.startSensingTimed(Accelerometer, ts)
    exit = False
    while not exit:
        sensor_data = str(droid.sensorsReadAccelerometer().result)
        try:
            time.sleep(time_out)
            s.sendto(sensor_data, (hostname, port))
            s.settimeout(time_out)
        except Exception as e:
            droid.makeToast(' Could not connect to host, Error: {}'.format(e))
            droid.ttsSpeak('Failed to send data to host!')
            droid.stopSensing()
            exit = True

elif options[result] == options[1]:

    try:
        # TODO Add an IP checker, If it has changed ttsSpeak else use one from file
       # droid.ttsSpeak("Please enter server's IP address")
        time.sleep(time_out)
        hostname = "192.168.0.103"
        #hostname = str(droid.dialogGetInput(title='IP Address').result)
        message = "Connecting to hostname:{}, port:{}".format(hostname, port)
        droid.makeToast(hostname)
    except Exception as e:
        droid.ttsSpeak('Failed to get IP address.')

    try:
        # Creating a UDP Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connecting to Host (Usually not required since it is UDP)
        s.connect((hostname, port))
        droid.makeToast("Connected to server!")
    except Exception as e:
        droid.ttsSpeak('Not connected to host due to {}'.format(e))
        droid.makeToast('Failed: {}'.format(e))

    while True:
        # Using Android API for Google Voice and Recognizing command
        if data == '':
            droid.ttsSpeak('Speak now')
        data = droid.recognizeSpeech('Speak now', None, None)
        if data.error != None:
            pass
        else:
            data = str(data.result)
            droid.makeToast(data)
            if data == 'exit':
                droid.ttsSpeak('Exiting program, goodbye!')
                break
            else:
                s.sendto(data, (hostname, port))
                droid.ttsSpeak(data)

else:
    droid.makeToast("Aborted")
    raise Exception("Aborted")
