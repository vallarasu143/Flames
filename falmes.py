from tkinter import*
root=Tk()
root.geometry("500x300")
root.title("FLAMES")
root.resizable(0,0)

code_1=StringVar()
code_2=StringVar()
code_3=StringVar()

class Flames():
    def __members(self):
       self.__F=[5,7]
       self.__A=[6,8,10]
       self.__L=[12,14]
       self.__M=[13,15,17]
       self.__E=[16,18]
       self.__S=[9,11]
    def getname(self):
        self.__members()
        your_name=code_1.get()
        partner_name=code_2.get()
        a=len(your_name)
        b=len(partner_name)
        self.__c=(a+b)
        
    def __getbonding(self):
        Flames.getname(self)
        if (self.__c in self.__F):
            bonding="FREINDS"
            code_3.set(bonding)
        elif (self.__c in self.__A):
            bonding="AFACTION"
            code_3.set(bonding)
        elif (self.__c in self.__L):
            bonding="LOVERS"
            code_3.set(bonding)
        elif (self.__c in self.__M):
            bonding="MARRIGE"
            code_3.set(bonding)
        elif (self.__c in self.__E):
            bonding="ENEMY"
            code_3.set(bonding)
        elif (self.__c in self.__S):
            bonding="SISTER"
            code_3.set(bonding)
            

    
obj=Flames()
        


mainlabel=Label(root,text="FLAMES").pack()

label_1=Label(root,text="YOUR NAME:").place(x=50,y=80)
label_2=Label(root,text="PARTNER NAME:").place(x=50,y=120)
label_3=Label(root,text="YOUR BONDING:").place(x=50,y=220)

entry_1=Entry(root,width=20,textvariable=code_1).place(x=220,y=80)
entry_2=Entry(root,width=20,textvariable=code_2).place(x=220,y=120)
entry_3=Entry(root,width=20,textvariable=code_3).place(x=220,y=220)


button=Button(root,text="ENTER",width=10,height=1,
              command=lambda:obj._Flames__getbonding()).place(x=50,y=160)

root.mainloop()
