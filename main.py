from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess
import threading
import os
import sys

pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(False, False)
pro.title('SuperMarché El Mejri')
pro.iconbitmap('icone.ico')
title = Label(pro, text='Système de SuperMarché', fg='gold', bg='black', font=('tajawal', 16, 'bold'))
title.pack(fill=X)
u1 = 'https://www.facebook.com/aziz30mejri'
u2 = 'www.linkedin.com/in/mohamed-aziz-mejri-tn'
u3 = 'https://github.com/Aziz30Mejri'


def Facebook():
    webbrowser.open_new(u1)


def Linkedin():
    webbrowser.open_new(u2)


def Githib():
    webbrowser.open_new(u3)


def Gmail():
    url = "https://mail.google.com/mail/?view=cm&fs=1&to=aziz30mejri@gmail.com"
    webbrowser.open(url)


def run_script():
    # Exécute 'super.py' dans un thread séparé
    subprocess.call(['python', 'super.py'])


def login():
    user = En1.get()
    password = En2.get()
    if user == 'admin' and password == 'admin':
        threading.Thread(target=run_script).start()
        pro.after(100, pro.destroy)
    else:
        messagebox.showerror('Erreur', 'Données erronées')


def on_enter(e):
    e.widget.config(bg='#CA3928', fg='black')


def on_leave(e):
    e.widget.config(bg='#DBA901', fg='white')
    e.widget.config(cursor="hand2")


F1 = Frame(pro, width=230, height=420, bg='#0B2F3A')
F1.place(x=570, y=30)
Title1 = Label(F1, text='Projet de Supermarché', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title1.place(x=42, y=20)
Title2 = Label(F1, text='Contactez Moi', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title2.place(x=60, y=60)

B1 = Button(F1, text='FaceBook', width=22, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=Facebook)
B1.place(x=20, y=118)
B2 = Button(F1, text='LinkedIn', width=22, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=Linkedin)
B2.place(x=20, y=170)
B3 = Button(F1, text='GitHub', width=22, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=Githib)
B3.place(x=20, y=220)
B4 = Button(F1, text='Email', width=22, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=Gmail)
B4.place(x=20, y=270)
B6 = Button(F1, text='Quitter', width=22, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=quit)
B6.place(x=20, y=350)

photo = PhotoImage(file='shop.png')
imo = Label(pro, image=photo)
imo.place(x=-30, y=30, width=600, height=372)

F2 = Frame(pro, width=570, height=120, bg='#0B2F3A')
F2.place(x=0, y=330)
photo1 = PhotoImage(file='log.png')
imo1 = Label(pro, image=photo1)
imo1.place(x=460, y=335, width=110, height=110)
L1 = Label(F2, text="Nom d'utilisateur:", fg='gold', bg='#0B2F3A', font=('tajawal', 12))
L1.place(x=10, y=20)
L2 = Label(F2, text='Mot de Passe:', fg='gold', bg='#0B2F3A', font=('tajawal', 12))
L2.place(x=10, y=70)
En1 = Entry(F2, font=('tajawal', 12), justify='center')
En1.place(x=140, y=23)
En2 = Entry(F2, font=('tajawal', 12), justify='center', show='*')
En2.place(x=140, y=70)
B = Button(F2, text='Se Connecter', bg='#DBA901', font=('tajawal', 12), width=12, height=3, command=login)
B.bind("<Enter>", on_enter)
B.bind("<Leave>", on_leave)
B.place(x=340, y=16)

pro.mainloop()
