from tkinter import *
def createwindow() :
    top = Tk()
    top.title("Create Basic GUI using grid geometry")
    top.geometry("750x500")
    top.configure(bg="#BFEAF5")
    return(top)

def createwidget(top) :
    title = Label(top,text = "Find average of 3 number program",font=("Open Sans",(15)),fg="#0081C9",bg="#BFEAF5")
    title.grid(padx=60,pady=30)

    tag1=Label(top,text= "Number1 :",fg="#0081C9",font=("Open Sans",(15)),bg="#FFC93C")
    tag1.grid(row=1,column=0,pady=20)
    box1 = Entry(top,width=20)
    box1.grid(row=1,column=1,pady=20,ipady=7)

    tag2=Label(top,text= "Number2 :",fg="#0081C9",font=("Open Sans",(15)),bg="#FFC93C")
    tag2.grid(row=3,column=0,pady=25)
    box2 = Entry(top,width=20)
    box2.grid(row=3,column=1,pady=20,ipady=7)

    tag3=Label(top,text= "Number3 :",fg="#0081C9",font=("Open Sans",(15)),bg="#FFC93C")
    tag3.grid(row=5,column=0,pady=20)
    box3 = Entry(top,width=20)
    box3.grid(row=5,column=1,pady=20,ipady=7)

    botton1 = Button(top,text="Reset",width=25,bg="#5BC0F8")
    botton1.grid(row=7,column=0,pady=20,ipady=10)

    botton2 = Button(top,text="Find Average",width=25,bg="#5BC0F8")
    botton2.grid(row=7,column=1,pady=20,ipady=10)

    tag2=Label(top,text= "Created by Patiphan Arphorn , ID : 1650707878",fg="#0081C9",font=("Open Sans",(15)),bg="#BFEAF5")
    tag2.grid(row=8,column=0,pady=10,padx=15)

top = createwindow()
createwidget(top)
top.mainloop()