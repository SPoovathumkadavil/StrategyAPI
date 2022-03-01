from tkinter import *
from TBAFunctions import *

# Ranking Information
class Ranking(Frame):

    def __init__(self, parent, controller):
        self.year = None
        self.eventID = None

        # init self as frame
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
              text="Ranking Information Tab"
              ).grid(row=0, columnspan=2, sticky='n')

        # Event List TODO make this its own separate object
        # init canvas frame
        eventCanvasFrame = Frame(f)
        eventCanvasFrame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        eventCanvasFrame.grid_rowconfigure(0, weight=1)
        eventCanvasFrame.grid_columnconfigure(0, weight=1)

        # init canvas (for scroll bar)
        eventCanvas = Canvas(eventCanvasFrame)
        eventCanvas.grid(row=0, column=0, sticky="nsew")

        # init scroll bar
        scrollBar = Scrollbar(eventCanvasFrame, orient='vertical', command=eventCanvas.yview)
        scrollBar.grid(row=0, column=1, sticky='ns')
        eventCanvas.configure(yscrollcommand=scrollBar.set)

        # init selection frame
        eventFrame = Frame(eventCanvas)
        eventFrame.grid(row=0, column=0, sticky='nsew')
        eventCanvas.create_window((0, 0), window=eventFrame, anchor='nw')

        # get events and names
        events = getEvents(self.year)
        eventNames = list(events.keys())  # TODO sort alpha

        # event button list container
        eventButtons = []
        # TODO update year on year change/page open
        for i in range(len(eventNames)):
            button = Button(
                eventFrame,
                text=eventNames[i],
                command=lambda: self.setEventID(events[eventNames[i]])
            )
            button.grid(row=i, column=0, sticky='w')
            eventButtons.append(button)

        # set canvas scroll region
        eventFrame.bind("<Configure>", lambda event, canvas=eventCanvas: self.onFrameConfigure(canvas))

        # Competition Toggle
        self.competition = False
        isComp = BooleanVar()
        compCheck = Checkbutton(f, text="Competition", variable=isComp, onvalue=True, offvalue=False,
                                command=lambda: self.updateCompetition(isComp))
        compCheck.grid(row=1, column=1, sticky='nw')

        # Simple toggle

        # run button
        Button(f,
               text="Run",
               command=lambda: self.runRankingInfo()
               ).grid(row=1, column=1, sticky="se", padx=10, pady=10)

    # TODO: - make setEventID change color of button so user can see selected
    def setEventID(self, id):
        self.eventID = id

    def updateCompetition(self, isComp):
        self.competition = isComp.get()

    def onFrameConfigure(self, canvas):
        canvas.config(scrollregion=canvas.bbox("all"))

    def runRankingInfo(self):
        print("Competition: " + str(self.competition))
        print("Event ID:" + self.eventID)

    def updateYear(self, year):
        self.year = year
