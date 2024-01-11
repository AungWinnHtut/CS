from tkinter import *
from tkinter import messagebox


def funLogin():
    uname = txtUserName.get()
    password = txtPassword.get()
    if uname == 'aung' and password == '1234':
        messagebox.showinfo('Success!','Login successfully')
    else:
        messagebox.showinfo('Fail!','Login fail, pls try again')


window = Tk()
window.geometry('340x280')

lblUserName = Label(window,text="Username:", font =('Courier',20, 'bold'))
lblUserName.pack()

txtUserName = Entry(window, bd =5,width=100,font =('Courier',20, 'bold'))
txtUserName.pack()

lblPassword = Label(window,text="Password:", font =('Courier',20, 'bold'))
lblPassword.pack()

txtPassword = Entry(window, bd =5,width=100,font =('Courier',20, 'bold'))
txtPassword.pack()

btnHello = Button(window, text = 'Login', font =('Courier',20, 'bold'),command=funLogin)
btnHello.pack()


window.mainloop()