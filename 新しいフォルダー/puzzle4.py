import tkinter
import random

mouse_c=0
pos = [280,120,360,120,360,40,720,200,800,200,800,120,440,120,880,200]
ran1 = random.randint(1,4)
ran2 = random.randint(1,4)
ran3 = random.randint(1,4)
ran4 = random.randint(1,4)
ran5 = random.randint(1,4)
ran6 = random.randint(1,4)
#形を決めるランダム、1,2はpresent、3,4はnextブロック。ran7はranlist1,2を選択するランダム#
ran7 = random.randint(0,1)
ran8 = random.randint(0,1)
ranlist1 = [4,12]
ranlist2 = [5,13]
ranlist3 = [10,14]
ranlist4 = [11,15]

def crebl():#画像を表示させる#
    cvs.create_image(pos[0],pos[1],image=image_block[ran1],tag="BL")
    cvs.create_image(pos[2],pos[3],image=image_block[ran2],tag="BL")
    cvs.create_image(pos[ranlist1[ran7]],pos[ranlist2[ran7]],image=image_block[ran3],tag="BL")
    cvs.create_image(pos[6],pos[7],image=image_block[ran4],tag="BL")
    cvs.create_image(pos[8],pos[9],image=image_block[ran5],tag="BL")
    cvs.create_image(pos[ranlist3[ran8]],pos[ranlist4[ran8]],image=image_block[ran6],tag="BL")

def crebl2():#画像を変える#
    global ran1
    global ran2
    global ran3
    global ran4
    global ran5
    global ran6
    global ran7
    global ran8
    ran1=ran4
    ran2=ran5
    ran3=ran6
    ran7=ran8
    ran4=random.randint(1,4)
    ran5=random.randint(1,4)
    ran6=random.randint(1,4)
    ran8=random.randint(0,1)
    cvs.delete("BL")
    cvs.create_image(pos[0],pos[1],image=image_block[ran1],tag="BL")
    cvs.create_image(pos[2],pos[3],image=image_block[ran2],tag="BL")
    cvs.create_image(pos[ranlist1[ran7]],pos[ranlist2[ran7]],image=image_block[ran3],tag="BL")
    cvs.create_image(pos[6],pos[7],image=image_block[ran4],tag="BL")
    cvs.create_image(pos[8],pos[9],image=image_block[ran5],tag="BL")
    cvs.create_image(pos[ranlist3[ran8]],pos[ranlist4[ran8]],image=image_block[ran6],tag="BL")
   

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def main():
    global mouse_c
    if mouse_c == 1:
        mouse_c = 0
        crebl()
        root.after(100,main2)
    else :
        root.after(100,main)

def main2():
    global mouse_c
    
    if mouse_c == 1:
        mouse_c = 0
        crebl2()
    root.after(100,main2)

root = tkinter.Tk()
root.title("ブロックがランダムで出てくるやつ")
root.bind("<ButtonPress>",mouse_press)
cvs = tkinter.Canvas(width=900,height=640)
cvs.pack()

image_block=[
    None,
    tkinter.PhotoImage(file="square_blue.png"),
    tkinter.PhotoImage(file="square_green.png"),
    tkinter.PhotoImage(file="square_red.png"),
    tkinter.PhotoImage(file="square_yellow.png")
]

main()
root.mainloop()
