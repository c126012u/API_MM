#!/usr/bin/env python
"""
http://37444.jp/tkintertips/event.html
"""
import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
         width=10,
         height=2,
         text="Hello!!",
)
def print_click(event):
    print("Clicked\n")
l.bind("<Button-1>", print_click)
l.pack()

root.mainloop()
