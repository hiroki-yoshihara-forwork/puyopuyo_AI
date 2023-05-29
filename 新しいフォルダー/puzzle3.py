import tkinter
import random

pos = [280,40,280,120,360,120,720,120,720,200,800,200]
ran1 = random.randint(1,4)
ran2 = random.randint(1,4)
ran3 = random.randint(1,4)
ran4 = random.randint(1,4)
ran5 = random.randint(1,4)
ran6 = random.randint(1,4)
mouse_c=0

def crebl():#画像を表示させる#
    cvs.create_image(pos[0],pos[1],image=image_block[ran1],tag="BL")
    cvs.create_image(pos[2],pos[3],image=image_block[ran2],tag="BL")
    cvs.create_image(pos[4],pos[5],image=image_block[ran3],tag="BL")
    cvs.create_image(pos[6],pos[7],image=image_block[ran4],tag="BL")
    cvs.create_image(pos[8],pos[9],image=image_block[ran5],tag="BL")
    cvs.create_image(pos[10],pos[11],image=image_block[ran6],tag="BL")

def crebl2():#画像を変える#
    global ran1
    global ran2
    global ran3
    global ran4
    global ran5
    global ran6
    ran1=ran4
    ran2=ran5
    ran3=ran6
    ran4=random.randint(1,4)
    ran5=random.randint(1,4)
    ran6=random.randint(1,4)
    cvs.delete("BL")
    cvs.create_image(pos[0],pos[1],image=image_block[ran1],tag="BL")
    cvs.create_image(pos[2],pos[3],image=image_block[ran2],tag="BL")
    cvs.create_image(pos[4],pos[5],image=image_block[ran3],tag="BL")
    cvs.create_image(pos[6],pos[7],image=image_block[ran4],tag="BL")
    cvs.create_image(pos[8],pos[9],image=image_block[ran5],tag="BL")
    cvs.create_image(pos[10],pos[11],image=image_block[ran6],tag="BL")
   

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
cvs = tkinter.Canvas(width=880,height=640)
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
