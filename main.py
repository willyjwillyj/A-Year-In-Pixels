import tkinter as tk
import pickle
import os

root = tk.Tk(className="a year in pixels")
root.geometry("1200x900")
def processInput():
    setData()
    renderData()

def setData():
    path = "saveData"
    data = []

    if os.path.isfile(path=path):
        f = open(path,"rb")
        data = pickle.load(f)
        f.close()
    else: 
        data = [[],[],[],[],[],[],[],[],[],[],[],[]]
        
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(12):
            for ii in range(days[i]):
                data[i].append("#ffffff")
            for ii in range(31 - days[i]):
                data[i].append("#000000")
    global optionColorer
    global optionInput
    global monthInput
    global dateInput
    data[int(monthInput.get())-1][int(dateInput.get())-1] = optionColorer[optionInput.get()]
    f = open(path, "wb")
    pickle.dump(data, f)
    f.close()

def renderData():
    buildBorder()
    colorItems()
    buildKey()

def buildBorder():
    global canvas
    global border
    global mainWidth
    global mainHeight
    totalWidth = 14*border + 13*mainWidth
    totalHeight = 33*border + 32*mainHeight
    for i in range(14):
        canvas.create_rectangle((border + mainWidth)*i, 0, (border + mainWidth)*i + border, totalHeight, fill="#000000")
    for i in range(33):
        canvas.create_rectangle(0, (border + mainHeight)*i, totalWidth, (border+mainHeight)* i + border, fill="#000000")


def colorItems():
    path = "saveData"
    global canvas
    global border
    global mainWidth
    global mainHeight
    f = open(path,"rb")
    data = pickle.load(f)
    f.close()
    for i in range(len(data)):
        for ii in range(len(data[i])):
            canvas.create_rectangle((mainWidth+border) * (i + 1) + border, (mainHeight + border) * (ii + 1) + border, (mainWidth + border)*(i + 2), (mainHeight + border)* (ii + 2), fill=data[i][ii])

def buildKey():
    global canvas
    global border
    global mainWidth
    global mainHeight
    global options
    global optionColorer
    totalWidth = 14*border + 13*mainWidth
    totalHeight = 33*border + 32*mainHeight
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY", "AUG", "SEP", "OCT", "NOV", "DEC"]
    for i in range(12):
        canvas.create_text((i + 1) * (border + mainWidth) + border + mainWidth*0.5, border + mainHeight * 0.5,anchor=tk.CENTER,text=months[i])
    for i in range(31):
        canvas.create_text(border+mainWidth*0.5, (i + 1) * (border + mainHeight) + border + mainHeight * 0.5, anchor=tk.CENTER, text=str(i+1))
    for i in range(len(options)-2):
        canvas.create_text(totalWidth + 350, 200 + 50 * i, anchor=tk.E, text=options[i])
        canvas.create_rectangle(totalWidth + 375,200 + 50 * i - border - mainHeight * 0.5,totalWidth + 375 + border + border + mainWidth, 200 + 50 * i + border + mainHeight * 0.5, fill="#000000")
        canvas.create_rectangle(totalWidth + 375,200 + 50 * i - border - mainHeight * 0.5,totalWidth + 375 + border + border + mainWidth, 200 + 50 * i + border + mainHeight * 0.5, fill=optionColorer[options[i]])


options = [
    "Amazing, Fantastic day",
    "Really good, Happy day",
    "Normal, average day",
    "Exhausted, tired day",
    "Depressed, sad day",
    "Frustrated, angry day",
    "Stressed out, Anxious day",
    "Clear",
    "Black"
]

optionColorer = {
    "Amazing, Fantastic day": "#F6A5F4",
    "Really good, Happy day": "#A5F5E8",
    "Normal, average day": "#F7F5A4",
    "Exhausted, tired day": "#A7F5A9",
    "Depressed, sad day": "#6F62E5",
    "Frustrated, angry day": "#E67A70",
    "Stressed out, Anxious day": "#E4AC62",
    "Clear": "#FFFFFF",
    "Black": "#000000",
}

monthList = []
dayList = []

for i in range(1,32):
    dayList.append(str(i))

for i in range(1,13):
    monthList.append(str(i))


title = tk.Frame(master=root)
titleLabel = tk.Label(master=title, text="A Year In Pixels")
titleLabel.pack(side=tk.TOP)

inputArea = tk.Frame(master=root)

optionInput = tk.StringVar()
optionInput.set("Normal, average day")

monthInput = tk.StringVar()
monthInput.set("1")

dateInput = tk.StringVar()
dateInput.set("1")

optionFrame = tk.Frame(master=inputArea)
monthFrame = tk.Frame(master=inputArea)
dayFrame = tk.Frame(master=inputArea)


optionFrame.pack(side=tk.LEFT)
monthFrame.pack(side=tk.LEFT)
dayFrame.pack(side=tk.LEFT)

optionLabel = tk.Label(optionFrame, text="How Was Your Day?")
monthLabel = tk.Label(monthFrame, text="Select Today's Month")
dayLabel = tk.Label(dayFrame, text="Select Today's Date")

optionLabel.pack(side=tk.TOP)
monthLabel.pack(side=tk.TOP)
dayLabel.pack(side=tk.TOP)


optionDrop = tk.OptionMenu(optionFrame, optionInput, *options)
monthDrop = tk.OptionMenu(monthFrame, monthInput, *monthList)
dayDrop = tk.OptionMenu(dayFrame, dateInput, *dayList)

optionDrop.pack(side=tk.TOP)
monthDrop.pack(side=tk.TOP)
dayDrop.pack(side=tk.TOP)

submitButton = tk.Button(root, text="Submit", command=processInput)

displayArea = tk.Frame(master=root)


border = 2
mainWidth = 50
mainHeight = 20
canvas = tk.Canvas(displayArea, width=(14*border + 13*mainWidth + 500), height=(33*border + 32*mainWidth))
canvas.pack(side=tk.TOP)



title.pack(side=tk.TOP)
inputArea.pack(side=tk.TOP)
submitButton.pack(side=tk.TOP)
displayArea.pack(side=tk.TOP)
root.mainloop()
