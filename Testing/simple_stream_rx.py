import socket
import pygame

host="192.168.1.228"
port=1891

screen = pygame.display.set_mode((320,240))

while 1:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()
    message = []
    while True:
        d = conn.recv(1024*1024)
        if not d:
            s.close()
            break
        else: message.append(d)
    data = ''.join(message)
    image = pygame.image.fromstring(data,(320,240),"RGB")
    screen.blit(image,(0,0))
    pygame.display.update()
    s.close()
