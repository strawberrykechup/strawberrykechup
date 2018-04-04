import random
import pygame
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(1000, 3000))
pygame.time.set_timer(pygame.USEREVENT + 2, 20)
done = False
x = 300
y = 300
player_size = 15
font = pygame.font.Font(None,24)
mob = []

# init background
bgimg = pygame.image.load("bg.jpg")
ww, wh = pygame.display.get_surface().get_size()
bgimg = pygame.transform.scale(bgimg, (ww,wh))
bgsize = bgimg.get_rect()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == (pygame.USEREVENT + 1):
                        mxy = random.choice([[0, 0], [0, 700], [1100 ,0], [1100 ,700]])
                        msize = random.randint(player_size - 10, player_size + 30)
                        mob.append([mxy, msize])
                if event.type == (pygame.USEREVENT + 2):
                        for m in mob:
                                
                                if m[1] > player_size:
                                        if m[0][0] < x:
                                                m[0][0] += 1
                                        elif m[0][0] > x:
                                                m[0][0] -= 1
                                        if m[0][1] > y:
                                                m[0][1] -= 1
                                        elif m[0][1] < y:
                                                m[0][1] += 1
                                else:
                                        ra = random.randint(1,3)
                                        rb = random.randint(-1,1)
                                        if ra == 1:
                                                m[0][0] += rb
                                                m[0][1] += rb
                                        elif ra == 2:
                                                m[0][0] += rb
                                                m[0][1] += rb
                                        elif ra == 3:
                                                if m[0][0] < x:
                                                        m[0][0] += 1
                                                elif m[0][0] > x:
                                                        m[0][0] -= 1
                                                if m[0][1] > y:
                                                        m[0][1] -= 1
                                                elif m[0][1] < y:
                                                        m[0][1] += 1

                                if m[0][0] > (1200-m[1]):
                                        m[0][0] = 1200-m[1]
                                elif m[0][0] < 0:
                                        m[0][0] = 0
                                if m[0][1] > (800-m[1]):
                                        m[0][1] = 800-m[1]
                                elif m[0][1] < 0:
                                        m[0][1] = 0
                
        

        xy = 4
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
                y -= xy
                if y < 0:
                        y = 0
        if pressed[pygame.K_DOWN]: 
                y += xy
                if (y+player_size) > 800:
                        y = 800-player_size
        if pressed[pygame.K_LEFT]: 
                x -= xy
                if x < 0:
                        x = 0
        if pressed[pygame.K_RIGHT]: 
                x += xy
                if (x+player_size) > 1200:
                        x = 1200-player_size
        screen.blit(bgimg, bgsize)
        color = (221, 215, 19)
        
        player_rect = pygame.Rect(x,y,player_size,player_size)
        pygame.draw.rect(screen, color, player_rect)

        del_mob = []
        for m in mob:
                mob_rect = pygame.Rect(m[0][0], m[0][1], m[1], m[1])
                pygame.draw.rect(screen, (0, 0, 255), mob_rect)

                if mob_rect.colliderect(player_rect):
                        if m[1] > player_size:
                                print('game over')
                                time.sleep(3)
                                done = True
                        else:
                                player_size += m[1]//5
                                del_mob.append(m)

                        for dm in del_mob:
                                mob.remove(dm)
                else:
                        for om in mob:
                                if m!= om:
                                        omr = pygame.Rect(om[0][0], om[0][1], om[1], om[1])
                                        if mob_rect.colliderect(omr):
                                                del_mob.append(om)
                                                del_mob.append(m) 
                                                
        text = font.render('{0} score'.format(player_size*100), True, (66,75,244),(255,255,255))
        textrect = pygame.Rect(10, 10, 100, 100)
        screen.blit(text, textrect)
        for dm in del_mob:
                if dm in mob:
                        mob.remove(dm)
        pygame.display.flip()
        clock.tick(80)
         
        