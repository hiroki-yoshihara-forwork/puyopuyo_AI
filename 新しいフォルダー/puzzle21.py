import pygame
import time
import sys
import random

"""
やるべきこと
現在のブロックを28通りの置き方をした時のpuzzleのリストを作る
""" 
#クラス化#
class Puyomodoki():
    def __init__(self):
        self.BLACK = (  0,  0,  0)
        self.cnt = 0
        self.s1 = 0
        self.s2 = 0
        self.t = 3
        """
        self.flag = 0 通常の動かせる状態
        self.falg = 1 ブロックが新しく作られる状態
        self.flag = 2 接地判定に引っかかった状態
        self.flag = 3 接地判定を受けて、ブロックがpuzzleに加えられた状態 → 4,5
        self.flag = 4 下が空きマスのブロックがいる際に突入し、自動落下状態となる。 → 2
        self.flag = 5 消去判定に入るフェーズ。
        self.flag = 6 一定フレーム消去ブロックを虹色にしてから消去するフェーズ。
        """
        self.flag = 0
        self.flaglist =[0,0,0]
        self.stopflag = 0
        self.rotflag = 0
        self.flagr = 0#横キーを押した時のフラグ#
        self.flagl = 0
        self.rc_flag1 = 0
        self.rc_flag2 = 0
        self.rc_flag3 = 0
        self.gameover = 0
        self.waittmr = -25
        self.stoptmr = 0
        self.delete_tmr = 0
        self.restart_tmr = 0
        self.posp1 = [188,100]#初期位置#
        self.posp2 = [242,100]
        self.posp3a = [242,46]
        self.posp3b = [296,100]
        self.posn1 = [563,138]
        self.posn2 = [617,138]
        self.posn3a = [617,84]
        self.posn3b = [671,138]
        self.ran1 = random.randint(1,4)
        self.ran2 = random.randint(1,4)
        self.ran3 = random.randint(1,4)
        self.ran4 = random.randint(1,4)
        self.ran5 = random.randint(1,4)
        self.ran6 = random.randint(1,4)
        self.ran7 = random.randint(0,1)
        self.ran8 = random.randint(0,1)
        self.ran7list = [self.posp3a,self.posp3b]
        self.ran8list = [self.posn3a,self.posn3b]
        self.posp3 = self.ran7list[self.ran7]
        self.posn3 = self.ran8list[self.ran8]

        self.ranlis = [self.ran1,self.ran2,self.ran3]
        self.copy_posp1 = [self.posp1[0],self.posp1[1]]
        self.copy_posp2 = [self.posp2[0],self.posp2[1]]
        self.copy_posp3 = [self.posp3[0],self.posp3[1]]
        self.copy_posn1 = self.posn1
        self.copy_posn2 = self.posn2
        self.copy_posn3 = self.posn3
        self.poslis = [self.copy_posp1,self.copy_posp2,self.copy_posp3]
        self.sabun = [self.posp2[0] - self.posp3[0],self.posp2[1] - self.posp3[1]]
        self.puzzle = []
        self.check = []
        self.check2 = []
        self.dcnt = []
        self.auto_down_list = []
        self.auto_down_speed = []
        for i in range(8):
            self.puzzle.append([0,0,0,0,0,0,0,0])
            self.auto_down_list.append([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
            self.auto_down_speed.append([0,0,0,0,0,0,0,0])
        for i in range(10):
            self.check.append([0,0,0,0,0,0,0,0,0,0])
            self.check2.append([0,0,0,0,0,0,0,0,0,0])
            self.dcnt.append([0,0,0,0,0,0,0,0,0,0])
        self.img_bg = [
            pygame.image.load("../bg1.png"),
            pygame.image.load("../bg2.png"),
            pygame.image.load("../bg3.png")
            ]
        self.img_blc = [
            pygame.image.load("../square_2.png"),
            pygame.image.load("../square_blue2.png"),
            pygame.image.load("../square_green2.png"),
            pygame.image.load("../square_red2.png"),
            pygame.image.load("../square_yellow2.png"),
            pygame.image.load("../square_rainbow2.png")
            ]
        self.ai_down = False
        self.ai_left = False
        self.ai_right = False
        self.ai_turnRight = False
        self.ai_turnLeft = False
        self.ai_cnt = 0#self.flag=1になったら0にして、マイフレームごとに+1
        self.ai_automode = True
        self.ai_cycleStart = True#ブロックが地面についてブロックを新生したところをサイクルのはじめとして起動する
        self.ai_autofirst = True
        self.ai_decisionNum = 0
        """
        0なにもしない
        1down
        2left 2フレ
        3right 2フレ
        4turnright 4フレ
        """
        self.ai_action00 = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action01 = [0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action02 = [0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action03 = [0,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action04 = [0,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action05 = [0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action06 = [0,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        self.ai_action10 = [0,4,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action11 = [0,4,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action12 = [0,4,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action13 = [0,4,0,0,0,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action14 = [0,4,0,0,0,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action15 = [0,4,0,0,0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action16 = [0,4,0,0,0,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        self.ai_action20 = [0,4,0,0,0,4,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action21 = [0,4,0,0,0,4,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action22 = [0,4,0,0,0,4,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action23 = [0,4,0,0,0,4,0,0,0,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action24 = [0,4,0,0,0,4,0,0,0,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action25 = [0,4,0,0,0,4,0,0,0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action26 = [0,4,0,0,0,4,0,0,0,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        self.ai_action30 = [0,4,0,0,0,4,0,0,0,4,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action31 = [0,4,0,0,0,4,0,0,0,4,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action32 = [0,4,0,0,0,4,0,0,0,4,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action33 = [0,4,0,0,0,4,0,0,0,4,0,0,0,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action34 = [0,4,0,0,0,4,0,0,0,4,0,0,0,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action35 = [0,4,0,0,0,4,0,0,0,4,0,0,0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_action36 = [0,4,0,0,0,4,0,0,0,4,0,0,0,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.ai_actionList = [
            self.ai_action00,
            self.ai_action01,
            self.ai_action02,
            self.ai_action03,
            self.ai_action04,
            self.ai_action05,
            self.ai_action06,
            self.ai_action10,
            self.ai_action11,
            self.ai_action12,
            self.ai_action13,
            self.ai_action14,
            self.ai_action15,
            self.ai_action16,
            self.ai_action20,
            self.ai_action21,
            self.ai_action22,
            self.ai_action23,
            self.ai_action24,
            self.ai_action25,
            self.ai_action26,
            self.ai_action30,
            self.ai_action31,
            self.ai_action32,
            self.ai_action33,
            self.ai_action34,
            self.ai_action35,
            self.ai_action36,
        ]
        self.main()
    ######################################################
    def create_block1(self,bg,tmr):
        print("create_block")
        if self.flag == 0:
            bg.fill(self.BLACK)
            bg.blit(self.img_bg[0],[20,148])
            bg.blit(self.img_bg[2],[480,0])
            for y in range(8):
                for x in range(8):
                    bg.blit(self.img_blc[self.puzzle[y][x]],[26+54*x,154+54*y])
            bg.blit(self.img_blc[self.ran1],[self.copy_posp1[0],self.copy_posp1[1]])
            bg.blit(self.img_blc[self.ran2],[self.copy_posp2[0],self.copy_posp2[1]])
            bg.blit(self.img_blc[self.ran3],[self.copy_posp3[0],self.copy_posp3[1]])
            bg.blit(self.img_blc[self.ran4],[self.copy_posn1[0],self.copy_posn1[1]])
            bg.blit(self.img_blc[self.ran5],[self.copy_posn2[0],self.copy_posn2[1]])
            bg.blit(self.img_blc[self.ran6],[self.copy_posn3[0],self.copy_posn3[1]])
   
            if self.copy_posp1[1] + self.t < 154 + 54 * 7 and self.copy_posp2[1] + self.t < 154 + 54 * 7 and self.copy_posp3[1] + self.t < 154 + 54 * 7:
                self.copy_posp1[1] = self.copy_posp1[1]+self.t
                self.copy_posp2[1] = self.copy_posp2[1]+self.t
                self.copy_posp3[1] = self.copy_posp3[1]+self.t
                self.copy_posp1[0] = self.copy_posp1[0]+self.s1+self.s2
                self.copy_posp2[0] = self.copy_posp2[0]+self.s1+self.s2
                self.copy_posp3[0] = self.copy_posp3[0]+self.s1+self.s2
        if self.flag == 4:
            bg.fill(self.BLACK)
            bg.blit(self.img_bg[0],[20,148])
            bg.blit(self.img_bg[2],[480,0])
            bg.blit(self.img_blc[self.ran4],[self.copy_posn1[0],self.copy_posn1[1]])
            bg.blit(self.img_blc[self.ran5],[self.copy_posn2[0],self.copy_posn2[1]])
            bg.blit(self.img_blc[self.ran6],[self.copy_posn3[0],self.copy_posn3[1]])
            for y in range(7,-1,-1):
                for x in range(8):
                    bg.blit(self.img_blc[self.puzzle[y][x]],[26+54*x,154+54*y])
                    if self.auto_down_list[y][x][2] != 0:
                        bg.blit(self.img_blc[self.auto_down_list[y][x][2]],[self.auto_down_list[y][x][0],self.auto_down_list[y][x][1]])
                        self.auto_down_list[y][x][1] = self.auto_down_list[y][x][1] + self.auto_down_speed[y][x]
       
        
        if self.flag == 6:#ブロックを消す前に虹色にしておく処理。
            for y in range(8):
                for x in range(8):
                    bg.blit(self.img_blc[self.puzzle[y][x]],[26+54*x,154+54*y]) 
        if self.flag == 1:#ブロックが下まで行った時の処理。リストを更新、ブロックを新生#
            self.ran1=self.ran4
            self.ran2=self.ran5
            self.ran3=self.ran6
            self.ranlis = [self.ran1,self.ran2,self.ran3]
            self.ran7=self.ran8
            self.ran4=random.randint(1,4)
            self.ran5=random.randint(1,4)
            self.ran6=random.randint(1,4)
            self.ran8=random.randint(0,1)
            posp3 = self.ran7list[self.ran7]
            self.posn3 = self.ran8list[self.ran8]
            self.sabun = [self.posp2[0] - posp3[0],self.posp2[1] - posp3[1]]
            self.copy_posp1 = [self.posp1[0],self.posp1[1]]
            self.copy_posp2 = [self.posp2[0],self.posp2[1]]
            self.copy_posp3 = [posp3[0],posp3[1]]
            self.copy_posn3 = [self.posn3[0],self.posn3[1]]
            self.poslis = [self.copy_posp1,self.copy_posp2,self.copy_posp3]#ここで再定義しなおさないといけないのはリストが中身に変数を入れていた場合、その変数が変更されてもリストの変数は更新されないから#
            self.cnt = 0
            self.flag = 0
            self.stopflag = 0
            self.ai_cnt = 0
            self.ai_decisionNum = random.randint(0,27)
    ###########################################################################################################################        
    def move_block(self,key,tmr):
        #落下について#
        if self.stopflag == 0:
            if key[pygame.K_DOWN] == 1 or self.ai_down:
                
                self.t = 24#54未満じゃないとcheck_touch内の定義でバグる#
            else:
                self.t = 3
    
        #左右移動について#
        #fragr,lが1の時にstopflagが1になってしまうと、flagr=1のまま左右に動けなくなる#

            if self.flagr == 0 and self.flagl == 0:
                if key[pygame.K_RIGHT] == 1 or self.ai_right:
                    self.flagr = 1
                    self.stoptmr = tmr
                    self.s1 = 27
                if key[pygame.K_LEFT] == 1 or self.ai_left:
                    self.flagl = 1
                    self.stoptmr = tmr
                    self.s2 = -27
            elif self.flagr == 1 and self.flagl == 1:
                 self.flagr = 0
                 self.flagl = 0
                 self.s1 = 0
                 self.s2 = 0
            elif self.flagr == 1:
                if tmr >= self.stoptmr + 2:
                    self.flagr = 0
                    self.s1 = 0
            elif self.flagl == 1:  
                if tmr >= self.stoptmr + 2:
                    self.flagl = 0
                    self.s2 = 0
        if self.stopflag == 1:
            self.s1 = 0
            self.s2 = 0
            self.flagr = 0
            self.fragl = 0
        for i in range(3):
            if self.poslis[i][0] == 26 + 54 * 7:
                self.s1 = 0
            if self.poslis[i][0] == 26 + 54 * 0:
                self.s2 = 0
    ########################################################################################################################
    def ai_init(self):
        self.ai_down = False
        self.ai_left = False
        self.ai_right = False
        self.ai_turnRight = False
        self.ai_turnLeft = False
    def ai_console_right(self):
        self.ai_right = True
    def ai_console_left(self):
        self.ai_left = True
    def ai_console_down(self):
        self.ai_down = True
    def ai_console_turnRight(self):
        self.ai_turnRight = True
    def ai_console_turnLeft(self):
        self.ai_turnLeft = True
    def ai_decision(self):
        pass
    def ai_action(self):
        act = self.ai_actionList[self.ai_decisionNum]
        ai_cnt = self.ai_cnt % 38
        if act[ai_cnt] == 0:
            self.ai_init()
        elif act[ai_cnt] == 1:
            self.ai_init()
            self.ai_console_down()
        elif act[ai_cnt] == 2:
            self.ai_init()
            self.ai_console_left()
        elif act[ai_cnt] == 3:
            self.ai_init()
            self.ai_console_right()
        elif act[ai_cnt] == 4:
            self.ai_init()
            self.ai_console_turnRight()

    

        
    ########################################################################################################################
    def check_touch(self):
        #横の接地判定#
        for i in range(3):
            for y in range(8):
                for x in range(8):
                    if self.poslis[i][0] == x * 54 + 26 and (y - 1) * 54 + 154   < self.poslis[i][1] + self.t <= y * 54 +154:
                        if x >= 1:
                            if self.puzzle[y][x - 1] != 0:
                                self.s2 = 0
                        if x <= 6:        
                            if self.puzzle[y][x + 1] != 0:
                                self.s1 = 0
        #縦の接地判定#
        if self.flag == 0 or self.flag ==1:
            for i in range(3):
                for y in range(7,-1,-1):
                    for x in range(8):
                        localsabun11 = self.poslis[i][1] - self.copy_posp1[1]
                        localsabun21 = self.poslis[i][1] - self.copy_posp2[1]
                        localsabun31 = self.poslis[i][1] - self.copy_posp3[1]
                        localsabun10 = self.poslis[i][0] - self.copy_posp1[0]
                        localsabun20 = self.poslis[i][0] - self.copy_posp2[0]
                        localsabun30 = self.poslis[i][0] - self.copy_posp3[0]
                        if self.poslis[i][0] == x * 54 + 26 and self.poslis[i][1] + self.t >= 154 + 54 * 7:
                            self.poslis[0][1] = 7 * 54 + 154 - localsabun11
                            self.poslis[1][1] = 7 * 54 + 154 - localsabun21
                            self.poslis[2][1] = 7 * 54 + 154 - localsabun31
                            self.puzzle[7][x] = self.ranlis[i]
                            self.flag = 2
                        if self.poslis[i][0] == x * 54 + 26 and self.poslis[i][1]  <= (y - 1) * 54 + 154 < self.poslis[i][1] + self.t:
                            if  self.puzzle[y][x] != 0:
                                self.poslis[0][1] = (y - 1) * 54 + 154 - localsabun11
                                self.poslis[1][1] = (y - 1) * 54 + 154 - localsabun21
                                self.poslis[2][1] = (y - 1) * 54 + 154 - localsabun31
                        
                                if y >= 1:
                                    self.puzzle[y-1][x] = self.ranlis[i]
                                    self.stopflag = 1
                                    self.flag = 2
                                if y == 0:
                                    self.gameover = 1
                        if self.poslis[i][0] == x * 54 + 26 + 27 and self.poslis[i][1] + self.t >= 154 + 54 * 7:
                            self.poslis[0][1] = 7 * 54 + 154 - localsabun11
                            self.poslis[1][1] = 7 * 54 + 154 - localsabun21
                            self.poslis[2][1] = 7 * 54 + 154 - localsabun31
                            self.poslis[0][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun10
                            self.poslis[1][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun20
                            self.poslis[2][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun30
                            self.puzzle[7][x] = self.ranlis[i]
                            self.stopflag = 1
                            self.flag = 2
                    
                    
                        if self.poslis[i][0] == x * 54 + 26 + 27 and self.poslis[i][1]  <= (y - 1) * 54 + 154 < self.poslis[i][1] + self.t:
                            if  self.puzzle[y][x] != 0:
                                self.poslis[0][1] = (y - 1) * 54 + 154 - localsabun11
                                self.poslis[1][1] = (y - 1) * 54 + 154 - localsabun21
                                self.poslis[2][1] = (y - 1) * 54 + 154 - localsabun31
                                self.poslis[0][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun10
                                self.poslis[1][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun20
                                self.poslis[2][0] = x * 54 + 26 + 27 + self.s1 + self.s2 - localsabun30
                        
                                if y >= 1:
                                    self.puzzle[y-1][x] = self.ranlis[i]
                                    self.stopflag = 1
                                    self.flag = 2
                                if y == 0:
                                    self.gameover = 1
        if self.flag == 4: 
            for y in range(6,-1,-1):
                for x in range(8):    
                    if self.auto_down_list[y][x][0] == x * 54 + 26 and self.auto_down_list[y][x][1] + self.auto_down_speed[y][x] >= 154 + 54 * (y+1) > self.auto_down_list[y][x][1]:
                        self.auto_down_list[y][x][1] = 154 + 54 * (y+1) #要らんかも#
                        self.puzzle[y+1][x] = self.auto_down_list[y][x][2]
                        self.auto_down_list[y][x] = [0,0,0]
                        self.auto_down_speed[y][x] = 0
                        self.flag = 3
                
                        
                        
                    
    ########################################################################################################################
    def death_check(self):
        if self.gameover == 1:
            game = Puyomodoki()
            

    ########################################################################################################################                                                
    def rotation(self,key,tmr):
        rot = [[54,-54],[54,54],[-54,54],[-54,-54]]
        cntt = self.cnt + 1 + self.ran7
        if self.rotflag == 1:
            if tmr == self.stoptmr2 + 4:
                self.rotflag = 0
        if self.rc_flag1 == 1 and self.rc_flag2 == 1 and self.rc_flag3 == 1 and self.rotflag == 0:
            if key[pygame.K_2] == 1 or self.ai_turnRight:
                self.copy_posp1[0] = self.copy_posp1[0] + rot[self.cnt % 4][0]
                self.copy_posp1[1] = self.copy_posp1[1] + rot[self.cnt % 4][1]
                self.copy_posp3[0] = self.copy_posp3[0] + rot[cntt % 4][0]
                self.copy_posp3[1] = self.copy_posp3[1] + rot[cntt % 4][1]
                self.cnt = self.cnt + 1
                self.stoptmr2 = tmr
                self.rotflag = 1
                self.rc_flag1 = 0
                self.rc_flag2 = 0
                self.rc_flag3 = 0
    ########################################################################################################################
    def rotation_check(self):
        self.rc_flag1 = 0
        self.rc_flag2 = 0
        self.rc_flag3 = 0
        rot = [[54,-54],[54,54],[-54,54],[-54,-54]]
        cntt = self.cnt + 1 + self.ran7
        if self.flagr == 0 and self.flagl == 0:
            self.rc_flag1 = 1
        for y in range(8):
            for x in range(8):
                if 54 * x + 26 == self.copy_posp1[0] + rot[self.cnt % 4][0] and 54 * (y - 1)+ 154 < self.copy_posp1[1] + rot[self.cnt % 4][1] + self.t <= 54 * y + 154:
                    if self.puzzle[y][x] == 0 :
                        self.rc_flag2 = 1
                    
                if 54 * x + 26 == self.copy_posp3[0] + rot[cntt % 4][0] and 54 * (y - 1)+ 154 < self.copy_posp3[1] + rot[cntt % 4][1] + self.t <= 54 * y + 154:
                    if self.puzzle[y][x] == 0 :
                        self.rc_flag3 = 1
        if self.copy_posp2[1] + self.t < 154:
            self.rc_flag2 = 1
            self.rc_flag3 = 1
    #########################################################################################################################
    def auto_down(self):#switchは自然落下ブロッが接地するまで消去フェーズに移行しないためのもの#
        print("auto_down")
        if self.flag == 2:
            for i in range(3):
                for y in range(8):
                    for x in range(8):
                        if self.poslis[i][0] == 26 + x * 54 and self.poslis[i][1] == 154 + y * 54:
                            self.puzzle[y][x] = self.ranlis[i]
                            self.flag = 3
        
        if self.flag ==3:
            switch = 0
            for y in range(6,-1,-1):
                for x in range(8):
                    if self.puzzle[y][x] != 0 and self.puzzle[y+1][x] == 0:
                        self.auto_down_list[y][x] = [26 + 54 * x,154 + 54 * y,self.puzzle[y][x]]#experiment_list2参照#
                        self.auto_down_speed[y][x] = 27
                        self.puzzle[y][x] = 0
                        switch = 1
                        self.flag = 4
                    
            if switch == 0:
                self.flag = 5
    ########################################################################################################################
    def check_delete(self,y,x,dcnt):
        if self.check[y][x] != 0 and self.check[y+1][x] == self.check2[y][x]:
            self.check[y+1][x] = self.check2[y][x] + 5 #4色の場合。これを用いて消去エフェクトを作ると同時にカウントのダブりを予防#
            dcnt = dcnt + 1
            dcnt = self.check_delete(y+1,x,dcnt)
        if self.check[y][x] != 0 and self.check[y-1][x] == self.check2[y][x]:
            self.check[y-1][x] = self.check2[y][x] + 5
            dcnt = dcnt + 1
            dcnt = self.check_delete(y-1,x,dcnt)
        if self.check[y][x] != 0 and self.check[y][x+1] == self.check2[y][x]:
            self.check[y][x+1] = self.check2[y][x] + 5
            dcnt = dcnt + 1
            dcnt = self.check_delete(y,x+1,dcnt)
        if self.check[y][x] != 0 and self.check[y][x-1] == self.check2[y][x]:
            self.check[y][x-1] = self.check2[y][x] + 5
            dcnt = dcnt + 1
            dcnt = self.check_delete(y,x-1,dcnt)
        return(dcnt)
    
              
    def delete(self,deletenum):#deletenumは何個くっつくと消えるかswitch2は消えるブロックがあるときまた自然落下に移行するためのもの#
        if self.flag == 6:
            self.delete_tmr -= 1
            if self.delete_tmr == 0:
                self.flag = 3
                for y in range(1,9):
                    for x in range(1,9):
                        if self.puzzle[y-1][x-1] == 5:
                            self.puzzle[y-1][x-1] = 0
        elif self.flag == 5:
            switch2 = 0
            print("switch2Before")
            print(switch2)
            for y in range(8):
                for x in range(8):
                    self.check[y+1][x+1] = self.puzzle[y][x]
                    self.check2[y+1][x+1] = self.puzzle[y][x]
            for y in range(1,9):
                for x in range(1,9):
                    for i in range(1,9):
                        for j in range(1,9):
                            self.check[i][j] = self.check2[i][j]
                    dcntneo = self.check_delete(y,x,self.dcnt[y][x])#checkdeleteのdcntはあくまで引数、その引数にリストのdcntを代入している#
                    print("dcntneo")
                    print(dcntneo)
                    if dcntneo >= deletenum:
                        switch2 = 1
                        self.flag = 6
                        self.delete_tmr = 20               
                        for y in range(1,9):
                            for x in range(1,9):
                                if self.check[y][x] >= 5:
                                    self.puzzle[y-1][x-1] = 5
            if self.flag != 6:                    
                self.flag = 3
                if switch2 == 0:
                    self.flag = 1
    ########################################################################################################################
    ########################################################################################################################        
    def main(self):
        pygame.init()
        pygame.display.set_caption("ぷよもどき")
        screen = pygame.display.set_mode((800,600))
        clock = pygame.time.Clock()
        mouse_c = 0

        tmr = 0
        while True:
            tmr = tmr + 1
            self.poslis = [self.copy_posp1,self.copy_posp2,self.copy_posp3]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            self.move_block(key,tmr)
            self.rotation_check()
            self.rotation(key,tmr)
            self.check_touch()
            self.death_check()
            self.auto_down()
            self.delete(4)
            if self.ai_automode:
                self.ai_cnt += 1
            self.create_block1(screen,tmr)
            self.ai_decision()
            self.ai_action()
            pygame.display.update()
            clock.tick(20)
if __name__ == '__main__':
    game = Puyomodoki()

