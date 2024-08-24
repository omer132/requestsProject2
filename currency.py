import tkinter as tk
import requests as rp
from tkinter import messagebox

window = tk.Tk()
window.geometry("400x400")

def v():
    c = inp.get()
    if len(c) == 0:
        messagebox.showerror(title="Hata", message="Lütfen bir veri girin")
        return 

    found = False
    for i in y:
        if i["currency"] == c:
            k=(i["price"])
            m.config(text=k)
            found = True
            break

    if not found:
        messagebox.showerror(title="Hata", message="Aradığınız şey burada bulunamadı")

x = rp.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
y = x.json()

k = tk.Label(text="Lütfen bir kripto para birimi girin:")
k.place(relx=0.5, rely=0.5, anchor="center")

inp = tk.Entry(window, width=30)
inp.place(relx=0.5, rely=0.6, anchor="center")

m=tk.Label(text="")
m.place(relx=0.5,rely=0.7, anchor="center")

b = tk.Button(text="Devam", command=v)
b.place(relx=0.5, rely=0.8, anchor="center")

window.mainloop()
