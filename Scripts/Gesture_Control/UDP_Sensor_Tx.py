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

hostname = '255.255.255.255'
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

try:
    # Creating a UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    droid.makeToast("Connected to server!")
except Exception as e:
    droid.ttsSpeak('Not connected to host due to {}!'.format(e))

if options[result] == options[0]:

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
        message = "Connecting to hostname:{}, port:{}".format(hostname, port)
    except Exception as e:
        droid.ttsSpeak('Failed to get IP address.')

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
