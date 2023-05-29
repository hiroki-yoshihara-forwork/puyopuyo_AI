import tkinter
import random

mouse_c=0
color = ["red","blue","green","yellow"]

def crst():
    global x
    global y
    global loc
    x = random.randint(100,700)
    y = random.randint(100,500)
    loc = [x,y+50,x+50,y+100,x,y,x+50,y+50,x+50,y+50,x+100,y+100]
    rec1=cvs.create_rectangle(loc[0],loc[1],loc[2],loc[3],fill=color[random.randint(0,3)])
    rec2=cvs.create_rectangle(loc[4],loc[5],loc[6],loc[7],fill=color[random.randint(0,3)])
    rec3=cvs.create_rectangle(loc[8],loc[9],loc[10],loc[11],fill=color[random.randint(0,3)])
    
def mouse_press(e):
    global mouse_c
    mouse_c = 1

def main():
    global mouse_c
    if mouse_c == 1:
        mouse_c = 0
        crst()
    root.after(100,main)
    
        


root = tkinter.Tk()
root.title("ブロックがランダムで出てくるやつ")
root.bind("<ButtonPress>",mouse_press)
cvs = tkinter.Canvas(width=800,height=600)
cvs.pack()
main()
root.mainloop()
