from tkinter import *
from win32api import GetSystemMetrics
import webbrowser


ScreenX = GetSystemMetrics(0)
ScreenY = GetSystemMetrics(1)
screen = Tk()

class Main:

    def __init__(self, master):

        # Цыганские фокусы для окна
        self.Hidden = 0
        self.window = master
        self.window.title("Clone Bounce")
        self.window.geometry(f'285x350+{int((ScreenX - 285) / 2)}+{int((ScreenY - 400) / 2)}')
        self.window.resizable(False, False)
        self.window.attributes('-fullscreen', False)
        self.window.overrideredirect(1)

        self.Startfr = Frame(master, width=285, bg='#151515')
        self.Startfr.pack(fill=Y, side=LEFT)

        # Заголовок игры
        self.game_title = Label(self.Startfr, text='Clone Bounce', font=('Arial', 30), cursor='hand2')
        self.game_title.config(bg='#151515', activebackground='#151515', fg='grey')
        self.game_title.place(x=20, y=50)

        # Кнопка запуска синглплеера
        self.StartbtnSingle = Button(self.Startfr, text='SINGLE PLAY', border=0, command=self.btnStartSingle, cursor='hand2', font=17)
        self.StartbtnSingle.config(bg='#202020', activebackground='#151515', activeforeground='grey', fg='grey')
        self.StartbtnSingle.bind("<Enter>", self.inStart)
        self.StartbtnSingle.bind("<Leave>", self.outStart)
        self.StartbtnSingle.place(x=89, y=140)

        # Кнопка запуска мультиплеера
        self.Startbtn_mp = Button(self.Startfr, text='MULTIPLAYER', border=0, command=self.btnStart, cursor='hand2',
                               font=17)
        self.Startbtn_mp.config(bg='#202020', activebackground='#151515', activeforeground='grey', fg='grey')
        self.Startbtn_mp.bind("<Enter>", self.inStart_mp)
        self.Startbtn_mp.bind("<Leave>", self.outStart_mp)
        self.Startbtn_mp.place(x=86, y=200)

        # Выход из лаунчера
        self.Exitlbl = Label(self.Startfr, text='Exit', font=('Arial', 12), cursor='hand2')
        self.Exitlbl.bind('<Button-1>', self.close)
        self.Exitlbl.bind('<Enter>', self.inStart_ex)
        self.Exitlbl.bind('<Leave>', self.outStart_ex)
        self.Exitlbl.config(bg='#151515', activebackground='#151515', activeforeground='grey', fg='grey')
        self.Exitlbl.place(x=125, y=283)

        # Титры
        self.by = Label(self.Startfr, text='By CR4CKKER, GaLeon and YENOGGY', font=('Arial', 8))
        self.by.config(bg='#151515', activebackground='#151515', activeforeground='grey', fg='grey')
        self.by.place(x=45, y=310)
        self.by.bind('<Button-1>', self.github)
        self.by.bind('<Enter>', self.inBy)
        self.by.bind('<Leave>', self.outBy)


    # Запуск сингла
    def btnStartSingle(self):
        import main
        self.window.destroy()

    # Закрытие окна
    def close(self, event):
        self.window.destroy()

    # Ссылка на гит
    def github(self, event):
        webbrowser.open('https://github.com/Yenoggy/Clone-Bounce', new=2)


    # Эффекты
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

    def inBy(self, event):
        self.by.config(bg='#151515', activebackground='#151515', fg='white', font='Arial 8 underline')

    def outBy(self, event):
        self.by.config(bg='#151515', activebackground='#151515', fg='grey', font='Arial 8')

# Запуск лаунчера
if __name__ == '__main__':
    app = Main(screen)
    screen.mainloop()