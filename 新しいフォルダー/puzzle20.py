import pygame
import sys
import random

#現在deleteのぶぶんで虹色にしてから消そうとしているため、消すブロックを=4に変化させている。その都合で消そうとすると無限ループになる#

BLACK = (  0,  0,  0)
cnt = 0
s1 = 0
s2 = 0
t = 3
flag = 0
flaglist =[0,0,0]
stopflag = 0
rotflag = 0
flagr = 0#横キーを押した時のフラグ#
flagl = 0
rc_flag1 = 0
rc_flag2 = 0
rc_flag3 = 0
gameover = 0
waittmr = -25
stoptmr = 0
stoptmr = 0
posp1 = [188,100]#初期位置#
posp2 = [242,100]
posp3a = [242,46]
posp3b = [296,100]
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

ranlis = [ran1,ran2,ran3]
copy_posp1 = [posp1[0],posp1[1]]
copy_posp2 = [posp2[0],posp2[1]]
copy_posp3 = [posp3[0],posp3[1]]
copy_posn1 = posn1
copy_posn2 = posn2
copy_posn3 = posn3
poslis = [copy_posp1,copy_posp2,copy_posp3]
sabun = [posp2[0] - posp3[0],posp2[1] - posp3[1]]
puzzle = []
check = []
check2 = []
dcnt = []
auto_down_list = []
auto_down_speed = []
for i in range(8):
    puzzle.append([0,0,0,0,0,0,0,0])
    auto_down_list.append([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
    auto_down_speed.append([0,0,0,0,0,0,0,0])
for i in range(10):
    check.append([0,0,0,0,0,0,0,0,0,0])
    check2.append([0,0,0,0,0,0,0,0,0,0])
    dcnt.append([0,0,0,0,0,0,0,0,0,0])
img_bg = [
    pygame.image.load("../bg1.png"),
    pygame.image.load("../bg2.png"),
    pygame.image.load("../bg3.png")
    ]
img_blc = [
    pygame.image.load("../square_2.png"),
    pygame.image.load("../square_blue2.png"),
    pygame.image.load("../square_green2.png"),
    pygame.image.load("../square_red2.png"),
    pygame.image.load("../square_yellow2.png"),
    pygame.image.load("../square_rainbow2.png")
    ]
######################################################
def create_block1(bg,tmr):
    global flag,ran1,ran2,ran3,ran4,ran5,ran6,ran7,ran8,posp3,posn3,copy_posp1,copy_posp2,copy_posp3,copy_posn3,ranlis,poslis,sabun,waittmr,stopflag,cnt,auto_down_list
    if flag == 0:
        bg.fill(BLACK)
        bg.blit(img_bg[0],[20,148])
        bg.blit(img_bg[2],[480,0])
        for y in range(8):
            for x in range(8):
                bg.blit(img_blc[puzzle[y][x]],[26+54*x,154+54*y])
        bg.blit(img_blc[ran1],[copy_posp1[0],copy_posp1[1]])
        bg.blit(img_blc[ran2],[copy_posp2[0],copy_posp2[1]])
        bg.blit(img_blc[ran3],[copy_posp3[0],copy_posp3[1]])
        bg.blit(img_blc[ran4],[copy_posn1[0],copy_posn1[1]])
        bg.blit(img_blc[ran5],[copy_posn2[0],copy_posn2[1]])
        bg.blit(img_blc[ran6],[copy_posn3[0],copy_posn3[1]])
   
        if copy_posp1[1] + t < 154 + 54 * 7 and copy_posp2[1] + t < 154 + 54 * 7 and copy_posp3[1] + t < 154 + 54 * 7:
            copy_posp1[1] = copy_posp1[1]+t
            copy_posp2[1] = copy_posp2[1]+t
            copy_posp3[1] = copy_posp3[1]+t
            copy_posp1[0] = copy_posp1[0]+s1+s2
            copy_posp2[0] = copy_posp2[0]+s1+s2
            copy_posp3[0] = copy_posp3[0]+s1+s2
    if flag == 4:
        bg.fill(BLACK)
        bg.blit(img_bg[0],[20,148])
        bg.blit(img_bg[2],[480,0])
        bg.blit(img_blc[ran4],[copy_posn1[0],copy_posn1[1]])
        bg.blit(img_blc[ran5],[copy_posn2[0],copy_posn2[1]])
        bg.blit(img_blc[ran6],[copy_posn3[0],copy_posn3[1]])
        for y in range(7,-1,-1):
            for x in range(8):
                bg.blit(img_blc[puzzle[y][x]],[26+54*x,154+54*y])
                if auto_down_list[y][x][2] != 0:
                    bg.blit(img_blc[auto_down_list[y][x][2]],[auto_down_list[y][x][0],auto_down_list[y][x][1]])
                    auto_down_list[y][x][1] = auto_down_list[y][x][1] + auto_down_speed[y][x]
       
        
            
    if flag == 1:#ブロックが下まで行った時の処理。リストを更新、ブロックを新生#
        ran1=ran4
        ran2=ran5
        ran3=ran6
        ranlis = [ran1,ran2,ran3]
        ran7=ran8
        ran4=random.randint(1,4)
        ran5=random.randint(1,4)
        ran6=random.randint(1,4)
        ran8=random.randint(0,1)
        posp3 = ran7list[ran7]
        posn3 = ran8list[ran8]
        sabun = [posp2[0] - posp3[0],posp2[1] - posp3[1]]
        copy_posp1 = [posp1[0],posp1[1]]
        copy_posp2 = [posp2[0],posp2[1]]
        copy_posp3 = [posp3[0],posp3[1]]
        copy_posn3 = [posn3[0],posn3[1]]
        poslis = [copy_posp1,copy_posp2,copy_posp3]#ここで再定義しなおさないといけないのはリストが中身に変数を入れていた場合、その変数が変更されてもリストの変数は更新されないから#
        cnt = 0
        flag = 0
        stopflag = 0
###########################################################################################################################        
def move_block(key,tmr):
    global s1,s2,t,flagl,flagr,stoptmr
    #落下について#
    if stopflag == 0:
        if key[pygame.K_DOWN] == 1:
            t = 24#54未満じゃないとcheck_touch内の定義でバグる#
        else:
            t = 3
    
    #左右移動について#
    #fragr,lが1の時にstopflagが1になってしまうと、flagr=1のまま左右に動けなくなる#

        if flagr == 0 and flagl == 0:
            if key[pygame.K_RIGHT] == 1:
                flagr = 1
                stoptmr = tmr
                s1 = 27
            if key[pygame.K_LEFT] == 1:
                flagl = 1
                stoptmr = tmr
                s2 = -27
        elif flagr == 1 and flagl == 1:
             flagr = 0
             flagl = 0
             s1 = 0
             s2 = 0
        elif flagr == 1:
            if tmr >= stoptmr + 2:
                flagr = 0
                s1 = 0
        elif flagl == 1:  
            if tmr >= stoptmr + 2:
                flagl = 0
                s2 = 0
    if stopflag == 1:
        s1 = 0
        s2 = 0
        flagr = 0
        fragl = 0
    for i in range(3):
        if poslis[i][0] == 26 + 54 * 7:
            s1 = 0
        if poslis[i][0] == 26 + 54 * 0:
            s2 = 0
########################################################################################################################
def check_touch():
    global s1,s2,puzzle,gameover,flag,stopflag,copy_posp1,copy_posp2,copy_posp3,flaglist,auto_down_list,auto_down_speed
    #横の接地判定#
    for i in range(3):
        for y in range(8):
            for x in range(8):
                if poslis[i][0] == x * 54 + 26 and (y - 1) * 54 + 154   < poslis[i][1] + t <= y * 54 +154:
                    if x >= 1:
                        if puzzle[y][x - 1] != 0:
                            s2 = 0
                    if x <= 6:        
                        if puzzle[y][x + 1] != 0:
                            s1 = 0
    #縦の接地判定#
    if flag == 0 or flag ==1:
        for i in range(3):
            for y in range(7,-1,-1):
                for x in range(8):
                    localsabun11 = poslis[i][1] - copy_posp1[1]
                    localsabun21 = poslis[i][1] - copy_posp2[1]
                    localsabun31 = poslis[i][1] - copy_posp3[1]
                    localsabun10 = poslis[i][0] - copy_posp1[0]
                    localsabun20 = poslis[i][0] - copy_posp2[0]
                    localsabun30 = poslis[i][0] - copy_posp3[0]
                    if poslis[i][0] == x * 54 + 26 and poslis[i][1] + t >= 154 + 54 * 7:
                        poslis[0][1] = 7 * 54 + 154 - localsabun11
                        poslis[1][1] = 7 * 54 + 154 - localsabun21
                        poslis[2][1] = 7 * 54 + 154 - localsabun31
                        puzzle[7][x] = ranlis[i]
                        flag = 2
                    if poslis[i][0] == x * 54 + 26 and poslis[i][1]  <= (y - 1) * 54 + 154 < poslis[i][1] + t:
                        if  puzzle[y][x] != 0:
                            poslis[0][1] = (y - 1) * 54 + 154 - localsabun11
                            poslis[1][1] = (y - 1) * 54 + 154 - localsabun21
                            poslis[2][1] = (y - 1) * 54 + 154 - localsabun31
                        
                            if y >= 1:
                                puzzle[y-1][x] = ranlis[i]
                                stopflag = 1
                                flag = 2
                            if y == 0:
                                gameover = 1
                    if poslis[i][0] == x * 54 + 26 + 27 and poslis[i][1] + t >= 154 + 54 * 7:
                        poslis[0][1] = 7 * 54 + 154 - localsabun11
                        poslis[1][1] = 7 * 54 + 154 - localsabun21
                        poslis[2][1] = 7 * 54 + 154 - localsabun31
                        poslis[0][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun10
                        poslis[1][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun20
                        poslis[2][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun30
                        puzzle[7][x] = ranlis[i]
                        stopflag = 1
                        flag == 2
                    
                    
                    if poslis[i][0] == x * 54 + 26 + 27 and poslis[i][1]  <= (y - 1) * 54 + 154 < poslis[i][1] + t:
                        if  puzzle[y][x] != 0:
                            poslis[0][1] = (y - 1) * 54 + 154 - localsabun11
                            poslis[1][1] = (y - 1) * 54 + 154 - localsabun21
                            poslis[2][1] = (y - 1) * 54 + 154 - localsabun31
                            poslis[0][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun10
                            poslis[1][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun20
                            poslis[2][0] = x * 54 + 26 + 27 + s1 + s2 - localsabun30
                        
                            if y >= 1:
                                puzzle[y-1][x] = ranlis[i]
                                stopflag = 1
                                flag = 2
                            if y == 0:
                                gameover = 1
    if flag == 4: 
        for y in range(6,-1,-1):
            for x in range(8):    
                if auto_down_list[y][x][0] == x * 54 + 26 and auto_down_list[y][x][1] + auto_down_speed[y][x] >= 154 + 54 * (y+1) > auto_down_list[y][x][1]:
                    auto_down_list[y][x][1] = 154 + 54 * (y+1) #要らんかも#
                    puzzle[y+1][x] = auto_down_list[y][x][2]
                    auto_down_list[y][x] = [0,0,0]
                    auto_down_speed[y][x] = 0
                    flag = 3
                
                        
                        
                    
########################################################################################################################
def death_check():
    global gameover,flag
    if gameover == 1:
        for y in range(8):
            for x in range(8):
                puzzle[y][x] = 0
                auto_down_list[y][x] = [0,0,0]
                auto_down_speed[y][x] = 0
                gameover = 0
                flag = 1
########################################################################################################################                                                
def rotation(key,tmr):
    global cnt,copy_posp1,copy_posp3,stoptmr2,rotflag,rc_flag1,rc_flag2,rc_flag3
    rot = [[54,-54],[54,54],[-54,54],[-54,-54]]
    cntt = cnt + 1 + ran7
    if rotflag == 1:
        if tmr == stoptmr2 + 4:
            rotflag = 0
    if rc_flag1 == 1 and rc_flag2 == 1 and rc_flag3 == 1 and rotflag == 0:
        if key[pygame.K_2] == 1:
            copy_posp1[0] = copy_posp1[0] + rot[cnt % 4][0]
            copy_posp1[1] = copy_posp1[1] + rot[cnt % 4][1]
            copy_posp3[0] = copy_posp3[0] + rot[cntt % 4][0]
            copy_posp3[1] = copy_posp3[1] + rot[cntt % 4][1]
            cnt = cnt + 1
            stoptmr2 = tmr
            rotflag = 1
            rc_flag1 = 0
            rc_flag2 = 0
            rc_flag3 = 0
########################################################################################################################
def rotation_check():
    global rc_flag1,rc_flag2,rc_flag3
    rc_flag1 = 0
    rc_flag2 = 0
    rc_flag3 = 0
    rot = [[54,-54],[54,54],[-54,54],[-54,-54]]
    cntt = cnt + 1 + ran7
    if flagr == 0 and flagl == 0:
        rc_flag1 = 1
    for y in range(8):
        for x in range(8):
            if 54 * x + 26 == copy_posp1[0] + rot[cnt % 4][0] and 54 * (y - 1)+ 154 < copy_posp1[1] + rot[cnt % 4][1] + t <= 54 * y + 154:
                if puzzle[y][x] == 0 :
                    rc_flag2 = 1
                    
            if 54 * x + 26 == copy_posp3[0] + rot[cntt % 4][0] and 54 * (y - 1)+ 154 < copy_posp3[1] + rot[cntt % 4][1] + t <= 54 * y + 154:
                if puzzle[y][x] == 0 :
                    rc_flag3 = 1
    if copy_posp2[1] + t < 154:
        rc_flag2 = 1
        rc_flag3 = 1
#########################################################################################################################
def auto_down():#switchは自然落下ブロッが接地するまで消去フェーズに移行しないためのもの#
    global auto_down_list,auto_down_speed,puzzle,flag
    if flag == 2:
        for i in range(3):
            for y in range(8):
                for x in range(8):
                    if poslis[i][0] == 26 + x * 54 and poslis[i][1] == 154 + y * 54:
                        puzzle[y][x] = ranlis[i]
                        flag = 3
        
    if flag ==3:
        switch = 0
        for y in range(6,-1,-1):
            for x in range(8):
                if puzzle[y][x] != 0 and puzzle[y+1][x] == 0:
                    auto_down_list[y][x] = [26 + 54 * x,154 + 54 * y,puzzle[y][x]]#experiment_list2参照#
                    auto_down_speed[y][x] = 27
                    puzzle[y][x] = 0
                    switch = 1
                    flag = 4
                    
        if switch == 0:
            flag = 5
########################################################################################################################
def check_delete(y,x,dcnt):
    if check[y][x] != 0 and check[y+1][x] == check2[y][x]:
        check[y+1][x] = check2[y][x] + 5 #4色の場合。これを用いて消去エフェクトを作ると同時にカウントのダブりを予防#
        dcnt = dcnt + 1
        dcnt = check_delete(y+1,x,dcnt)
    if check[y][x] != 0 and check[y-1][x] == check2[y][x]:
        check[y-1][x] = check2[y][x] + 5
        dcnt = dcnt + 1
        dcnt = check_delete(y-1,x,dcnt)
    if check[y][x] != 0 and check[y][x+1] == check2[y][x]:
        check[y][x+1] = check2[y][x] + 5
        dcnt = dcnt + 1
        dcnt = check_delete(y,x+1,dcnt)
    if check[y][x] != 0 and check[y][x-1] == check2[y][x]:
        check[y][x-1] = check2[y][x] + 5
        dcnt = dcnt + 1
        dcnt = check_delete(y,x-1,dcnt)
    return(dcnt)
    
              
def delete(deletenum):#deletenumは何個くっつくと消えるかswitch2は消えるブロックがあるときまた自然落下に移行するためのもの#
    global flag
    if flag == 5:
        switch2 = 0
        for y in range(8):
            for x in range(8):
                check[y+1][x+1] = puzzle[y][x]
                check2[y+1][x+1] = puzzle[y][x]
        for y in range(1,9):
            for x in range(1,9):
                for i in range(1,9):
                    for j in range(1,9):
                        check[i][j] = check2[i][j]
                dcntneo = check_delete(y,x,dcnt[y][x])#checkdeleteのdcntはあくまで引数、その引数にリストのdcntを代入している#
                if dcntneo >= deletenum:
                    switch2 = 1
                    for y in range(1,9):
                        for x in range(1,9):
                            if check[y][x] >= 5:
                                puzzle[y-1][x-1] = 4
        flag = 3
        if switch2 == 0:
            flag = 1
           
########################################################################################################################        
def main():
    pygame.init()
    pygame.display.set_caption("きえる")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    mouse_c = 0

    tmr = 0
    while True:
        tmr = tmr + 1
        poslis = [copy_posp1,copy_posp2,copy_posp3]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        move_block(key,tmr)
        rotation_check()
        rotation(key,tmr)
        check_touch()
        auto_down()
        delete(4)
        create_block1(screen,tmr)
        death_check()
        pygame.display.update()
        clock.tick(20)
        


if __name__ == '__main__':
    main()


