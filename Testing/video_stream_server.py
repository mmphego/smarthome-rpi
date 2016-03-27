import socket,os
from PIL import *
import pygame,sys
import pygame.camera
from pygame.locals import *

# http://s9.zetaboards.com/Ultimate3D_community/topic/7224981/1/
#Create server:
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.SOCK_STREAM)
server.bind(("192.168.9.229",5000))
server.listen(5)

#Start Pygame
pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((320,240))

cam = pygame.camera.Camera("/dev/video0",(320,240),"RGB")
cam.start()


#Send data
while True:
    s,add = server.accept()
    print "Connected from",add
    print s
    image = cam.get_image()
    screen.blit(image,(0,0))
    data = cam.get_raw()
    try:
        print len(data)
        s.sendall(data)
        pygame.display.update()
    except:
        import IPython;IPython.embed()

#Interupt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
