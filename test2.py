import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.pack()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.select = tk.StringVar(None, '普通成员')
        # root.geometry('250x145')
        # root.minsize(250, 160)
        # root.maxsize(250, 160)
        root.title('登录')
        # root.iconbitmap()

        self.intWind()

    def buttonActive(self):
        u = self.username.get()
        p = self.password.get()

        if len(u) == 0 or len(p) == 0:
            messagebox.showinfo('提示：', '请完整信息')
            return

        messagebox.showinfo('提示：', '你输入的账号：%s\n密码：%s\n你的登录身份是：%s' % (u, p, self.select.get()))
        print(self.selector.cget('values'))

    def selectorLinstener(self, *args):
        self.select.set(self.selector.get())

    def dely(self):
        print(self)

    def intWind(self):
        frame1 = Frame(self)

        Label(frame1, text='账号：').grid(row=0, column=0)
        Entry(frame1, textvariable=self.username).grid(row=0, column=1)

        frame2 = Frame(self)
        Label(frame2, text='密码：').grid(row=0, column=0)
        Entry(frame2, show='*', textvariable=self.password).grid(row=0, column=1)

        frame3 = Frame(self)
        Label(frame3, text='身份：').grid(row=0, column=0)
        self.selector = ttk.Combobox(frame3, values=('普通成员', '管理员'), width='18')
        self.selector.grid(row=0, column=1)
        self.selector.current(0)
        self.selector.bind('<<ComboboxSelected>>', self.selectorLinstener)
        # self.selector.grid_forget()
        self.selector.grid_remove()
        # self.selector.grid(row=0, column=1)
        self.selector.grid()
        print(self.selector.grid_bbox(0, 0, 1, 1))
        print(self.selector.grid_location( 1, 1))
        self.selector.grid_propagate(0)

        frame3.grid(pady=6)
        frame1.grid(pady=10)
        frame2.grid(pady=6)


        #
        btn = Button(self, text='登录', width=15, command=self.buttonActive)

        print(self.grid_slaves(2,0))


        btn.grid(pady=5)
        btn.after(500, self.dely)
        btn.bell()

        print(btn.grid_size())

        # Scale(self, activebackground='#000', background='#ff0', length=500, from_=50, to=100).grid()


if __name__ == '__main__':
    root = tk.Tk()
application = Application(root=root)
application.mainloop()
