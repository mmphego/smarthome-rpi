import subprocess
import socket

def get_host():
    # find hostname/domain name
    host =  subprocess.Popen("echo `hostname`.`grep search /etc/resolv.conf | cut -f 2 -d ' '`",
        shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    return host

def get_ip():
    # find local IP
    loc_ip = ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close())
                for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    return loc_ip
