#!usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This is the main GUI
it will include multiple pages with a simple and usable interface
these pages will include drop down menus and possibly search features in order to improve usability
the pages are as follows:
 - A page to get overall event information
 - A page to get team specific information
 - A page to get team match information from a specific year

all of these will be exported to csv (or excel) files or possibly viewed within the application

Needs:
 - HEE HEE HEE HAW
 - Work
 - Get event, team, and match info and export it to a csv
 - Simple and functional interface
 - Exported as a .exe (for familiar ease of use)
 - Settings and Help page
 - Credits

Wants:
 - Excel files
 - looks good
 - advanced options
 - viewing information from the application
 - searching for information from the application
 - most matches contain url for a media type object like an image or a video. A player for this media would be nice.
"""

__author__ = "Riley Carter"
__credits__ = "Riley Carter"
__license__ = "FRC4500"
__maintainer__ = "Riley Carter"
__status__ = "Development"
__version__ = "0.1.0"

from datetime import datetime
from TBAFunctions import *
from tkinter import *

year = str(datetime.today().year)


class StratUI(Tk):

    # init app
    def __init__(self, *args, **kwargs):
        # init Tk
        Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("StrategyAPI")

        # create container
        container = Frame(self, bg='blue')
        container.pack(
            side="top",
            fill="both",
            expand=True
        )

        container.grid_rowconfigure(0, weight=0)  # weight 0 means it just takes up only necessary space at the top
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # General GUI
        # this is GUI that is always on screen regardless of tab
        tabs = Frame(container, bg='Black')  # tab selection button container
        tabs.pack(side="top", fill="both", expand=True)
        tabs.grid(row=0, sticky="nsew")
        tabs.grid_columnconfigure(0, weight=1)
        tabs.grid_columnconfigure(1, weight=1)
        tabs.grid_columnconfigure(2, weight=1)
        tabs.grid_columnconfigure(3, weight=1)
        tabs.grid_rowconfigure(0, weight=1)

        # Ranking tab
        Button(
            tabs,
            text="Home",
            command=lambda: self.showFrame(StartPage)
        ).grid(row=0, column=0, sticky="nwe", padx=10, pady=10)
        Button(
            tabs,
            text="Ranking",
            command=lambda: self.showFrame(Ranking)
        ).grid(row=0, column=1, sticky="nwe", padx=10, pady=10)
        # Matches tab
        Button(
            tabs,
            text="Matches",
            command=lambda: self.showFrame(Matches)
        ).grid(row=0, column=2, sticky="nwe", padx=10, pady=10)
        # Event Insight Tab
        Button(
            tabs,
            text="Event Insight",
            command=lambda: self.showFrame(EventInsight)
        ).grid(row=0, column=3, sticky="nwe", padx=10, pady=10)

        # Tabs
        self.frames = {}

        # initialize all tabs
        for F in (StartPage, Ranking, Matches, EventInsight):  # order pages with init page first
            page = F(container, self)

            self.frames[F] = page

            page.grid(row=1, column=0, sticky="nsew")

        self.showFrame(StartPage)  # start page

    # display current frame
    def showFrame(self, cont):
        self.updateFrames()
        page = self.frames[cont]
        page.tkraise()

    def updateFrames(self):
        self.frames[Ranking].eventScrollable.updateEvents()
        self.frames[Matches].eventScrollable.updateEvents()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        f = Frame(self)
        f.grid(row=0, column=0, sticky='nsew')
        f.pack(side="top", fill="both", expand=True)
        f.grid_columnconfigure(0, weight=1)
        f.grid_rowconfigure(1, weight=1)

        # create label
        Label(
            f,
            text="Hello! Welcome to StrategyAPI!\nTo Begin, Select a Year"
        ).grid(row=0, column=0, sticky='n')

        # create year pick dropdown menu
        option = StringVar()
        option.set("Year")
        validYears = getValidYears()
        OptionMenu(
            f,
            option,
            *validYears,
            command=updateYear
        ).grid(row=1, column=0, sticky='n')


# Ranking Information
class Ranking(Frame):
    def __init__(self, parent, controller):
        self.eventID = int
        global year
        Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky='nsew')

        # init frame
        f = Frame(self)
        f.grid(row=0, column=0, sticky='nsew')
        f.pack(side="top", fill="both", expand=True)
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(1, weight=0)
        f.grid_rowconfigure(0, weight=0)
        f.grid_rowconfigure(1, weight=1)

        # create label
        Label(f,
              text="Ranking Information Tab"
              ).grid(row=0, columnspan=2, sticky='n')

        # init event Scrollable
        self.eventScrollable = EventScrollable(f, self)

        # options frame
        optFrame = Frame(f)
        optFrame.grid(row=1, column=1, sticky='nse', padx=10, pady=10)
        optFrame.grid_rowconfigure(0, weight=0)
        optFrame.grid_rowconfigure(1, weight=1)
        optFrame.grid_columnconfigure(0, weight=0)

        # Competition Toggle
        self.competition = False
        isComp = BooleanVar()
        compCheck = Checkbutton(optFrame, text="Competition", variable=isComp, onvalue=True, offvalue=False,
                                command=lambda: self.updateCompetition(isComp))
        compCheck.grid(row=0, column=0, sticky='nw')

        # Advanced Toggle
        self.isAdvanced = False
        isAdvancedVar = BooleanVar()
        advCheck = Checkbutton(optFrame, text="Advanced", variable=isAdvancedVar, onvalue=True, offvalue=False,
                               command=lambda: self.update_isAdvanced(isAdvancedVar))
        advCheck.grid(row=1, column=0, sticky='nw')

        # run button
        Button(optFrame,
               text="Run",
               command=lambda: self.runRankingInfo()
               ).grid(row=1, column=0, sticky="se")

    def runRankingInfo(self):
        if self.competition:
            print("Competition is true")
        else:
            print("Competition is false")
        print("Event ID:" + self.eventScrollable.eventID)

        print("Processing...")
        get_ranking(self.competition, year, self.eventScrollable.eventID)  # TODO sal pls fix

        print("Done!")

    def updateCompetition(self, isComp):
        self.competition = isComp.get()


# Match information
class Matches(Frame):

    def __init__(self, parent, controller):
        global year
        Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky='nsew')

        # init frame
        f = Frame(self)
        f.grid(row=0, column=0, sticky='nsew')
        f.pack(side="top", fill="both", expand=True)
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(1, weight=1)
        f.grid_columnconfigure(2, weight=0)
        f.grid_rowconfigure(0, weight=0)
        f.grid_rowconfigure(1, weight=1)

        # create label
        Label(
            f,
            text="Matches Information"
        ).grid(row=0, columnspan=3, sticky='n')

        # init scrollable event frame
        self.eventScrollable = EventScrollable(f, self)

        # init scrollable teams list
        self.teamsScrollable = TeamsScrollable(f, self)

        # options frame
        optFrame = Frame(f)
        optFrame.grid(row=1, column=2, sticky='nse', padx=10, pady=10)
        optFrame.grid_rowconfigure(0, weight=0)
        optFrame.grid_rowconfigure(1,weight=1)
        optFrame.grid_columnconfigure(0, weight=1)

        # Competition Toggle
        self.competition = False
        isComp = BooleanVar()
        compCheck = Checkbutton(optFrame, text="Competition", variable=isComp, onvalue=True, offvalue=False,
                                command=lambda: self.updateCompetition(isComp))
        compCheck.grid(row=0, column=0, sticky='nw')

        # Advanced Toggle
        self.isAdvanced = False
        isAdvancedVar = BooleanVar()
        advCheck = Checkbutton(optFrame, text="Advanced", variable=isAdvancedVar, onvalue=True, offvalue=False,
                               command=lambda: self.update_isAdvanced(isAdvancedVar))
        advCheck.grid(row=1, column=0, sticky='nw')

        Button(optFrame,
               text="Run",
               command=lambda: self.runMatchInfo()
               ).grid(row=1, column=0, sticky="se")

    def runMatchInfo(self):
        if self.isAdvanced:
            print("Advanced is true")
        else:
            print("Advanced is false")

        if self.competition:
            print("Competition is true")
        else:
            print("Competition is false")
        print("Event ID:" + self.eventScrollable.eventID)
        print("Team: " + str(self.teamsScrollable.teamNumber))

        print("Processing...")
        get_matches(self.teamsScrollable.teamNumber, self.competition, year, self.eventScrollable.eventID,
                    not self.isAdvanced)

        print("Done!")

    def updateCompetition(self, isComp):
        self.competition = isComp.get()

    def update_isAdvanced(self, isAdvancedVar):
        self.isAdvanced = isAdvancedVar.get()


# Event Insight
class EventInsight(Frame):

    def __init__(self, parent, controller):
        self.eventID = int
        global year
        Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky='nsew')

        # init frame
        f = Frame(self)
        f.grid(row=0, column=0, sticky='nsew')
        f.pack(side="top", fill="both", expand=True)
        f.grid_columnconfigure(0, weight=1)
        f.grid_rowconfigure(0, weight=0)
        f.grid_rowconfigure(1, weight=1)

        # create label
        Label(f,
              text="Event Insight Page"
              ).grid(row=0, columnspan=2, sticky='n')

        # init event Scrollable
        self.eventScrollable = EventScrollable(f, self)

        # options frame
        optFrame = Frame(f)
        optFrame.grid(row=1, column=2, sticky='nse', padx=10, pady=10)
        optFrame.grid_rowconfigure(0, weight=0)
        optFrame.grid_rowconfigure(1, weight=1)
        optFrame.grid_columnconfigure(0, weight=1)

        # Competition Toggle
        self.competition = False
        isComp = BooleanVar()
        compCheck = Checkbutton(optFrame, text="Competition", variable=isComp, onvalue=True, offvalue=False,
                                command=lambda: self.updateCompetition(isComp))
        compCheck.grid(row=0, column=0, sticky='nw')

        # Advanced Toggle
        self.isAdvanced = False
        isAdvancedVar = BooleanVar()
        advCheck = Checkbutton(optFrame, text="Advanced", variable=isAdvancedVar, onvalue=True, offvalue=False,
                               command=lambda: self.update_isAdvanced(isAdvancedVar))
        advCheck.grid(row=1, column=0, sticky='nw')

        Button(optFrame,
               text="Run",
               command=lambda: self.runMatchInsight()
               ).grid(row=1, column=0, sticky="se")

    def runMatchInsight(self):
        if self.isAdvanced:
            print("Advanced is true")
        else:
            print("Advanced is false")

        if self.competition:
            print("Competition is true")
        else:
            print("Competition is false")
        print("Event ID:" + self.eventScrollable.eventID)

        print("Processing...")
        # TODO sal pls fix

        print("Done!")

    def updateCompetition(self, isComp):
        self.competition = isComp.get()

    def update_isAdvanced(self, isAdvancedVar):
        self.isAdvanced = isAdvancedVar.get()


class EventScrollable(Frame):
    def __init__(self, parent, controller):
        self.eventButtons = None
        self.eventID = None
        self.lastClicked = None
        global year
        Frame.__init__(self, parent)
        # Event List
        # TODO make this scrollable inside canvas
        # init canvas frame
        self.eventCanvasFrame = Frame(parent)
        self.eventCanvasFrame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.eventCanvasFrame.grid_rowconfigure(0, weight=1)
        self.eventCanvasFrame.grid_columnconfigure(0, weight=1)
        self.eventCanvasFrame.grid_columnconfigure(1, weight=0)

        # init canvas (for scroll bar)
        self.eventCanvas = Canvas(self.eventCanvasFrame)
        self.eventCanvas.grid(row=0, column=0, sticky="nsew")

        # init scroll bar
        scrollBar = Scrollbar(self.eventCanvasFrame, orient='vertical', command=self.eventCanvas.yview)
        scrollBar.grid(row=0, column=1, sticky='ns')
        self.eventCanvas.configure(yscrollcommand=scrollBar.set)

        # init selection frame
        self.eventFrame = Frame(self.eventCanvas)
        self.eventFrame.grid(row=0, column=0, sticky='nsew')
        self.eventCanvas.create_window((0, 0), window=self.eventFrame, anchor='nw')

        self.updateEvents()  # update event list on init

        # set canvas scroll region
        self.eventFrame.bind("<Configure>", lambda event, canvas=self.eventCanvas: self.onFrameConfigure(canvas))

    def setEventID(self, eventID, buttonIndex):
        self.eventID = eventID
        try:
            self.lastClicked.configure(bg="white")  # TODO make @self.buttonColor
        except AttributeError:
            pass
        self.lastClicked = self.eventButtons[buttonIndex]
        self.lastClicked.configure(bg="green")

    def updateEvents(self):
        global year
        # TODO update event
        # get events and names
        events = getEvents(year)
        eventNames = list(events.keys())  # TODO sort alphabetically

        # event button list container
        self.eventButtons = []

        # clear eventFrame
        for button in self.eventFrame.winfo_children():
            button.destroy()
        self.lastClicked = None

        for i in range(len(eventNames)):
            button = Button(
                self.eventFrame,
                text=eventNames[i],
                command=lambda index=i: self.setEventID(events[eventNames[index]], index)
            )
            button.grid(row=i, column=0, sticky='w')
            self.eventButtons.append(button)

    def onFrameConfigure(self, canvas):
        canvas.config(scrollregion=canvas.bbox("all"))


class TeamsScrollable(Frame):
    def __init__(self, parent, controller):
        self.teamButtons = None
        self.teamNumber = None
        self.lastClicked = None
        global year
        Frame.__init__(self, parent)
        # Event List
        # TODO make this scrollable inside canvas
        # init canvas frame
        self.teamCanvasFrame = Frame(parent)
        self.teamCanvasFrame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        self.teamCanvasFrame.grid_rowconfigure(0, weight=1)
        self.teamCanvasFrame.grid_columnconfigure(0, weight=1)
        self.teamCanvasFrame.grid_columnconfigure(1, weight=0)

        # init canvas (for scroll bar)
        self.teamCanvas = Canvas(self.teamCanvasFrame)
        self.teamCanvas.grid(row=0, column=1, sticky="nsew")

        # init scroll bar
        scrollBar = Scrollbar(self.teamCanvasFrame, orient='vertical', command=self.teamCanvas.yview)
        scrollBar.grid(row=0, column=1, sticky='ns')
        self.teamCanvas.configure(yscrollcommand=scrollBar.set)

        # init selection frame
        self.teamFrame = Frame(self.teamCanvas)
        self.teamFrame.grid(row=0, column=0, sticky='nsew')
        self.teamCanvas.create_window((0, 0), window=self.teamFrame, anchor='nw')

        self.updateTeams()  # update team list on init

        # set canvas scroll region
        self.teamFrame.bind("<Configure>", lambda team, canvas=self.teamCanvas: self.onFrameConfigure(canvas))

    def setTeamNumber(self, teamNumber, buttonIndex):
        self.teamNumber = teamNumber
        try:
            self.lastClicked.configure(bg="white")  # TODO make @self.buttonColor
        except AttributeError:
            pass
        self.lastClicked = self.teamButtons[buttonIndex]
        self.lastClicked.configure(bg="green")

    def updateTeams(self):
        global year
        # TODO update event
        # get teams and names
        teams = COMPETITION_TEAMS

        # reset buttons
        self.lastClicked = None

        # teams button list container
        self.teamButtons = []

        for i in range(len(teams)):
            button = Button(
                self.teamFrame,
                text=str(teams[i]),
                command=lambda index=i: self.setTeamNumber(teams[index], index)
            )
            button.grid(row=i, column=0, sticky='w')
            self.teamButtons.append(button)

    def onFrameConfigure(self, canvas):
        canvas.config(scrollregion=canvas.bbox("all"))


def getValidYears():
    validYears = []
    for i in range(1991, datetime.today().year + 1):
        validYears.append(i)
    validYears.sort(reverse=True)
    return validYears


# Data functions


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
'''

# Mainloop
StratUI().mainloop()
