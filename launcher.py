from tkinter import *
from win32api import GetSystemMetrics


ScreenX = GetSystemMetrics(0)
ScreenY = GetSystemMetrics(1)
screen = Tk()

class Main:

    def __init__(self, master):

        self.Hidden = 0
        self.window = master
        self.window.title("Clone Bounce")
        self.window.geometry(f'285x350+{int((ScreenX - 285) / 2)}+{int((ScreenY - 400) / 2)}')
        self.window.resizable(False, False)
        self.window.attributes('-fullscreen', False)
        self.window.overrideredirect(1)

        self.Startfr = Frame(master, width=285, bg='#151515')
        self.Startfr.pack(fill=Y, side=LEFT)

        self.game_title = Label(self.Startfr, text='Clone Bounce', font=('Arial', 30), cursor='hand2')
        self.game_title.config(bg='#151515', activebackground='#151515', fg='grey')
        self.game_title.place(x=20, y=50)

        self.Startbtn = Button(self.Startfr, text='SINGLE PLAY', border=0, command=self.btnStart, cursor='hand2', font=17)
        self.Startbtn.config(bg='#202020', activebackground='#151515', activeforeground='grey', fg='grey')
        self.Startbtn.bind("<Enter>", self.inStart)
        self.Startbtn.bind("<Leave>", self.outStart)
        self.Startbtn.place(x=89, y=140)

        self.Startbtn_mp = Button(self.Startfr, text='MULTIPLAYER', border=0, command=self.btnStart, cursor='hand2',
                               font=17)
        self.Startbtn_mp.config(bg='#202020', activebackground='#151515', activeforeground='grey', fg='grey')
        self.Startbtn_mp.bind("<Enter>", self.inStart_mp)
        self.Startbtn_mp.bind("<Leave>", self.outStart_mp)
        self.Startbtn_mp.place(x=86, y=200)

        self.Exitlbl = Label(self.Startfr, text='Exit', font=('Arial', 12), cursor='hand2')
        self.Exitlbl.bind('<Button-1>', self.close)
        self.Exitlbl.bind('<Enter>', self.inStart_ex)
        self.Exitlbl.bind('<Leave>', self.outStart_ex)
        self.Exitlbl.config(bg='#151515', activebackground='#151515', activeforeground='grey', fg='grey')
        self.Exitlbl.place(x=125, y=283)

    def btnStart(self):
        import main
        self.window.destroy()

    def close(self, event):
        self.window.destroy()

    def inStart(self, event):
        self.Startbtn.config(bg='#202020', activebackground='#151515', fg='white')

    def outStart(self, event):
        self.Startbtn.config(bg='#202020', activebackground='#151515',  fg='grey')

    def inStart_mp(self, event):
        self.Startbtn_mp.config(bg='#202020', activebackground='#151515', fg='white')

    def outStart_mp(self, event):
        self.Startbtn_mp.config(bg='#202020', activebackground='#151515',  fg='grey')

    def inStart_ex(self, event):
        self.Exitlbl.config(bg='#151515', activebackground='#151515', fg='white', font='Arial 12 underline')

    def outStart_ex(self, event):
        self.Exitlbl.config(bg='#151515', activebackground='#151515', fg='grey', font='Arial 12')


if __name__ == '__main__':
    app = Main(screen)
    screen.mainloop()