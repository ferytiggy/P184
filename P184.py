# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:23:55 2024

@author: Aidan
"""

from tkinter import*
import requests
import json

root = Tk()
root.geometry("650x450")
root.title("P184")

newsupdate = Label(root, text="Actualización de noticias de la BBC")
newsupdate.place(relx=0.5, rely=0.1, anchor=CENTER)

news1 = Label(root, wraplength=500)
news1.place(relx=0.5, rely=0.15, anchor=CENTER)
news1_desc = Label(root, wraplength=500)
news1_desc.place(relx=0.5, rey=0.2, anchor=CENTER)

news2 = Label(root, wraplength=500)
news2.place(relx=0.5, rely=0.25, anchor=CENTER)
news2_desc = Label(root, wraplength=500)
news2_desc.place(relx=0.5, rely=0.3, anchor=CENTER)

news3 = Label(root, wraplength=500)
news3.place(relx=0.5, rely=0.35, anchor=CENTER)
news3_desc = Label(root, wraplength=500)
news3_desc.place(relx=0.5, rely=0.4, anchor=CENTER)

news4 = Label(root, wraplength=500)
news4.place(relx=0.5, rely=0.45, anchor=CENTER)
news4_desc = Label(root, wraplength=500)
news4_desc.place(relx=0.5, rely=0.5, anchor=CENTER)

news5 = Label(root, wraplength=500)
news5.place(relx=0.5, rely=0.55, anchor=CENTER)
news5_desc = Label(root, wraplength=500)
news5_desc.place(relx=0.5, rely=0.6, anchor=CENTER)

api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d19e527b11df48c0bcc07c26dfe0a65e")
api_output_json.loads(api_request.content)
t1=["articles"][0]["title"]
d1=["articles"][0]["description"]
t2=["articles"][1]["title"]
d2=["articles"][1]["description"]
t3=["articles"][2]["title"]
d3=["articles"][2]["description"]
t4=["articles"][3]["title"]
d4=["articles"][3]["description"]
t5=["articles"][4]["title"]
d5=["articles"][4]["description"]

news1["text"] = "Titulo 1 " + src(t1)
news2["text"] = "Titulo 2 " + src(t2)
news3["text"] = "Titulo 3 " + src(t3)
news4["text"] = "Titulo 4 " + src(t4)
news5["text"] = "Titulo 5 " + src(t5)

news1_desc["text"] = "Descripción " + src(d1)
news2_desc["text"] = "Descripción " + src(d2)
news3_desc["text"] = "Descripción " + src(d3)
news4_desc["text"] = "Descripción " + src(d4)
news5_desc["text"] = "Descripción " + src(d5)

 

root.mainloop()