
import ctypes

x11 = ctypes.cdll.LoadLibrary("libX11.so")

x11.XInitThreads()

import tkinter as tk

app = tk.Tk()
button = tk.Button(app, text="Press me")
button.pack()
app.mainloop()
