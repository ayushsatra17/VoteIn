import sqlite3
from tkinter import *
from PIL import Image,ImageTk

connection = sqlite3.connect('db/Voters.db')

class loginPage():
    def __init__(self, master):
        self.label1 = Label(master, text="Username")
        self.label2 = Label(master, text="Voter_Id")
        self.entry1 = Entry(master)
        self.entry2 = Entry(master,show="*")
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.button1 = Button(master, text="Login",command=self.new)
        self.button2 = Button(master, text="Polls",command=self.Result)
        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)

    def new(self):
        self.username = self.entry1.get()
        self.id = self.entry2.get()
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()

        sql1 = ' SELECT * FROM Voters WHERE NAME LIKE ? AND VOTERID LIKE ? AND VOTED LIKE "0" '
        cursor.execute(sql1, (self.username, self.id))

        s1 = ' SELECT VOTERID FROM VOTERS WHERE NAME LIKE ? and VOTED LIKE "0" '
        cursor1.execute(s1, (self.username,))

        s2 = ' SELECT VOTERID,VOTED FROM VOTERS WHERE NAME LIKE ? '
        cursor2.execute(s2, (self.username,))

        if cursor.fetchone() is not None:
            self.tp = Toplevel()
            self.label3 = Label(self.tp, text="SUCCESSFUL LOGIN")
            self.label3.pack()
            sql2 = 'UPDATE VOTERS SET VOTED = 1 WHERE NAME LIKE ?'
            cursor.execute(sql2, (self.username,))
            connection.commit()
            self.button3 = Button(self.tp, text="VOTE",command=self.vote)
            self.button3.pack(side=LEFT)
        else:
            self.tp = Toplevel()
            self.label3 = Label(self.tp, text="UNSUCCESSFUL LOGIN")
            self.label3.pack()

    def vote(self):
        self.tp1=Toplevel()
        self.tp1.geometry('400x550')
        self.x = StringVar()

        self.photo1 = Image.open('C:\\Users\\dell\\PycharmProjects\\Project-Python\\bjp.png')
        self.photo1 = self.photo1.resize((150, 100), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.photo1)
        self.label4 = Label(self.tp1, image=self.image1)
        self.label4.grid(row=0, column=0)
        self.r1 = Radiobutton(self.tp1, variable=self.x, value="BJP", command=self.invoke, indicatoron=0, text="BJP")
        self.r1.config(font=("courier", 15))
        self.r1.grid(row=0, column=1)

        self.photo2 = Image.open('C:\\Users\\dell\\PycharmProjects\\Project-Python\\congress.png')
        self.photo2 = self.photo2.resize((100, 100), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.photo2)
        self.label5 = Label(self.tp1,image=self.image2)
        self.label5.grid(row=1, column=0)
        self.r2 = Radiobutton(self.tp1, variable=self.x, text="CONGRESS", value="CONGRESS", command=self.invoke, indicatoron=0)
        self.r2.config(font=("courier", 15))
        self.r2.grid(row=1, column=1)

        self.photo3 = Image.open('C:\\Users\\dell\\PycharmProjects\\Project-Python\\bsp.png')
        self.photo3 = self.photo3.resize((150, 100), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.photo3)
        self.label6 = Label(self.tp1, image=self.image3)
        self.label6.grid(row=2, column=0)
        self.r3 = Radiobutton(self.tp1, variable=self.x, value="BSP", command=self.invoke, indicatoron=0, text="BSP")
        self.r3.config(font=("courier", 15))
        self.r3.grid(row=2, column=1)

        self.photo4 = Image.open('C:\\Users\\dell\\PycharmProjects\\Project-Python\\ncp.png')
        self.photo4 = self.photo4.resize((150, 100), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(self.photo4)
        self.label7 = Label(self.tp1, image=self.image4)
        self.label7.grid(row=3, column=0)
        self.r4 = Radiobutton(self.tp1, variable=self.x, value="NCP", command=self.invoke, indicatoron=0, text="NCP")
        self.r4.config(font=("courier", 15))
        self.r4.grid(row=3, column=1)

        self.photo5 = Image.open('C:\\Users\\dell\\PycharmProjects\\Project-Python\\aap.png')
        self.photo5 = self.photo5.resize((150, 100), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(self.photo5)
        self.label8 = Label(self.tp1, image=self.image5)
        self.label8.grid(row=4, column=0)
        self.r5 = Radiobutton(self.tp1, variable=self.x, value="AAP", command=self.invoke, indicatoron=0, text="AAP")
        self.r5.config(font=("courier", 15))
        self.r5.grid(row=4, column=1)

    def invoke(self):
        self.var = self.x.get()
        connection1 = sqlite3.connect('db/Party.db')
        cursor1 = connection1.cursor()
        sql2 = ' UPDATE PARTY SET VOTE = VOTE+1 WHERE PARTY_NAME LIKE ? '
        cursor1.execute(sql2, (self.var,))
        connection1.commit()
        self.tp.destroy()
        self.tp1.destroy()
        self.entry1.delete(0,'end')
        self.entry2.delete(0, 'end')

    def Result(self):
        self.tp3=Toplevel()
        self.l1= Label(self.tp3, text="ADMIN-NAME")
        self.l2 = Label(self.tp3, text="PASSWORD")
        self.e1 = Entry(self.tp3)
        self.e2 = Entry(self.tp3,show='*')
        self.l1.grid(row=0, column=0)
        self.l2.grid(row=1, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.button1 = Button(self.tp3, text="LOGIN", command=self.Verify)

        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)

    def Verify(self):
        c = sqlite3.connect('db/Admin.db')
        a = c.cursor()
        self.name = self.e1.get()
        self.password = self.e2.get()
        cu = c.cursor()
        sql5 = ' SELECT * FROM ADMIN WHERE NAME LIKE ? AND Password LIKE ? '
        cu.execute(sql5, (self.name, self.password))
        if cu.fetchone() is not None :
            import matplotlib.pyplot as plt
            conn = sqlite3.connect('db/Party.db')
            curs = conn.cursor()
            x = ['BJP', 'CONGRESS', 'NCP', 'BSP', 'AAP']
            y = []
            for i in range(len(x)):
                q = ' SELECT VOTE FROM PARTY WHERE PARTY_NAME LIKE ? '
                curs.execute(q, (x[i],))
                z = curs.fetchone()[0]
                y.append(z)

            N = len(y)
            width = 1 / 1.5
            plt.bar(x, y, width, color="yellow")
            plt.ylabel('VOTES--->')
            plt.xlabel('PARTIES---->')
            fig = plt.gcf()
            fig.show()

root = Tk()
a = loginPage(root)
root.mainloop()

