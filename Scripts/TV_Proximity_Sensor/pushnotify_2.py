try:
    from pushbullet import Pushbullet
except ImportError:
    import pip
    pip.main(['install', 'pushbullet.py'])
finally:
    from pushbullet import Pushbullet

def send_pushbullet(api_key, alert, message):
    push_success = False
    try:
       pb = Pushbullet(api_key)
    except :
        return False
    else:
        push_success = pb.push_note(alert, message)['active']

    if push_success:
        return True
    else:
        return False
