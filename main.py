'''
This is the main GUI
it will include multiple pages with a simple and usable interface
these pages will include drop down menus and possibly search features in order to improve usability
the pages are as follows:
 - A page to get overall event information
 - A page to get team specific information
 - A page to get team match information from a specific year

all of these will be exported to csv (or excel) files or possibly viewed within the application

Needs:
 - Get event, team, and match info and export it to a csv
 - Simple and functional interface
 - Exported as a .exe (for familiar ease of use)

Wants:
 - excel files
 - looks good
 - advanced options
 - viewing information from the application
 - searching for information from the application
 - most matches have a url for a media type object like an image or a video. A player for this media would be nice.
'''

from TBAFunctions import *
from tkinter import *

#creates root
root = Tk()
root.title("StrategyAPI")
root.geometry("400x400")

#create canvas1
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack()

# intro text for init tab
introText = "Hello! Welcome to StrategyAPI!\nTo Begin, Select an option"
canvas1.create_window(200,100, window = Label(canvas1,text = introText))

#Quit button
canvas1.create_window(350,350,window = Button(canvas1,text = "Quit", bg="red", command = root.destroy))

# get event info

# get teams

# get specific match info




# !!! TESTING USER INPUT AND STUFF !!!
'''
# - input box 
userIn = Entry(root)
canvas1.create_window(200,170, window=userIn)

def testCommand(text):
    print(text)

testButton = Button(canvas1,text = "Test",command= lambda: testCommand(userIn.get()))
canvas1.create_window(200,190, window = testButton)


# - drop down menu sample
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
'''

#Mainloop
root.mainloop()