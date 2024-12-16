import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('惊喜')
    window.geometry("250x48" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='傻狍子!',
             bg='pink',
             font=('LXGW WenKai Mono GB Screen', 16),
             width=128, height=2
             ).pack()
    window.mainloop()


threads = []
for i in range(90):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
