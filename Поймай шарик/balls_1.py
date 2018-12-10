from tkinter import *

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg="#ffffff")
canv.pack(fill=BOTH, expand=1)

x = y = 300
r = 130
color = "#33cc33"

canv.create_oval(x - r, y + r, x + r, y - r, fill=color)

mainloop()
