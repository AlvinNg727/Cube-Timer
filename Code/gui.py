import tkinter as tk
import scramble
import time
import os

timing = False

startTime = 0
endTime = 0

f = open("time.txt", "a")
f.close()

pastTimes = []

def getPrevTime():
    global pastTimes
    with open("time.txt") as f:
        lines = f.readlines()
        if len(lines) >= 5:
            pastTimes = [lines[-5].strip(), lines[-4].strip(), lines[-3].strip(), lines[-2].strip(), lines[-1].strip()]
        else:
            pastTimes = []
            for i in range(len(lines)):
                pastTimes.append(lines[i].strip())
    prevTime.set("   ".join(pastTimes))
    #print(pastTimes)

def writeToFile(time):
    f = open("time.txt", "a")
    f.write(f"{str(time)}\n")
    f.close()

def startTimer(event):
    global timing, startTime
    
    timing = True
    startTime = time.time()
    window.bind("<space>", stopTimer)

    def update():
        if timing == True:
            currentTime = time.time()
            #print(round(currentTime - startTime, 2))
            timeVar.set(round(currentTime - startTime, 2))
            timeLbl.after(1, update)
    
    update()

def stopTimer(event):
    global timing, endTime

    endTime = time.time()
    timing = False
    finalTime = round(endTime - startTime, 2)
    timeVar.set(finalTime)
    writeToFile(finalTime)
    getPrevTime()
    scrambler()
    window.bind("<space>", startTimer)

window = tk.Tk()
window.title("Cube Timer")
window.iconbitmap(f"{os.getcwd()}\\Code\\icon.ico")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry("%dx%d"%(w, h))
window.state("zoomed")

#Scarmble label
scramble_Text = tk.StringVar()
scrambleLbl = tk.Label(window, textvariable = scramble_Text, font = ("Calibri", 30))
scrambleLbl.place(relx = 0.5, rely = 0.03, anchor="center")

#Calling the scramble generator
def scrambler():
    txt = scramble.call()
    scramble_Text.set(txt)
scrambler()

#Time label
timeVar = tk.StringVar()
timeLbl = tk.Label(window, textvariable = timeVar, font = ("Calibri", 100), fg = "Black")
timeLbl.place(relx = 0.5, rely = 0.5, anchor="center")
timeVar.set("0.00")

#Previous time label
prevTime = tk.StringVar()
prevLbl = tk.Label(window, textvariable = prevTime, font = ("Calibri", 30))
prevLbl.place(relx = 0.5, rely = 0.95, anchor="center")
prevTime.set("0.00")

getPrevTime()

#Btn for generating new scramble
btn1 = tk.Button(window, text = "New scramble", command = scrambler, font = ("Calibri", 20))
btn1.place(relx = 0.5, rely = 0.1, anchor="center")

window.bind("<space>", startTimer)

window.mainloop()
