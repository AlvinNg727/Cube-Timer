import tkinter as tk
import scramble

window = tk.Tk()
window.title("Cube Timer")
window.iconbitmap("icon.ico")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry("%dx%d"%(w, h))
window.state("zoomed")

#Scarmble label
scramble_Text = tk.StringVar()
scrambleLbl = tk.Label(window, textvariable = scramble_Text, font = ("Calibri", 20))
scrambleLbl.place(relx = 0.26)

#Calling the scramble generator
def scrambler():
    txt = scramble.call()
    scramble_Text.set(txt)
scrambler()

#Btn for generating new scramble
btn1 = tk.Button(window, text = "New scramble", command = scrambler, font = ("Calibri", 15))
btn1.place(relx = 0.43, rely = 0.05)

window.mainloop()