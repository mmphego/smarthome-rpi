import socket,sys
import pygame
from PIL import Image

#Create a var for storing an IP address:
ip = "192.168.0.104"

#Start PyGame:
pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.display.set_caption('Remote Webcam Viewer')
font = pygame.font.SysFont("Arial",14)
clock = pygame.time.Clock()
timer = 0
previousImage = ""
image = ""

#Main program loop:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#Receive data
    if timer < 1:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((str(ip),5000))
        data = client_socket.recv(1024000)
        timer = 30

    else:
        timer -= 1
    previousImage = image

#Convert image
    try:
        # image = Image.fromstring("RGB",(120,90),data)
        image = Image.fromstring("RGB",(320,240),data)
        # image = image.resize((320,240))
        image = pygame.image.frombuffer(image.tostring(),(320,240),"RGB")

    #Interupt
    except:
        image = previousImage
        output = image
        screen.blit(output,(0,0))
        clock.tick(60)
        pygame.display.flip()
