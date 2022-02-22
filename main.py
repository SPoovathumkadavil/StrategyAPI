import competition_info
import event_info
import tbapy as t

tba = t.TBA('import tbapy')
tba = t.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

actions = ['update event info(get team information for specific events)',
           'update information for teams we will compete in the 2022 season(regional teams)']

print("Hello, Welcome to the FRC Team 4500 strategy API application!")
print("To begin, enter an action chosen from the following list. You may select it using the number on the left of "
      "the option.")

print("\n")

for action in range(len(actions)):
    print(str(action+1)+" - "+actions[action])

print("\n")

while True:
    a = input("Action: ")

    if a == '1':
        print("Enter the year of the event below.")
        year = int(input("Event year: "))

        events = tba.events(year)

        print("\n")

        print("enter an event from the list below. You may select it using the number on the left of the option.")

        event_picks = []
        for i in range(len(events)):
            rn = []
            print(str(i+1)+" - "+events[i]['name'])
            rn.append(events[i]['key'])
            rn.append(events[i]['name'])

            event_picks.append(rn)

        print("\n")

        event = int(input("Event: "))

        out = event_info.get_event_info(event_picks[event-1])

        if not out:
            continue

        for i in out:
            print(i)

        print("\n")
        print("the event_info_output file has been updated with the information above. enter 0 or quit in 'Action: ' "
              "to quit.")

    elif a == '2':
        print("Please enter the year of the competition season.")
        year = input("Year: ")

        print("\n")
        print("please wait...")
        print("\n")

        out = competition_info.get_competition_info(year)

        if not out:
            continue

        for i in out:
            print(i)

        print("\n")

        print("the competition_info_output file has been updated with the information above. enter 0 or quit in "
              "'Action: ' to quit.")

    elif a == '0' or a == 'quit':
        break

    else:
        pass

print('\ngoodbye!')
