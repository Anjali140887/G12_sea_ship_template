import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=500
height=400
screen = pygame.display.set_mode((width,height))

#load images


#variable to hold x-axis value of background image


while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #decrement bgx to move the background
    
    # Add code to reset bgx to 0 after bgx becomes less then -1000
    
    
    #display the background and ship image

    
   
    pygame.display.update()
    clock.tick(30)
