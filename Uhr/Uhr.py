import pygame
import math
from datetime import datetime
import time

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
analog = True
continous = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                analog = True
            if event.key == pygame.K_d:
                analog = False
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_p:
                continous = not continous

    now = datetime.now()
    s =  now.second
    m = now.minute
    hour = now.hour
    w, h = pygame.display.get_surface().get_size()
    if analog == True:

        screen.fill((0,0,0))
        pygame.draw.ellipse(screen, (255, 80, 0), pygame.Rect(w * 0.09, h * 0.09, w * 0.82, h * 0.82))
        pygame.draw.ellipse(screen, (100, 50, 0), pygame.Rect(w * 0.10, h * 0.10, w * 0.80, h * 0.80))
        pygame.draw.ellipse(screen, (20, 20, 20), pygame.Rect(w * 0.15, h * 0.15, w * 0.70, h * 0.70))
        for i in range(1,13):
            font = pygame.font.SysFont(None, 72)
            text = font.render(str(i), True, (255, 80, 0))
            screen.blit(text,(w/2+math.cos(-1*i*2*math.pi/12+math.pi/2)*w*0.46-text.get_width()/2,w/2-math.sin(-1*i*2*math.pi/12+math.pi/2)*h*0.46-text.get_height()/2))

        if continous == True:
            s = now.microsecond / 1000000
            s = (now.second + s)

        #Zeitzeiger
        pygame.draw.line(screen,(255,80,0),[w/2,h/2],[math.cos(s*2*math.pi/60-math.pi/2)*w*0.35+w/2,math.sin(s*2*math.pi/60-math.pi/2)*h*0.35+h/2],1)
        pygame.draw.line(screen, (200,60,0), [w / 2, h / 2],
                         [math.cos(m*2*math.pi/60-math.pi/2) * w * 0.25 + w / 2, math.sin(m*2*math.pi/60-math.pi/2) * h * 0.25 + h / 2],3)
        pygame.draw.line(screen,(100,40,0), [w / 2, h / 2],
                         [math.cos(hour*2*math.pi/12-math.pi/2) * w * 0.15 + w / 2, math.sin(hour *2*math.pi/12-math.pi/2) * h * 0.15 + h / 2],5)

        pygame.display.flip()
    else:
        if s < 10:
            s = "0"+str(s)
        if m < 10:
            m = "0" + str(m)
        if hour < 10:
            hour = "0"+str(hour)

        pygame.font.init()
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 72)
        text = font.render(str(hour)+":"+str(m)+":"+str(s), True, (255, 80, 0))
        pygame.draw.rect(screen, (255, 80, 0),
                         pygame.Rect(w / 2 - text.get_width() * 1.3 / 2, h / 2 - text.get_height() * 1.3 / 2,
                                     text.get_width() * 1.3, text.get_height() * 1.3))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(w/2-text.get_width()*1.2/2, h/2-text.get_height()*1.2/2,text.get_width()*1.2, text.get_height()*1.2))
        #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(w/2-text.get_width()/2,h/2-text.get_height()/2),text.get_width(),text.get_height()))
        screen.blit(text,(w/2-text.get_width()/2,h/2 -text.get_height()/2))
        pygame.display.flip()

