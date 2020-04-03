import re
import requests
import tkinter as tk
import webbrowser
from tkinter import messagebox
response = requests.get('http://www.qmaile.com/')

response.encoding = response.apparent_encoding
response = response.text

reg=re.compile('<option value="(.*?)" selected="">')

res = re.findall(reg,response)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]

root = tk.Tk()
root.title('Vip_Movie')
root.geometry('500x250+100+100')

l1 = tk.Label(root, text='播放接口:', font=("Arial",12),)

l1.grid(row=0, column=0)
l2 = tk.Label(root, text='播放链接:', font=("Arial",12),)
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)

var = tk.StringVar(value=None)
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one,)
r1.grid(row=0, column=1,)
var.set(r1)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two,)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three,)
r3.grid(row=2,column=1)
r4 = tk.Radiobutton(root,text='播放接口4', variable=var, value=four,)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放接口5', variable=var, value=five,)
r5.grid(row=4, column=1)


def help_():
    messagebox.showinfo("帮助信息", message="请把想看的视频链接放到输入框即可！")


def author_info():
    messagebox.showinfo("联系更新", message="Author：善念")


menu = tk.Menu(root)
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='帮助(H)', menu=help_menu)
help_menu.add_command(label='帮助文档',command=help_)
help_menu.add_command(label='作者信息', command=author_info)
root.config(menu=menu)


def play_movie():
    webbrowser.open(var.get()+t1.get())


b1 = tk.Button(root,text='播放', font=("Arial",14), width=8, command=play_movie)
b1.grid(row=7, column=1)


def del_text():
    t1.delete(0, 'end')


b2 = tk.Button(root, text='清除', font=("Arial", 12), width=8, command=del_text)
b2.grid(row=8, column=1)

root.mainloop()




