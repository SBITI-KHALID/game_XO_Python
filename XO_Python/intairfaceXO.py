import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('580x530')
window.resizable(False,False)
window.title("X/O game")
window.iconbitmap("images/icon (1).ico") 
bgImg = tk.PhotoImage(name='bgimage',file="images/bgImg.png")
new_width = 300
new_height = 300
# Images -------------------------------------------
resized_image = bgImg.subsample(bgImg.width() // new_width, bgImg.height() // new_height)
bgi = tk.Label(window,image=resized_image)
bgi.place(x=0,y=0)
# images of buttons ------------------------------
xImg = tk.PhotoImage(name='xImg',file="images/symboXX.png")
Xnew_width = 100
Xnew_height = 100
xresized_image = xImg.subsample(xImg.width() // Xnew_width, xImg.height() // Xnew_height)

yImg = tk.PhotoImage(name='yImg',file="images/red-circle-free-png.png")
ynew_width = 100
ynew_height = 100
yresized_image = yImg.subsample(yImg.width() // ynew_width, yImg.height() // ynew_height)

# Lines Images  ---------------------------------------------
# Line1 =  tk.PhotoImage(name='L1',file="images/L1.png")
# L1new_width = 300
# L1new_height = 300
# L1resized_image = Line1.subsample(Line1.width() // L1new_width, Line1.height() // L1new_height)
# L1b = tk.Label(window,image=L1resized_image)
# L1b.place(x=0,y=0)
# row 1 ---------------------------------------------
button1 = tk.Button(window,text='',bd=0)
button1.place(x=80,y=60,width=100,height=100)

button2 = tk.Button(window,text='',bd=0)
button2.place(x=250,y=60,width=100,height=100)

button3 = tk.Button(window,text='',bd=0)
button3.place(x=420,y=60,width=100,height=100)
# row 2 ---------------------------------------------
button4 = tk.Button(window,text='',bd=0)
button4.place(x=80,y=220,width=100,height=100)

button5 = tk.Button(window,text='',bd=0)
button5.place(x=250,y=220,width=100,height=100)

button6 = tk.Button(window,text='',bd=0)
button6.place(x=420,y=220,width=100,height=100)
# row3 ---------------------------------------------
button7 = tk.Button(window,text='',bd=0)
button7.place(x=80,y=380,width=100,height=100)

button8 = tk.Button(window,text='',bd=0)
button8.place(x=250,y=380,width=100,height=100)

button9 = tk.Button(window,text='',bd=0)
button9.place(x=420,y=380,width=100,height=100)

# Functions ----------------------------------------
class Traitement():
    jeux = True
    v = True
    active = False
    X = 'X'
    O = 'O'
    def __init__(self):
        self.Activbtn1 = ''
        self.Activbtn2 = ''
        self.Activbtn3 = ''
        self.Activbtn4 = ''
        self.Activbtn5 = ''
        self.Activbtn6 = ''
        self.Activbtn7 = ''
        self.Activbtn8 = ''
        self.Activbtn9 = ''
        
    def Message(self, value):
            if (messagebox.showinfo("", value) == 'ok'):
                button1.config(text='')
                button1.config(image='')
                button2.config(text='')
                button2.config(image='')
                button3.config(text='')
                button3.config(image='')
                button4.config(image='')
                button4.config(text='')
                button5.config(image='')
                button5.config(text='')
                button6.config(image='')
                button6.config(text='')
                button7.config(image='')
                button7.config(text='')
                button8.config(image='')
                button8.config(text='')
                button9.config(text='')
                button9.config(image='')
                self.Activbtn1 = ''
                self.Activbtn2 = ''
                self.Activbtn3 = ''
                self.Activbtn4 = ''
                self.Activbtn5 = ''
                self.Activbtn6 = ''
                self.Activbtn7 = ''
                self.Activbtn8 = ''
                self.Activbtn9 = ''
                self.v = True
                self.active = False

    
    def Verifier(self):
        if ((self.Activbtn1 == self.Activbtn2 and self.Activbtn2 == self.Activbtn3) and( self.Activbtn1 != ''and self.Activbtn2 != ''and self.Activbtn3 != '')):
            T.Message((self.Activbtn1,'gagner'))
        elif (self.Activbtn4 == self.Activbtn5 and self.Activbtn5 == self.Activbtn6 and( self.Activbtn4 != ''and self.Activbtn5 != ''and self.Activbtn6 != '')):
            T.Message((self.Activbtn4,'gagner'))
        elif (self.Activbtn7 == self.Activbtn8 and self.Activbtn8 == self.Activbtn9 and( self.Activbtn7 != ''and self.Activbtn8 != ''and self.Activbtn9 != '')):
            T.Message((self.Activbtn7,'gagner'))
        elif (self.Activbtn1 == self.Activbtn5 and self.Activbtn5 == self.Activbtn9 and( self.Activbtn1 != ''and self.Activbtn5 != ''and self.Activbtn9 != '')):
            T.Message((self.Activbtn1,'gagner'))
        elif (self.Activbtn3 == self.Activbtn5 and self.Activbtn5 == self.Activbtn7 and( self.Activbtn3 != ''and self.Activbtn5 != ''and self.Activbtn7 != '')):
            T.Message((self.Activbtn3,'gagner'))
        elif (self.Activbtn1 == self.Activbtn4 and self.Activbtn4 == self.Activbtn7 and( self.Activbtn1 != ''and self.Activbtn4 != ''and self.Activbtn7 != '')):
            T.Message((self.Activbtn1,'gagner'))
        elif (self.Activbtn2 == self.Activbtn5 and self.Activbtn5 == self.Activbtn8 and( self.Activbtn2 != ''and self.Activbtn5 != ''and self.Activbtn8 != '')):
            T.Message((self.Activbtn2,'gagner'))
        elif (self.Activbtn3 == self.Activbtn6 and self.Activbtn6 == self.Activbtn9 and( self.Activbtn3 != ''and self.Activbtn6 != ''and self.Activbtn9 != '')):
            T.Message((self.Activbtn3,'gagner'))
        elif (self.Activbtn1 != '' and self.Activbtn2 != '' and self.Activbtn3 != ''
              and self.Activbtn5 != '' and self.Activbtn5 != '' and self.Activbtn6 != ''
              and self.Activbtn7 != '' and self.Activbtn8 != '' and self.Activbtn9 != ''):
            T.Message("Parti null")
            
         
    def btn1(self):
        if self.Activbtn1 == ''  :
            if(self.v == True):
                button1.config(text= self.X)
                button1.config(image=xresized_image)
                self.Activbtn1 = self.X
                self.v = False
            else:
                button1.config(text= self.O)
                button1.config(image =yresized_image)
                self.Activbtn1 = self.O
                self.v = True
        T.Verifier()


    def btn2(self):
            if self.Activbtn2 == '' :
                if(self.v == True):
                    button2.config(text= self.X)
                    button2.config(image=xresized_image)
                    self.v = False
                    self.Activbtn2 = self.X
                else:
                    button2.config(text= self.O)
                    button2.config(image =yresized_image)
                    self.v = True
                    self.Activbtn2 = self.O
            T.Verifier()    
        
    def btn3(self):
        if self.Activbtn3 == "" :
                if(self.v == True):
                    button3.config(text= self.X)
                    button3.config(image=xresized_image)
                    self.Activbtn3 = self.X
                    self.v = False
                else:
                    button3.config(text= self.O)
                    button3.config(image =yresized_image)
                    self.Activbtn3 = self.O
                    self.v = True
        T.Verifier()
        
    def btn4(self):
        if self.Activbtn4 == "" :
                if(self.v == True):
                    button4.config(text= self.X)
                    button4.config(image=xresized_image)
                    self.Activbtn4 = self.X
                    self.v = False
                else:
                    button4.config(text= self.O)
                    button4.config(image =yresized_image)
                    self.Activbtn4 = self.O
                    self.v = True
        
    def btn5(self):
        if self.Activbtn5 == "" :
            if(self.v == True):
                button5.config(text= self.X)
                button5.config(image=xresized_image)
                self.Activbtn5 = self.X
                self.v = False
            else:
                button5.config(text= self.O)
                button5.config(image =yresized_image)
                self.Activbtn5 = self.O
                self.v = True
        T.Verifier()

    def btn6(self):
        if self.Activbtn6 == "" :
            if(self.v == True):
                button6.config(text= self.X)
                button6.config(image=xresized_image)
                self.Activbtn6 = self.X
                self.v = False
            else:
                button6.config(text= self.O)
                button6.config(image =yresized_image)
                self.Activbtn6 = self.O
                self.v = True
        T.Verifier()

    def btn7(self):
        if self.Activbtn7 == "" :
            if(self.v == True):
                button7.config(text= self.X)
                button7.config(image=xresized_image)
                self.Activbtn7 = self.X
                self.v = False
            else:
                button7.config(text= self.O)
                button7.config(image =yresized_image)
                self.Activbtn7 = self.O
                self.v = True
        T.Verifier()                

    def btn8(self):
        if self.Activbtn8 == "" :
            if(self.v == True):
                button8.config(text= self.X)
                button8.config(image=xresized_image)
                self.Activbtn8 = self.X
                self.v = False
            else:
                button8.config(text= self.O)
                button8.config(image =yresized_image)
                self.Activbtn8 = self.O
                self.v = True
        T.Verifier()                

    def btn9(self):
        if self.Activbtn9 == "" :
            if(self.v == True):
                button9.config(text= self.X)
                button9.config(image=xresized_image)
                self.Activbtn9 = self.X
                self.v = False
            else:
                button9.config(text= self.O)
                button9.config(image =yresized_image)
                self.Activbtn9 = self.O
                self.v = True
        T.Verifier()                

      
T = Traitement()
button1.config(command=T.btn1)
button2.config(command=T.btn2)
button3.config(command=T.btn3)
button4.config(command=T.btn4)
button5.config(command=T.btn5)
button6.config(command=T.btn6)
button7.config(command=T.btn7)
button8.config(command=T.btn8)
button9.config(command=T.btn9)

window.mainloop()