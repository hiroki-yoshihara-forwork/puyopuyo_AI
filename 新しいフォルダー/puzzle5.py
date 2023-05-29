import tkinter
import random

mouse_c=0
pos = [224,134,278,134,278,80,590,165,644,165,644,111,332,134,698,165]
puzzle = []
check = []
for i in range(8):
    puzzle.append([0,0,0,0,0,0,0,0])
    check.append([0,0,0,0,0,0,0,0,])

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
cvs = tkinter.Canvas(root,width=800,height=600,bg="#000")
cvs.pack()
bg = [
    tkinter.PhotoImage(file="bg1.png"),
    tkinter.PhotoImage(file="bg2.png"),
    tkinter.PhotoImage(file="bg3.png")
]

cvs.create_image(250,378,image=bg[0])
cvs.create_image(640,300,image=bg[2])
label=tkinter.Label(root,text="NEXT",font=("メイリオ",20),fg="orange",bg="black")
label.place(x=520,y=30)
image_block=[
    None,
    tkinter.PhotoImage(file="square_blue1.png"),
    tkinter.PhotoImage(file="square_green1.png"),
    tkinter.PhotoImage(file="square_red1.png"),
    tkinter.PhotoImage(file="square_yellow1.png")
]

main()
root.mainloop()
