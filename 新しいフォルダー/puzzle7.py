import pygame
import sys
import random

BLACK = (  0,  0,  0)

mouse_c = 0
s1 = 0
s2 = 0
t = 1
flag = 0
posp1 = [187,100]#初期位置#
posp2 = [241,100]
posp3a = [241,46]
posp3b = [295,100]
posn1 = [563,138]
posn2 = [617,138]
posn3a = [617,84]
posn3b = [671,138]
ran1 = random.randint(1,4)
ran2 = random.randint(1,4)
ran3 = random.randint(1,4)
ran4 = random.randint(1,4)
ran5 = random.randint(1,4)
ran6 = random.randint(1,4)
ran7 = random.randint(0,1)
ran8 = random.randint(0,1)
ran7list = [posp3a,posp3b]
ran8list = [posn3a,posn3b]
posp3 = ran7list[ran7]
posn3 = ran8list[ran8]
copy_posp1 = posp1
copy_posp2 = posp2
copy_posp3 = posp3
copy_posn1 = posn1
copy_posn2 = posn2
copy_posn3 = posn3

img_bg = [
    pygame.image.load("bg1.png"),
    pygame.image.load("bg2.png"),
    pygame.image.load("bg3.png")
]
img_blc = [
    None,
    pygame.image.load("square_blue1.png"),
    pygame.image.load("square_green1.png"),
    pygame.image.load("square_red1.png"),
    pygame.image.load("square_yellow1.png")
    ]    
def create_block1(bg):
    global flag,ran1,ran2,ran3,ran4,ran5,ran6,ran7,ran8,posp3,posn3,copy_posp1,copy_posp2,copy_posp3
    if flag == 0:
        bg.fill(BLACK)
        bg.blit(img_bg[0],[20,148])
        bg.blit(img_bg[2],[480,0])
        bg.blit(img_blc[ran1],[copy_posp1[0],copy_posp1[1]])
        bg.blit(img_blc[ran2],[copy_posp2[0],copy_posp2[1]])
        bg.blit(img_blc[ran3],[copy_posp3[0],copy_posp3[1]])
        bg.blit(img_blc[ran4],[copy_posn1[0],copy_posn1[1]])
        bg.blit(img_blc[ran5],[copy_posn2[0],copy_posn2[1]])
        bg.blit(img_blc[ran6],[copy_posn3[0],copy_posn3[1]])
        copy_posp1[1] = copy_posp1[1]+t
        copy_posp2[1] = copy_posp2[1]+t
        copy_posp3[1] = copy_posp3[1]+t
        copy_posp1[0] = copy_posp1[0]+s1+s2
        copy_posp2[0] = copy_posp2[0]+s1+s2
        copy_posp3[0] = copy_posp3[0]+s1+s2
       
        flag = 0
    if flag == 1:#ブロックを新生#
        ran1=ran4
        ran2=ran5
        ran3=ran6
        ran7=ran8
        ran4=random.randint(1,4)
        ran5=random.randint(1,4)
        ran6=random.randint(1,4)
        ran8=random.randint(0,1)
        posp3 = ran7list[ran7]
        posn3 = ran8list[ran8]
        flag = 0
        
def move_block(key):
    global s1,s2,t
    if key[pygame.K_RIGHT] == 1:
        s1 = 4
    else:
        s1 = 0
    if key[pygame.K_DOWN] == 1:
        t = 6
    else:
        t = 1
    if key[pygame.K_LEFT] == 1:
        s2 = -4
    else:
        s2 = 0
    
def main():
    pygame.init()
    pygame.display.set_caption("ランダムでブロックが出現するやつpart2")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    tmr = 0
    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        move_block(key)
        create_block1(screen)
        pygame.display.update()
        clock.tick(20)
            

if __name__ == '__main__':
    main()

