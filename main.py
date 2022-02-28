#!usr/bin/env python3
# -*- coding: utf-8 -*-


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
 - Settings and Help page
 - Credits

Wants:
 - excel files
 - looks good
 - advanced options
 - viewing information from the application
 - searching for information from the application
 - most matches have a url for a media type object like an image or a video. A player for this media would be nice.
'''

from datetime import datetime
from TBAFunctions import *
from tkinter import *

year = int

class StratUI(Tk):

    # init app
    def __init__(self, *args, **kwargs):
        # init Tk
        Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")
        self.title("StrategyAPI")

        #create container
        container = Frame(self, bg = 'blue')
        container.pack(
            side="top",
            fill="both",
            expand=True
        )

        container.grid_rowconfigure(0, weight = 0) # weight 0 means it just takes up only necessary space at the top
        container.grid_rowconfigure(1, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # General GUI
        # this is GUI that is always on screen regardless of tab
        tabs = Frame(container, bg = 'Black') # tab selection button container
        tabs.pack(side = "top",fill = "both",expand = True)
        tabs.grid(row = 0, sticky = "nsew")
        tabs.grid_columnconfigure(0, weight = 1)
        tabs.grid_columnconfigure(1, weight = 1)
        tabs.grid_columnconfigure(2, weight = 1)
        tabs.grid_rowconfigure(0, weight = 1)

        # Ranking tab
        Button(
            tabs,
            text="Ranking",
            command=lambda: self.showFrame(Ranking)
        ).grid(row=0, column=0, sticky="nws", padx=10, pady=10)
        # Matches tab
        Button(
            tabs,
            text="Matches",
            command=lambda: self.showFrame(Matches)
        ).grid(row=0, column=1, sticky="ns", padx=10, pady=10)
        # Event Insight Tab
        Button(
            tabs,
            text="Event Insight",
            command=lambda: self.showFrame(EventInsight)
        ).grid(row=0, column=2, sticky="nes", padx=10, pady=10)


        # Tabs
        self.frames = {}

        # initalize all tabs
        for F in (StartPage, Ranking, Matches, EventInsight):  # order pages with init page first
            page = F(container, self)

            self.frames[F] = page

            page.grid(row=1, column=0, sticky="nsew")

        self.showFrame(StartPage)  # start page

    # display current frame
    def showFrame(self, cont):
        page = self.frames[cont]
        page.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        f = Frame(self)
        f.grid(row = 0, column = 0, sticky = 'nsew')
        f.pack(side = "top",fill = "both",expand = True)
        f.grid_columnconfigure(0, weight = 1)
        f.grid_rowconfigure(1, weight = 1)

        # create label
        Label(
            f,
            text = "Hello! Welcome to StrategyAPI!\nTo Begin, Select a Year"
        ).grid(row = 0, column = 0, sticky = 'n')

        # create year pick dropdown menu
        option = StringVar()
        option.set("Year")
        validYears = getValidYears()
        OptionMenu(
            f,
            option,
            *validYears,
            command = updateYear
        ).grid(row = 1, column = 0, sticky = 'n')


# Ranking Information
class Ranking(Frame):
    eventID = int

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid(row = 0, column = 0, sticky = 'nsew')

        # init frame
        f = Frame(self)
        f.grid(row = 0, column = 0, sticky = 'nsew')
        f.pack(side = "top",fill = "both",expand = True)
        f.grid_columnconfigure(0, weight = 1)
        f.grid_rowconfigure(0, weight = 1)

        # create label
        Label(f,
            text = "Overall Event Information"
        ).grid(row = 0, column = 0, sticky = 'nsew')

        # run button
        Button(f,
            text = "Run",
            command = lambda : print("nice")
        ).grid(row = 0, column = 0, sticky = "se", padx = 10, pady = 10)


# Match information
class Matches(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        f = Frame(self)
        f.grid(row=0, column=0)
        f.grid_columnconfigure(0, weight=1)
        f.grid_rowconfigure(0, weight=1)

        # intro text for init tab
        MatchesText = "Matches Information"

        # create label
        Label(
            self,
            text=MatchesText
        ).grid(row=0, column=0, sticky='n')


# Event Insight
class EventInsight(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        f = Frame(self)
        f.grid(row=0, column=0)
        f.grid_columnconfigure(0, weight=1)
        f.grid_rowconfigure(0, weight=1)

        # intro text for init tab
        EventInsightText = "Event Insight Tab"

        # create label
        Label(
            self,
            text=EventInsightText
        ).grid(row=0, column=0, sticky='n')


# Data functions
def getValidYears():
    validYears = []
    for i in range(1991, datetime.today().year):
        validYears.append(i)
    return validYears

def updateYear(choice):
    global year
    year = int(choice)

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

# Mainloop
StratUI().mainloop()
