# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import os


class InfoWindow(Frame):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=0, column=1)

        self.lb = Label(frame, text='文件名:')
        self.lb.pack()

        self.Ventry = StringVar()
        self.entry = Entry(frame, textvariable=self.Ventry)
        self.entry.pack()

        self.text = Text(frame, width=100, height=38)
        self.text.pack()
