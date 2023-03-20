import pygame
pygame.mixer.init() #Aqui estamos iniciando o mixer
pygame.init() #Aqui nós iniciamos o pygame, por algum motivo eu preciso iniciar o mixer primeiro.
pygame.mixer.music.load('musica.mp3') #aqui é a musica em si, estamos carregando-a
pygame.mixer.music.play()
pygame.event.wait() #Aqui estamos esperando a musica acabar para terminar o programa.

