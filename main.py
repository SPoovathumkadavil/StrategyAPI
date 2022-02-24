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

from TBAFunctions import *
from tkinter import *

class StratUI(Tk):

    # init app
    def __init__(self, *args, **kwargs):
        #init Tk
        Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")
        self.title("StrategyAPI")

        #create container
        container = Frame(self, bg = 'blue')
        container.pack(
            side = "top",
            fill = "both",
            expand = True
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

        #page 1 button
        Button(
            tabs,
            text = "Page1",
            command = lambda : self.showFrame(Page1)
        ).grid(row = 0, column = 0, sticky = "nws", padx = 10, pady = 10)
        # page 2 button
        Button(
            tabs,
            text = "Page2",
            command = lambda : self.showFrame(Page2)
        ).grid(row = 0, column = 1, sticky = "ns", padx = 10, pady = 10)
        # page 3 button
        Button(
            tabs,
            text = "Page3",
            command = lambda : self.showFrame(Page3)
        ).grid(row = 0, column = 2, sticky = "nes", padx = 10, pady = 10)


        # Tabs
        self.frames = {}

        #initalize all tabs
        for F in (StartPage, Page1, Page2, Page3): #order pages with init page first
            page = F(container, self)

            self.frames[F] = page

            page.grid(row = 1, column = 0, sticky ="nsew")

            
        
        self.showFrame(StartPage)#start page
    
    #display current frame
    def showFrame(self, cont):
        page = self.frames[cont]
        page.tkraise()

class StartPage(Frame):
    # Stuff on this page:
    #  - Welcome message and explenation
    #  - Settings and credit buttons
    #  - Quit button

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        f = Frame(self)
        f.grid(row = 0, column = 0, sticky = 'nsew')
        f.pack(side = "top",fill = "both",expand = True)
        f.grid_columnconfigure(0, weight = 1)
        f.grid_rowconfigure(0, weight = 1)

        # create label
        Label(
            f,
            text = "Hello! Welcome to StrategyAPI!\nTo Begin, Select an option"
        ).grid(row = 0, column = 0, sticky = 'n')

# Overall Event Information
class Page1(Frame):
    # Stuff on this page:
    #  - event key input (maybe event name to event key?)
    #  - whatever that bool value is as a check box?
    #  - Sal pls halp

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

# Team specific information
class Page2(Frame):
    # Stuff on this page:
    #  - Sal pls halp pls :smile:

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        f = Frame(self)
        f.grid(row = 0, column = 0)

        # intro text for init tab
        page1Text = "annother one?!?!?!"

        # create label
        Label(
            self,
            text = page1Text
        ).grid(row = 0, column = 0, sticky = 'nsew')

# Team match information from a specific year
class Page3(Frame):
    # Stuff on this page:
    #  - ahhhhhhhh

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        f = Frame(self)
        f.grid(row = 0, column = 0)

        # intro text for init tab
        page1Text = "THERE'S MORE"

        # create label
        Label(
            self,
            text = page1Text
        ).grid(row = 0, column = 0, sticky = 'nsew')
        

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
StratUI().mainloop()