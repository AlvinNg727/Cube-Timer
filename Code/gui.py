import tkinter as tk
import scramble

cubeTime = 0.00
timing = False

def startTimer(event):
    global timing, cubeTime
    timing = True
    cubeTime = 0.00
    window.bind("<space>", stopTimer)
    
    def start():
        if timing == True:
            global cubeTime
            cubeTime += 0.01
            timeLbl.config(text = round(cubeTime, 3))
            timeLbl.after(10, start)
    start()

def stopTimer(event):
    global timing
    timing= False
    window.bind("<space>", startTimer)

window = tk.Tk()
window.title("Cube Timer")
window.iconbitmap("icon.ico")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry("%dx%d"%(w, h))
window.state("zoomed")

#Scarmble label
scramble_Text = tk.StringVar()
scrambleLbl = tk.Label(window, textvariable = scramble_Text, font = ("Calibri", 30))
scrambleLbl.place(relx = 0.16)

#Time label
timeLbl = tk.Label(window, text = round(cubeTime, 3), font = ("Calibri", 100))
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