import os
try:
    from pushbullet import Pushbullet
except ImportError:
    import pip
    pip.main(['install', 'pushbullet.py'])
finally:
    from pushbullet import Pushbullet
    from yamlConfigFile import configFile

image_path ='/home/pi/Scripts/Smart_DoorBell/image.jpg'
def send_pushbullet(alert, message):
    api_key = configFile()['PushNotifications']['Pushbullet']
    push_success = False
    try:
       pb = Pushbullet(api_key)
    except :
        LOGGER.error ('Unable to connect to pushover server')
        raise RuntimeError ('Unable to connect to pushover server')
    else:
        #if os.path.exists(image_path):
            #with open(image_path, "rb") as pic:
                #file_data = pb.upload_file(pic, "picture.jpg")
            #push_success = pb.push_file(**file_data)['active']
        #else:
        push_success = pb.push_note(alert, message)['active']

    if push_success:
        return True
    else:
        return False
