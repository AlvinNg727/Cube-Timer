import tkinter as tk
import scramble
import time

timing = False

startTime = 0
endTime = 0

def startTimer(event):
    global timing, startTime
    
    timing = True
    if timing == True:
        startTime = time.time()
        window.bind("<space>", stopTimer)
        timeLbl.config(text = "Solve")

def stopTimer(event):
    global timing, endTime

    endTime = time.time()
    timing= False
    timeLbl.config(text = round(endTime - startTime, 3))
    scrambler()
    window.bind("<space>", startTimer)

window = tk.Tk()
window.title("Cube Timer")
#window.iconbitmap("icon.ico")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry("%dx%d"%(w, h))
window.state("zoomed")

#Scarmble label
scramble_Text = tk.StringVar()
scrambleLbl = tk.Label(window, textvariable = scramble_Text, font = ("Calibri", 30))
scrambleLbl.place(relx = 0.5, rely = 0.03, anchor="center")

#Time label
timeLbl = tk.Label(window, text = "0.00", font = ("Calibri", 100))
timeLbl.place(relx = 0.4, rely = 0.36)

#Calling the scramble generator
def scrambler():
    txt = scramble.call()
    scramble_Text.set(txt)
scrambler()

#Btn for generating new scramble
btn1 = tk.Button(window, text = "New scramble", command = scrambler, font = ("Calibri", 20))
btn1.place(relx = 0.43, rely = 0.07)

window.bind("<space>", startTimer)

window.mainloop()