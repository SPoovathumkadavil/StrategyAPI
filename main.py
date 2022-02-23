'''
This is the main GUI
'''

import TBAFunctions as tbaFunc
from tkinter import *

#creates canvas
root = Tk()
root.title("StrategyAPI")
canvas1 = Canvas(root,width=400,height=400)
canvas1.pack()

# intro text for init tab
introText = "Hello! Welcome to StrategyAPI!\nTo Begin, Select a Tab"
canvas1.create_window(200,140, window = Label(canvas1,text = introText))

#Quit button
canvas1.create_window(350,350,window = Button(canvas1,text = "Quit", command = root.destroy))


# !!! TESTING USER INPUT AND STUFF !!!
'''
# - input box 
userIn = Entry(root)
canvas1.create_window(200,170, window=userIn)

def testCommand(text):
    print(text)

testButton = Button(canvas1,text = "Test",command= lambda: testCommand(userIn.get()))
canvas1.create_window(200,190, window = testButton)
'''

# - drop down menu
actions = ['update event info(get team information for specific events)',
           'update information for teams we will compete in the 2022 season(regional teams)',
           'get team match information from a specific year.(WARNING too much info)']
           #no im not putting these actions in a drop down menu, just for testing

label = Label(root, text = "wat dis")
label.pack()

def updateLabel(choice):
    label.config( text = choice )

variable= StringVar()
variable.set(actions[0])

#create drop down menu
drop = OptionMenu(
    root, 
    variable, 
    *actions,
    command = updateLabel #gives 1 "choice" argument to command, is the value from the given list
)
drop.pack(expand = True)

#Mainloop
root.mainloop()