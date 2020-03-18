from tkinter import *
import matplotlib.pyplot as plt
from itertools import permutations



def enable():
    global player1,player2,buttn
    buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    b1.configure(text='1',state=NORMAL,bg='white')
    b2.configure(text='2',state=NORMAL,bg='white')
    b3.configure(text='3',state=NORMAL,bg='white')
    b4.configure(text='4',state=NORMAL,bg='white')
    b5.configure(text='5',state=NORMAL,bg='white')
    b6.configure(text='6',state=NORMAL,bg='white')
    b7.configure(text='7',state=NORMAL,bg='white')
    b8.configure(text='8',state=NORMAL,bg='white')
    b9.configure(text='9',state=NORMAL,bg='white')
    player1=[]
    player2=[]


#wininig condition

##123
##369
##789
##147
##159
##357
##258
##456
##

win_com=[(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,6,9),(4,5,6),(7,8,9),(3,5,7)]



root=Tk()                              #accses GUI library
root.title("My Window")                #naming the window

root.geometry("400x250+100+100")       #for resolution and location of screen




count1=0
count2=0

p=False
player1=[]
player2=[]


def abc():                             #fuctionality of 'submit' buttion
    print("hello")

def one(x):
    global buttn
    global comb1,comb2,count1,count2
    global p
    buttn.remove(x)
    p= not p
    if p == True:
        x.configure(state=DISABLED,bg='red')
        temp=int(x.config('text')[-1])
        print(temp)
        player1.append(temp)
        print(player1)
        x.config(text='O')
        if len(player1)>=3:
            comb1 = permutations(player1, 3) 
            print(comb1)
            for i in list(comb1):
                for j in win_com:
                    if i==j :
                        
                        #enable()
                        print('player 1 win')
                        count1=count1+1
                        e2.delete(0,'end')
                        e2.insert(0,str(count1))
                        p=False
                        for b in buttn:
                            b.config(state=DISABLED)
                            buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
                        return 
            if len(player1)+len(player2)==9:
                buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9] 
                print('draw')
                return                              
                
    if p == False:
        x.configure(state=DISABLED,bg='blue')
        temp=int(x.config('text')[-1])
        print(temp)
        player2.append(temp)
        print(player2)
        x.config(text='X')
        if len(player2)>=3:
            comb2 = permutations(player2, 3)
            print(comb2)
            for i in list(comb2):
                for j in win_com:
                    if i==j :
                        #enable()
                        print('player 2 win')
                        count2=count2+1
                        e5.delete(0,'end')
                        e5.insert(0,str(count2))
                        p =True
                        for b in buttn:
                            b.config(state=DISABLED)
                            buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9]                        
                        return
                        
            if len(player1)+len(player2)==9:
                buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9] 
                print('draw')
                return                       
f4=Frame(root,bg='white')
f4.pack(side='top',fill='both',expand='true')
l1=Label(f4,text='Player 1',fg='black',bg='red',font=('italic',20,'bold'))
l1.pack(side='left',fill='both',expand='true',padx=5,pady=5)

e2=Entry(f4,fg='black',bg='white')
e2.pack(side='right',fill='both',expand='true')

f5=Frame(root,bg='white')
f5.pack(side='top',fill='both',expand='true')
l2=Label(f5,text='player 2',fg='black',bg='blue',font=('italic',20,'bold'))
l2.pack(side='left',fill='both',expand='true',padx=5,pady=5)
e5=Entry(f5,fg='black',bg='white')
e5.pack(side='right',fill='both',expand='true')


f1=Frame(root,bg='white')
f1.pack(side='top',fill='both',expand='true')

b1=Button(f1,text='1',fg='black',bg='white',command=lambda :one(b1),activebackground='red')
b1.pack(side='left',fill='both',expand='true')

b2=Button(f1,text='2',fg='black',bg='white',command=lambda :one(b2),activebackground='red')
b2.pack(side='left',fill='both',expand='true')

b3=Button(f1,text='3',fg='black',bg='white',command=lambda :one(b3),activebackground='red')
b3.pack(side='left',fill='both',expand='true')


f2=Frame(root,bg='white')
f2.pack(side='top',fill='both',expand='true')

b4=Button(f2,text='4',fg='black',bg='white',command=lambda :one(b4),activebackground='red')
b4.pack(side='left',fill='both',expand='true')

b5=Button(f2,text='5',fg='black',bg='white',command=lambda :one(b5),activebackground='red')
b5.pack(side='left',fill='both',expand='true')

b6=Button(f2,text='6',fg='black',bg='white',command=lambda :one(b6),activebackground='red')
b6.pack(side='left',fill='both',expand='true')


f3=Frame(root,bg='white')
f3.pack(side='top',fill='both',expand='true')

b7=Button(f3,text='7',fg='black',bg='white',command=lambda :one(b7),activebackground='red')
b7.pack(side='left',fill='both',expand='true')

b8=Button(f3,text='8',fg='black',bg='white',command=lambda :one(b8),activebackground='red')
b8.pack(side='left',fill='both',expand='true')

b9=Button(f3,text='9',fg='black',bg='white',command=lambda :one(b9),activebackground='red')
b9.pack(side='left',fill='both',expand='true')

f3=Frame(root,bg='white')
f3.pack(side='top',fill='both',expand='true')

b10=Button(f3,text='restart',fg='black',bg='white',command=enable,activebackground='red')
b10.pack(side='left',fill='both',expand='true')


b11=Button(f3,text='exit',fg='black',bg='white',command=root.destroy,activebackground='red')
b11.pack(side='left',fill='both',expand='true')

buttn=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

mainloop()


