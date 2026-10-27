import pygame

pygame.init()  


ecran = pygame.display.set_mode((640, 480))
pygame.display.set_caption("NeuroPac test")


horloge = pygame.time.Clock()

en_cours = True
while en_cours:
    
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:  
            en_cours = False

    ecran.fill((0, 0, 0))                                      
    pygame.draw.circle(ecran, (255, 255, 0), (320, 240), 30)   
    pygame.display.flip()                                      
    horloge.tick(60)                                           

pygame.quit() 