from tkinter import *
from tkinter import messagebox
import re
import math, random, os


class super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1540x1080')
        self.root.title('SuperMarché El Mejri')
        self.root.resizable(False, False)
        self.root.iconbitmap('icone.ico')
        title = Label(self.root, text='Gestion du SuperMarché', fg='white', bg='#0B2F3A', font=('tajawal', 15, 'bold'))
        title.pack(fill=X)

        # ==== Les Variables Colonne 1====#
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        self.q11 = IntVar()
        self.q12 = IntVar()
        self.q13 = IntVar()
        self.q14 = IntVar()
        self.q15 = IntVar()
        self.q16 = IntVar()
        self.q17 = IntVar()
        self.q18 = IntVar()

        # ==== Les Variables Colonne 2====#
        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
        self.qq8 = IntVar()
        self.qq9 = IntVar()
        self.qq10 = IntVar()
        self.qq11 = IntVar()
        self.qq12 = IntVar()
        self.qq13 = IntVar()
        self.qq14 = IntVar()
        self.qq15 = IntVar()
        self.qq16 = IntVar()
        self.qq17 = IntVar()
        self.qq18 = IntVar()

        # ==== Les Variables Colonne 3====#
        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        self.qqq8 = IntVar()
        self.qqq9 = IntVar()
        self.qqq10 = IntVar()
        self.qqq11 = IntVar()
        self.qqq12 = IntVar()
        self.qqq13 = IntVar()
        self.qqq14 = IntVar()
        self.qqq15 = IntVar()
        self.qqq16 = IntVar()
        self.qqq17 = IntVar()
        self.qqq18 = IntVar()

        # ==== Les Variables de la Facture ====#
        self.fatora = StringVar()
        self.nom = StringVar()
        self.phone = StringVar()
        x = random.randint(1000, 9999)
        self.fatora.set(str(x))

        # ==== Calcul ====#
        self.bacoliat = StringVar()
        self.adoat = StringVar()
        self.madrasa = StringVar()

        # =====Données du Client ====#
        F1 = Frame(root, bd=2, width=528, height=170, bg='#0B4C5F')
        F1.place(x=0, y=35)
        tit = Label(F1, text='Les Données du Client:', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='tomato')
        tit.place(x=30, y=0)
        his_name = Label(F1, text='Nom du Client', font=('tajawal', 10), bg='#0B4C5F', fg='white')
        his_name.place(x=60, y=40)
        his_phone = Label(F1, text='Numéro Clinet', font=('tajawal', 10), bg='#0B4C5F', fg='white')
        his_phone.place(x=60, y=70)
        bill_num = Label(F1, text='Numéro Facture', font=('tajawal', 10), bg='#0B4C5F', fg='white')
        bill_num.place(x=60, y=100)

        Ent_name = Entry(F1, textvariable=self.nom, justify='center')
        Ent_name.place(x=180, y=42)
        Ent_phone = Entry(F1, textvariable=self.phone, justify='center')
        Ent_phone.place(x=180, y=72)
        Ent_bill = Entry(F1, textvariable=self.fatora, justify='center')
        Ent_bill.place(x=180, y=102)

        btn_customer = Button(F1, text='    Recherche    ', font=('tajawal', 10), width=10, height=4, bg='white')
        btn_customer.place(x=350, y=40)

        # ==== Facture ====#
        titdd = Label(root, text='Les Factures', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        titdd.place(x=180, y=170)
        F3 = Frame(root, bd=2, width=338, height=500, bg='white')
        F3.place(x=0, y=207)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3, yscrollcommand=scrol_y.set, wrap='word', width=63, height=32)
        self.textarea.grid(row=0, column=0, sticky='nsew')
        scrol_y.grid(row=0, column=1, sticky='ns')
        scrol_y.config(command=self.textarea.yview)
        F3.grid_rowconfigure(0, weight=1)
        F3.grid_columnconfigure(0, weight=1)
        for i in range(100):
            self.textarea.insert('end', f"Line {i + 1}\n")

        # ==== Les Prix ====#
        F4 = Frame(root, bd=2, width=848, height=112, bg='#0B4C5F')
        F4.place(x=0, y=722)
        hesab = Button(F4, text='Le Montant', width=15, height=1, font=('tajawal', 13), bg='#DBA901',
                       command=self.total)
        hesab.place(x=25, y=10)
        fatora = Button(F4, text='Exporte', width=15, height=1, font=('tajawal', 13), bg='#DBA901',
                        command=self.billing)
        fatora.place(x=25, y=55)
        clear = Button(F4, text='Supprimer', width=15, height=1, font=('tajawal', 13), bg='#DBA901', command=self.clear)
        clear.place(x=180, y=10)
        exite = Button(F4, text='Quitter', width=15, height=1, font=('tajawal', 13), bg='#DBA901', command=self.close)
        exite.place(x=180, y=55)

        lblol1 = Label(F4, text='Calcul des Articles Scolaires', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        lblol1.place(x=385, y=10)
        lblol2 = Label(F4, text='Calcul des Fournitures Ménagéres', font=('tajawal', 13, 'bold'), bg='#0B4C5F',
                       fg='gold')
        lblol2.place(x=385, y=40)
        lblol3 = Label(F4, text='Calcul Total des Légumineuses', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        lblol3.place(x=385, y=70)
        ento1 = Entry(F4, textvariable=self.madrasa, width=20)
        ento1.place(x=640, y=15)
        ento2 = Entry(F4, textvariable=self.adoat, width=20)
        ento2.place(x=640, y=46)
        ento3 = Entry(F4, textvariable=self.bacoliat, width=20)
        ento3.place(x=640, y=76)

        # ====  items[1] ====#
        FF1 = Frame(root, bd=2, width=338, height=800, bg='#0B4C5F')
        FF1.place(x=1190, y=35)
        t = Label(FF1, text='Les Légumineuses', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=100, y=20)
        bq1 = Label(FF1, text='Riz', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq1.place(x=70, y=80)
        bq2 = Label(FF1, text='Boulgour', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq2.place(x=70, y=110)
        bq3 = Label(FF1, text='Haricot', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq3.place(x=70, y=140)
        bq4 = Label(FF1, text='Lentille', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq4.place(x=70, y=170)
        bq5 = Label(FF1, text='Lentilles Vertes', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq5.place(x=70, y=200)
        bq6 = Label(FF1, text='Freekeh', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq6.place(x=70, y=230)
        bq7 = Label(FF1, text='Pois Chiche', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq7.place(x=70, y=260)
        bq8 = Label(FF1, text='Pois Cassés', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq8.place(x=70, y=290)
        bq9 = Label(FF1, text='Sel', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq9.place(x=70, y=320)
        bq10 = Label(FF1, text='Sucre', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq10.place(x=70, y=350)
        bq11 = Label(FF1, text='Poivron Noir', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq11.place(x=70, y=380)
        bq12 = Label(FF1, text='Poivron Rouge', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq12.place(x=70, y=410)
        bq13 = Label(FF1, text='Macaroni', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq13.place(x=70, y=440)
        bq14 = Label(FF1, text='flageolets', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq14.place(x=70, y=470)
        bq15 = Label(FF1, text='Vesces', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq15.place(x=70, y=500)
        bq16 = Label(FF1, text='Pois Sabre', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq16.place(x=70, y=530)
        bq17 = Label(FF1, text='Haricot Urd', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq17.place(x=70, y=560)
        bq18 = Label(FF1, text='Haricot Tépari', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq18.place(x=70, y=590)

        bqent1 = Entry(FF1, textvariable=self.q1, width=12)
        bqent1.place(x=180, y=80)
        bqent2 = Entry(FF1, textvariable=self.q2, width=12)
        bqent2.place(x=180, y=110)
        bqent3 = Entry(FF1, textvariable=self.q3, width=12)
        bqent3.place(x=180, y=140)
        bqent4 = Entry(FF1, textvariable=self.q4, width=12)
        bqent4.place(x=180, y=170)
        bqent5 = Entry(FF1, textvariable=self.q5, width=12)
        bqent5.place(x=180, y=200)
        bqent6 = Entry(FF1, textvariable=self.q6, width=12)
        bqent6.place(x=180, y=230)
        bqent7 = Entry(FF1, textvariable=self.q7, width=12)
        bqent7.place(x=180, y=260)
        bqent8 = Entry(FF1, textvariable=self.q8, width=12)
        bqent8.place(x=180, y=290)
        bqent9 = Entry(FF1, textvariable=self.q9, width=12)
        bqent9.place(x=180, y=320)
        bqent10 = Entry(FF1, textvariable=self.q10, width=12)
        bqent10.place(x=180, y=350)
        bqent11 = Entry(FF1, textvariable=self.q11, width=12)
        bqent11.place(x=180, y=380)
        bqent12 = Entry(FF1, textvariable=self.q12, width=12)
        bqent12.place(x=180, y=410)
        bqent13 = Entry(FF1, textvariable=self.q13, width=12)
        bqent13.place(x=180, y=440)
        bqent14 = Entry(FF1, textvariable=self.q14, width=12)
        bqent14.place(x=180, y=470)
        bqent15 = Entry(FF1, textvariable=self.q15, width=12)
        bqent15.place(x=180, y=500)
        bqent16 = Entry(FF1, textvariable=self.q16, width=12)
        bqent16.place(x=180, y=530)
        bqent17 = Entry(FF1, textvariable=self.q17, width=12)
        bqent17.place(x=180, y=560)
        bqent18 = Entry(FF1, textvariable=self.q18, width=12)
        bqent18.place(x=180, y=590)

        # ==== items[2] ====#
        FF2 = Frame(root, bd=2, width=338, height=800, bg='#0B4C5F')
        FF2.place(x=850, y=35)
        t = Label(FF2, text='Les Fournitures Ménagers', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=80, y=20)
        bq1 = Label(FF2, text='Micro Onde', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq1.place(x=70, y=80)
        bq2 = Label(FF2, text='Aspirateur', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq2.place(x=70, y=110)
        bq3 = Label(FF2, text='Balai', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq3.place(x=70, y=140)
        bq4 = Label(FF2, text='Seau', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq4.place(x=70, y=170)
        bq5 = Label(FF2, text='Serpillère', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq5.place(x=70, y=200)
        bq6 = Label(FF2, text='Eponges', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq6.place(x=70, y=230)
        bq7 = Label(FF2, text='Plumeau', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq7.place(x=70, y=260)
        bq8 = Label(FF2, text='Sacs poubelles', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq8.place(x=70, y=290)
        bq9 = Label(FF2, text='Canard WC', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq9.place(x=70, y=320)
        bq10 = Label(FF2, text='Lave-Vaisselle', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq10.place(x=70, y=350)
        bq11 = Label(FF2, text='Brosse', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq11.place(x=70, y=380)
        bq12 = Label(FF2, text='Assouplissant', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq12.place(x=70, y=410)
        bq13 = Label(FF2, text='Fer à repasser', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq13.place(x=70, y=440)
        bq14 = Label(FF2, text='Lave-linge', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq14.place(x=70, y=470)
        bq15 = Label(FF2, text='Terre de sommières', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq15.place(x=70, y=500)
        bq16 = Label(FF2, text='Cuillères', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq16.place(x=70, y=530)
        bq17 = Label(FF2, text='Couteau', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq17.place(x=70, y=560)
        bq18 = Label(FF2, text='Fourchette', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq18.place(x=70, y=590)

        bqent1 = Entry(FF2, textvariable=self.qq1, width=12)
        bqent1.place(x=180, y=80)
        bqent2 = Entry(FF2, textvariable=self.qq2, width=12)
        bqent2.place(x=180, y=110)
        bqent3 = Entry(FF2, textvariable=self.qq3, width=12)
        bqent3.place(x=180, y=140)
        bqent4 = Entry(FF2, textvariable=self.qq4, width=12)
        bqent4.place(x=180, y=170)
        bqent5 = Entry(FF2, textvariable=self.qq5, width=12)
        bqent5.place(x=180, y=200)
        bqent6 = Entry(FF2, textvariable=self.qq6, width=12)
        bqent6.place(x=180, y=230)
        bqent7 = Entry(FF2, textvariable=self.qq7, width=12)
        bqent7.place(x=180, y=260)
        bqent8 = Entry(FF2, textvariable=self.qq8, width=12)
        bqent8.place(x=180, y=290)
        bqent9 = Entry(FF2, textvariable=self.qq9, width=12)
        bqent9.place(x=180, y=320)
        bqent10 = Entry(FF2, textvariable=self.qq10, width=12)
        bqent10.place(x=180, y=350)
        bqent11 = Entry(FF2, textvariable=self.qq11, width=12)
        bqent11.place(x=180, y=380)
        bqent12 = Entry(FF2, textvariable=self.qq12, width=12)
        bqent12.place(x=180, y=410)
        bqent13 = Entry(FF2, textvariable=self.qq13, width=12)
        bqent13.place(x=180, y=440)
        bqent14 = Entry(FF2, textvariable=self.qq14, width=12)
        bqent14.place(x=180, y=470)
        bqent15 = Entry(FF2, textvariable=self.qq15, width=12)
        bqent15.place(x=180, y=500)
        bqent16 = Entry(FF2, textvariable=self.qq16, width=12)
        bqent16.place(x=180, y=530)
        bqent17 = Entry(FF2, textvariable=self.qq17, width=12)
        bqent17.place(x=180, y=560)
        bqent18 = Entry(FF2, textvariable=self.qq18, width=12)
        bqent18.place(x=180, y=590)

        # ==== items[3] ====#
        FF3 = Frame(root, bd=2, width=318, height=686, bg='#0B4C5F')
        FF3.place(x=530, y=35)

        t = Label(FF3, text='Les Articles Scolaires', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=70, y=20)
        bq1 = Label(FF3, text='Sac à Dos', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq1.place(x=70, y=80)
        bq2 = Label(FF3, text='Trousse', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq2.place(x=70, y=110)
        bq3 = Label(FF3, text='Stylos', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq3.place(x=70, y=140)
        bq4 = Label(FF3, text='Gommes', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq4.place(x=70, y=170)
        bq5 = Label(FF3, text='Ciseaux', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq5.place(x=70, y=200)
        bq6 = Label(FF3, text='Feutres', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq6.place(x=70, y=230)
        bq7 = Label(FF3, text='Des Êtiquettes', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq7.place(x=70, y=260)
        bq8 = Label(FF3, text='Cahier de Texte', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq8.place(x=70, y=290)
        bq9 = Label(FF3, text='Feutre Effaçable', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq9.place(x=70, y=320)
        bq10 = Label(FF3, text='Pochette', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq10.place(x=70, y=350)
        bq11 = Label(FF3, text='Crayons', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq11.place(x=70, y=380)
        bq12 = Label(FF3, text='Règle Graduée', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq12.place(x=70, y=410)
        bq13 = Label(FF3, text='Crayons à Papier', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq13.place(x=70, y=440)
        bq14 = Label(FF3, text='Tube de Colle', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq14.place(x=70, y=470)
        bq15 = Label(FF3, text='Classeurs', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq15.place(x=70, y=500)
        bq16 = Label(FF3, text='Des Feuilles', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq16.place(x=70, y=530)
        bq17 = Label(FF3, text='Calculatrice', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq17.place(x=70, y=560)
        bq18 = Label(FF3, text='Compas', font=('tajawal', 11), bg='#0B4C5F', fg='white')
        bq18.place(x=70, y=590)

        bqent1 = Entry(FF3, textvariable=self.qqq1, width=12)
        bqent1.place(x=180, y=80)
        bqent2 = Entry(FF3, textvariable=self.qqq2, width=12)
        bqent2.place(x=180, y=110)
        bqent3 = Entry(FF3, textvariable=self.qqq3, width=12)
        bqent3.place(x=180, y=140)
        bqent4 = Entry(FF3, textvariable=self.qqq4, width=12)
        bqent4.place(x=180, y=170)
        bqent5 = Entry(FF3, textvariable=self.qqq5, width=12)
        bqent5.place(x=180, y=200)
        bqent6 = Entry(FF3, textvariable=self.qqq6, width=12)
        bqent6.place(x=180, y=230)
        bqent7 = Entry(FF3, textvariable=self.qqq7, width=12)
        bqent7.place(x=180, y=260)
        bqent8 = Entry(FF3, textvariable=self.qqq8, width=12)
        bqent8.place(x=180, y=290)
        bqent9 = Entry(FF3, textvariable=self.qqq9, width=12)
        bqent9.place(x=180, y=320)
        bqent10 = Entry(FF3, textvariable=self.qqq10, width=12)
        bqent10.place(x=180, y=350)
        bqent11 = Entry(FF3, textvariable=self.qqq11, width=12)
        bqent11.place(x=180, y=380)
        bqent12 = Entry(FF3, textvariable=self.qqq12, width=12)
        bqent12.place(x=180, y=410)
        bqent13 = Entry(FF3, textvariable=self.qqq13, width=12)
        bqent13.place(x=180, y=440)
        bqent14 = Entry(FF3, textvariable=self.qqq14, width=12)
        bqent14.place(x=180, y=470)
        bqent15 = Entry(FF3, textvariable=self.qqq15, width=12)
        bqent15.place(x=180, y=500)
        bqent16 = Entry(FF3, textvariable=self.qqq16, width=12)
        bqent16.place(x=180, y=530)
        bqent17 = Entry(FF3, textvariable=self.qqq17, width=12)
        bqent17.place(x=180, y=560)
        bqent18 = Entry(FF3, textvariable=self.qqq18, width=12)
        bqent18.place(x=180, y=590)
        self.welcome()

    def total(self):
        self.rez = round(self.q1.get() * 2.000, 3)
        self.borgol = round(self.q2.get() * 1.500, 3)
        self.fasoli = round(self.q3.get() * 2.500, 3)
        self.ades = round(self.q4.get() * 4.000, 3)
        self.makrona = round(self.q5.get() * 3.250, 3)
        self.frika = round(self.q6.get() * 1.150, 3)
        self.homes = round(self.q7.get() * 2.250, 3)
        self.fol = round(self.q8.get() * 1.750, 3)
        self.mlah = round(self.q9.get() * 0.800, 3)
        self.skar = round(self.q10.get() * 0.999, 3)
        self.felfeahmer = round(self.q11.get() * 3.400, 3)
        self.felfeakhel = round(self.q12.get() * 0.450, 3)
        self.lobia = round(self.q13.get() * 2.200, 3)
        self.admami = round(self.q14.get() * 2.150, 3)
        self.qamah = round(self.q15.get() * 0.700, 3)
        self.shair = round(self.q16.get() * 1.400, 3)
        self.shofan = round(self.q17.get() * 1.400, 3)
        self.zara = round(self.q18.get() * 3.500, 3)
        self.totalito = round(float(
            self.rez + self.borgol + self.fasoli + self.ades + self.makrona + self.frika + self.homes + self.fol + self.mlah + self.skar + self.felfeahmer +
            self.felfeakhel + self.lobia + self.admami + self.qamah + self.shair + self.shofan + self.zara), 3)
        self.bacoliat.set(f"{self.totalito:.3f} TND")

        self.rez1 = round(self.qq1.get() * 2.000, 3)
        self.borgol1 = round(self.qq2.get() * 1.500, 3)
        self.fasoli1 = round(self.qq3.get() * 2.500, 3)
        self.ades1 = round(self.qq4.get() * 4.500, 3)
        self.makrona1 = round(self.qq5.get() * 3.200, 3)
        self.frika1 = round(self.qq6.get() * 1.150, 3)
        self.homes1 = round(self.qq7.get() * 2.200, 3)
        self.fol1 = round(self.qq8.get() * 1.700, 3)
        self.mlah1 = round(self.qq9.get() * 0.800, 3)
        self.skar1 = round(self.qq10.get() * 0.999, 3)
        self.felfeahmer1 = round(self.qq11.get() * 3.450, 3)
        self.felfeakhel1 = round(self.qq12.get() * 0.450, 3)
        self.lobia1 = round(self.qq13.get() * 2.200, 3)
        self.admami1 = round(self.qq14.get() * 2.100, 3)
        self.qamah1 = round(self.qq15.get() * 0.700, 3)
        self.shair1 = round(self.qq16.get() * 1.400, 3)
        self.shofan1 = round(self.qq17.get() * 1.400, 3)
        self.zara1 = round(self.qq18.get() * 3.200, 3)
        self.adoatdd = round(float(
            self.rez1 + self.borgol1 + self.fasoli1 + self.ades1 + self.makrona1 + self.frika1 + self.homes1 + self.fol1 + self.mlah1 + self.skar1 + self.felfeahmer1 +
            self.felfeakhel1 + self.lobia1 + self.admami1 + self.qamah1 + self.shair1 + self.shofan1 + self.zara1), 3)
        self.adoat.set(f"{self.adoatdd:.3f} TND")

        self.rez2 = round(self.qqq1.get() * 2.000, 3)
        self.borgol2 = round(self.qqq2.get() * 1.500, 3)
        self.fasoli2 = round(self.qqq3.get() * 2.500, 3)
        self.ades2 = round(self.qqq4.get() * 3.900, 3)
        self.makrona2 = round(self.qqq5.get() * 3.200, 3)
        self.frika2 = round(self.qqq6.get() * 1.150, 3)
        self.homes2 = round(self.qqq7.get() * 2.200, 3)
        self.fol2 = round(self.qqq8.get() * 1.550, 3)
        self.mlah2 = round(self.qqq9.get() * 0.800, 3)
        self.skar2 = round(self.qqq10.get() * 0.750, 3)
        self.felfeahmer2 = round(self.qqq11.get() * 3.400, 3)
        self.felfeakhel2 = round(self.qqq12.get() * 0.450, 3)
        self.lobia2 = round(self.qqq13.get() * 2.200, 3)
        self.admami2 = round(self.qqq14.get() * 2.100, 3)
        self.qamah2 = round(self.qqq15.get() * 0.755, 3)
        self.shair2 = round(self.qqq16.get() * 1.400, 3)
        self.shofan2 = round(self.qqq17.get() * 1.425, 3)
        self.zara2 = round(self.qqq18.get() * 3.025, 3)

        self.madrsa = round(float(
            self.rez2 + self.borgol2 + self.fasoli2 + self.ades2 + self.makrona2 + self.frika2 + self.homes2 + self.fol2 + self.mlah2 + self.skar2 + self.felfeahmer2 +
            self.felfeakhel2 + self.lobia2 + self.admami2 + self.qamah2 + self.shair2 + self.shofan2 + self.zara2), 3)
        self.madrasa.set(f"{self.madrsa:.3f} TND")

        total = round(self.totalito + self.madrsa + self.adoatdd, 3)
        self.all = f"{total:.3f}"

    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, '\t      Bienvenu au SuperMarché El Mejri')
        self.textarea.insert(END, '\n ==============================================================')
        self.textarea.insert(END, f'\n\tFACTURE NUMÉRO   : {self.fatora.get()}')
        self.textarea.insert(END, f'\n\tNOM   :{self.nom.get()}')
        self.textarea.insert(END, f'\n\tNUMÉRO TÉLÉPHONE   :{self.phone.get()}')
        self.textarea.insert(END, '\n ==============================================================')
        self.textarea.insert(END, f'\n        Prix\t              Nombre\t               Achats')
        self.textarea.insert(END, '\n ==============================================================')

    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)
        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq18.set(0)
        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)
        self.qqq16.set(0)
        self.qqq17.set(0)
        self.qqq18.set(0)
        self.bacoliat.set(f"{0.000:.3f}")
        self.adoat.set(f"{0.000:.3f}")
        self.madrasa.set(f"{0.000:.3f}")
        self.nom.set('')
        self.phone.set('')

    def close(self):
        self.root.destroy()

    def saves(self):
        op = messagebox.askyesno('Enregistrer', 'Voulez-vous enregistrer la facture ?')
        if op:
            self.bb = self.textarea.get('1.0', END)
            file_path = os.path.join("C:\\Users\\aziz3\\Documents", str(self.fatora.get()) + '.txt')
            with open(file_path, 'w', encoding='utf-8') as f1:
                f1.write(self.bb)
                messagebox.showinfo('Enregistrement Réussi', 'Votre facture a été enregistrée avec succès.')
        else:
            return

    def billing(self):
        nom = self.nom.get().strip()
        phone = self.phone.get().strip()
        bacoliat = float(self.bacoliat.get().strip().replace(' TND', ''))
        adoat = float(self.adoat.get().strip().replace(' TND', ''))
        madrasa = float(self.madrasa.get().strip().replace(' TND', ''))

        formatted_bacoliat = f"{bacoliat:.3f} TND"
        formatted_adoat = f"{adoat:.3f} TND"
        formatted_madrasa = f"{madrasa:.3f} TND"

        if nom == "" or phone == "":
            messagebox.showerror("une erreur s'est produite",
                                 "Le champ du nom et du numéro de téléphone ne peut pas être laissé vide")
        elif not re.match("^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+$", nom):
            messagebox.showerror("une erreur s'est produite",
                                 "Le champ du nom ne peut contenir que des lettres et des caractères spéciaux autorisés")
            return
        elif not phone.isdigit() or len(phone) != 8:
            messagebox.showerror("une erreur s'est produite",
                                 "Le numéro de téléphone doit contenir exactement 8 chiffres")
            return
        elif formatted_bacoliat == '0.000 TND' and formatted_adoat == '0.000 TND' and formatted_madrasa == '0.000 TND':
            messagebox.showerror("une erreur s'est produite", "Il n'y a pas de produits sélectionnés")
            return
        else:
            self.welcome()
            if self.q1.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.rez:.3f}\t\t             {self.q1.get()}\t\t                 Riz")
            if self.q2.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.borgol:.3f}\t\t             {self.q2.get()}\t\t                 Boulgour")
            if self.q3.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fasoli:.3f}\t\t             {self.q3.get()}\t\t                 Haricot")
            if self.q4.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.ades:.3f}\t\t             {self.q4.get()}\t\t                 Lentille")
            if self.q5.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.makrona:.3f}\t\t             {self.q5.get()}\t\t                 L. Vertes")
            if self.q6.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.frika:.3f}\t\t             {self.q6.get()}\t\t                 Freekeh")
            if self.q7.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.homes:.3f}\t\t             {self.q7.get()}\t\t                 Pois Chiche")
            if self.q8.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fol:.3f}\t\t             {self.q8.get()}\t\t                 Pois Cassés")
            if self.q9.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.mlah:.3f}\t\t             {self.q9.get()}\t\t                 Sel")
            if self.q10.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.skar:.3f}\t\t             {self.q10.get()}\t\t                 Sucre")
            if self.q11.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeahmer:.3f}\t\t             {self.q11.get()}\t\t                 Poivron Noir")
            if self.q12.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeakhel:.3f}\t\t             {self.q12.get()}\t\t                 Poivron Rouge")
            if self.q13.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.lobia:.3f}\t\t             {self.q13.get()}\t\t                 Macaroni")
            if self.q14.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.admami:.3f}\t\t             {self.q14.get()}\t\t                 Flageolets")
            if self.q15.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.qamah:.3f}\t\t             {self.q15.get()}\t\t                 Vesces")
            if self.q16.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shair:.3f}\t\t             {self.q16.get()}\t\t                 Pois Sabre")
            if self.q17.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shofan:.3f}\t\t             {self.q17.get()}\t\t                 Haricot Urd")
            if self.q18.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.zara:.3f}\t\t             {self.q18.get()}\t\t                 H. Tépari")

            if self.qq1.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.rez1:.3f}\t\t             {self.qq1.get()}\t\t                Micro Onde")
            if self.qq2.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.borgol1:.3f}\t\t             {self.qq2.get()}\t\t                Aspirateur")
            if self.qq3.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fasoli1:.3f}\t\t             {self.qq3.get()}\t\t                Balai")
            if self.qq4.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.ades1:.3f}\t\t             {self.qq4.get()}\t\t                Seau")
            if self.qq5.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.makrona1:.3f}\t\t             {self.qq5.get()}\t\t                Serpillière")
            if self.qq6.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.frika1:.3f}\t\t             {self.qq6.get()}\t\t                Eponges")
            if self.qq7.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.homes1:.3f}\t\t             {self.qq7.get()}\t\t                Plumeau")
            if self.qq8.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fol1:.3f}\t\t             {self.qq8.get()}\t\t                Sacs Poubelles")
            if self.qq9.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.mlah1:.3f}\t\t             {self.qq9.get()}\t\t                Canard WC")
            if self.qq10.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.skar1:.3f}\t\t             {self.qq10.get()}\t\t                Lave-Vaisselle")
            if self.qq11.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeahmer1:.3f}\t\t             {self.qq11.get()}\t\t                Brosse")
            if self.qq12.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeakhel1:.3f}\t\t             {self.qq12.get()}\t\t                Assouplissant")
            if self.qq13.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.lobia1:.3f}\t\t             {self.qq13.get()}\t\t                Fer à Repasser")
            if self.qq14.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.admami1:.3f}\t\t             {self.qq14.get()}\t\t                Lave-Linge")
            if self.qq15.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.qamah1:.3f}\t\t             {self.qq15.get()}\t\t                Terre de Sommié")
            if self.qq16.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shair1:.3f}\t\t             {self.qq16.get()}\t\t                Cuolléres")
            if self.qq17.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shofan1:.3f}\t\t             {self.qq17.get()}\t\t                Couteau")
            if self.qq18.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.zara1:.3f}\t\t             {self.qq18.get()}\t\t                Fourchette")

            if self.qqq1.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.rez2:.3f}\t\t             {self.qqq1.get()}\t\t                Sac à Dos")
            if self.qqq2.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.borgol2:.3f}\t\t             {self.qqq2.get()}\t\t                Trousse")
            if self.qqq3.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fasoli2:.3f}\t\t             {self.qqq3.get()}\t\t                Stylos")
            if self.qqq4.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.ades2:.3f}\t\t             {self.qqq4.get()}\t\t                Gommes")
            if self.qqq5.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.makrona2:.3f}\t\t             {self.qqq5.get()}\t\t                Ciseaux")
            if self.qqq6.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.frika2:.3f}\t\t             {self.qqq6.get()}\t\t                Feutres")
            if self.qqq7.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.homes2:.3f}\t\t             {self.qqq7.get()}\t\t                Des Étiquettes")
            if self.qqq8.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.fol2:.3f}\t\t             {self.qqq8.get()}\t\t                Cahier de Texte")
            if self.qqq9.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.mlah2:.3f}\t\t             {self.qqq9.get()}\t\t                Feutre Effaçable")
            if self.qqq10.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.skar2:.3f}\t\t             {self.qqq10.get()}\t\t                Pochette")
            if self.qqq11.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeahmer2:.3f}\t\t             {self.qqq11.get()}\t\t                Crayons")
            if self.qqq12.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.felfeakhel2:.3f}\t\t             {self.qqq12.get()}\t\t                Règle Fraduée")
            if self.qqq13.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.lobia2:.3f}\t\t             {self.qqq13.get()}\t\t                Crayons à Papier")
            if self.qqq14.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.admami2:.3f}\t\t             {self.qqq14.get()}\t\t                Tube de Colle")
            if self.qqq15.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.qamah2:.3f}\t\t             {self.qqq15.get()}\t\t                Classeurs")
            if self.qqq16.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shair2:.3f}\t\t             {self.qqq16.get()}\t\t                Des Feuilles")
            if self.qqq17.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.shofan2:.3f}\t\t             {self.qqq17.get()}\t\t                Calculatrice")
            if self.qqq18.get() != 0:
                self.textarea.insert(END,
                                     f"\n        {self.zara2:.3f}\t\t             {self.qqq18.get()}\t\t                Compas")

            self.textarea.insert(END, "\n...............................................................")
            self.textarea.insert(END, f"\n                Montant Total: \t{self.all}  TND\t")
            self.textarea.insert(END, "\n...............................................................")
            self.saves()


root = Tk()
ob = super(root)
root.mainloop()
