#!usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Saaleh Poovathumkadavil"
__credits__ = "Saaleh Poovathumkadavil"
__license__ = "FRC4500"
__maintainer__ = "Saaleh Poovathumkadavil"
__status__ = "Development"
__version__ = "0.0.1"


import csv
import tbapy

COMPETITION_TEAMS = [
    111,
    648,
    706,
    1625,
    1716,
    1736,
    1756,
    1781,
    2039,
    2040,
    2338,
    2358,
    2451,
    2481,
    2704,
    2783,
    3061,
    3067,
    3381,
    3695,
    4096,
    4143,
    4213,
    4241,
    4500,
    4531,
    4645,
    4655,
    5442,
    5822,
    6651,
    7103,
    7417,
    7619,
    7848,
    8029,
    8096,
    8122,
    931,
    1178,
    1288,
    1329,
    1444,
    1658,
    1706,
    1736,
    1756,
    1781,
    1985,
    2408,
    2481,
    2707,
    2978,
    3397,
    3792,
    4143,
    4187,
    4232,
    4256,
    4329,
    4330,
    4500,
    4600,
    4931,
    5060,
    5176,
    5583,
    6157,
    6237,
    6391,
    6744,
    7117,
    7472,
    7496,
    7747,
    8069,
    8077,
    8719
]

# initialize The Blue Alliance object
tba = tbapy.TBA('import tbapy')
tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')


'''
    Original Functions
'''


# Get specific event ranking info
def get_event_ranking(event_key='2022week0', f=False):
    # get name of the event
    event = tba.event(event_key)['name']

    # get event rankings using the event key eg. '2022week0'
    # returns list of dictionaries with teams sorted by ranking
    # Collect keys from dictionary
    try:
        rankings = tba.event_rankings(event_key)['rankings']
        keys = rankings[0].keys()
    except:
        return

    vals = [
        ['competition', 'dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders',
         'team_key']
    ]
    # Iterate over teams in rankings
    for team in rankings:
        # temporarily hold values from dictionaries
        tmp_holder = [event]

        # Iterate over keys in teams dictionary.
        for key in keys:
            # Add values to tmp_holder
            tmp_holder.append(team[key])

        # append list to vals
        vals.append(tmp_holder)

    # If part of another function
    if f:
        return vals

    # If standalone
    else:
        # Open an output csv file and put value data in it
        with open('output/event_info_data.csv', 'w', newline='') as output:
            # Create a writer cursor
            writer = csv.writer(output)

            writer.writerows(vals)

        return vals


# Get competition ranking data
def get_competition_ranking(year=2019):
    # Get all the competition events
    events = []

    # Iterate though all of the teams
    for team in COMPETITION_TEAMS:
        # Get all events for team
        tmp_holder = tba.team_events(team=team, year=year)

        # Check for duplicates
        for t in tmp_holder:
            # If event_key not in events, then append
            if t['key'] not in events:
                events.append(t['key'])

    vals = [
        ['competition', 'dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders',
         'team_key']
    ]

    # Go through all event rankings and get info for competition teams
    for event in events:
        # Get rank data for each event
        rank_data = get_event_ranking(event, True)

        if rank_data is None:
            continue

        # Iterate over rank data to find comp. teams
        for team in rank_data:
            tmp_holder = [tba.event(event)['name']]

            # Team key = team num
            team_key = team[8][3:]
            if team_key == 'm_key':
                continue

            # convert key to num
            team_key = int(team_key)

            # If the team_key is one of our competition teams, then append it to
            if team_key not in COMPETITION_TEAMS:
                continue
            else:
                things = team[1:]
                for thing in things:
                    tmp_holder.append(thing)

            # Append the holder to the values
            vals.append(tmp_holder)

        # Write to csv file
    with open('output/competition_info_output.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(vals)

    # Return lines
    return vals


# Get team matches in a season or in a specific event
# Set simple to false in order to get more data
def get_team_matches(team=4500, event_key=False, year=2019, simple=True):
    if simple:
        # if there is no event input
        if not event_key:
            matches = tba.team_matches(team=team, year=year, simple=simple)

            # Define headers
            vals = [
                ['competition', 'actual time', 'blue alliance dq team keys', 'blue alliance score',
                 'blue alliance surrogate team keys', 'blue alliance team keys', 'red alliance dq team keys',
                 'red alliance score', 'red alliance surrogate team keys', 'red alliance team keys',
                 'competition level', 'event key', 'match key', 'match number', 'predicted time', 'set number', 'time',
                 'winning alliance']
            ]

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/team_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

        # if there is event input
        else:
            matches = tba.team_matches(team=team, event=event_key, year=year, simple=simple)

            # Define headers
            vals = [
                ['competition', 'actual time', 'blue alliance dq team keys', 'blue alliance score',
                 'blue alliance surrogate team keys', 'blue alliance team keys', 'red alliance dq team keys',
                 'red alliance score', 'red alliance surrogate team keys', 'red alliance team keys',
                 'competition level', 'event key', 'match key', 'match number', 'predicted time', 'set number', 'time',
                 'winning alliance']
            ]

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

    # If advanced information needed
    else:
        # if there is no event input
        if not event_key:
            matches = tba.team_matches(team=team, year=year, simple=simple)

            try:
                baseMatch = matches[0]
            except:
                return

            # Define headers
            vals = []

            # get all the match keys
            keys = matches[0].keys()

            # Header holder
            headers = ['competition']

            # For every key
            for key in keys:
                # Header name
                key_string = ""

                # If current value is a dictionary
                if type(baseMatch[key]) == dict:
                    # Add
                    key_string += key + '.'
                    newKeys = baseMatch[key].keys()

                    for newKey in newKeys:
                        if type(baseMatch[key][newKey]) == dict:
                            key_string += newKey + '.'

                            moreKeys = baseMatch[key][newKey].keys()

                            for mKey in moreKeys:
                                headers.append(key_string + mKey)

                        else:
                            headers.append(key_string + newKey)

                else:
                    headers.append(key)

            vals.append(headers)

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/team_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

        # if there is event input
        else:
            matches = tba.team_matches(team=team, event=event_key, year=year, simple=simple)

            try:
                baseMatch = matches[0]
            except:
                return

            # Define headers
            vals = []

            keys = matches[0].keys()

            headers = ['competition']

            for key in keys:
                key_string = ""
                if type(baseMatch[key]) == dict:
                    key_string += key + '.'
                    newKeys = baseMatch[key].keys()

                    for newKey in newKeys:
                        if type(baseMatch[key][newKey]) == dict:
                            key_string += newKey + '.'

                            moreKeys = baseMatch[key][newKey].keys()

                            for mKey in moreKeys:
                                headers.append(key_string + mKey)

                        else:
                            headers.append(key_string + newKey)

                else:
                    headers.append(key)

            vals.append(headers)

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/team_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

    # Return lines
    return vals


# Get event matches in a specific event
# Set simple to false in order to get more data
def get_event_matches(event_key='2022week0', simple=True):
    matches = tba.event_matches(event=event_key, simple=simple)

    try:
        baseMatch = matches[0]
    except:
        return

    # Define headers
    vals = []

    keys = matches[0].keys()

    headers = ['competition']

    for key in keys:
        key_string = ""
        if type(baseMatch[key]) == dict:
            key_string += key + '.'
            newKeys = baseMatch[key].keys()

            for newKey in newKeys:
                if type(baseMatch[key][newKey]) == dict:
                    key_string += newKey + '.'

                    moreKeys = baseMatch[key][newKey].keys()

                    for mKey in moreKeys:
                        headers.append(key_string + mKey)

                else:
                    headers.append(key_string + newKey)

        else:
            headers.append(key)

    vals.append(headers)

    # iterate over matches
    for match in matches:
        # values of dictionaries
        values = match.values()

        # A temporary holder to make vals an array
        tmp_holder = [tba.event(match['event_key'])['name']]

        # iterate over the match values
        for val in values:
            # If the value is a dictionary
            if type(val) == dict:
                # Get values from dictionary
                dictionary_values = val.values()

                # iterate over values
                for dictionary_value in dictionary_values:
                    # For dictionary array
                    item_value = dictionary_value.values()

                    # Append each item to tmp_holder
                    for item in item_value:
                        tmp_holder.append(item)
            else:
                # If the value is not a dictionary, just append it to tmp_holder
                tmp_holder.append(val)

        # Append tmp_holder to vals
        vals.append(tmp_holder)

    with open('output/event_matches_info_output.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(vals)

    # Return lines
    return vals


# Get competition match information
# Set simple to false in order to get more data
def get_competition_matches(year=2022, event_key=False, simple=True):
    if simple:
        if event_key:
            # Matches for all teams
            matches = []
            for team in COMPETITION_TEAMS:
                team_matches = tba.team_matches(team=team, event=event_key, simple=simple)

                try:
                    for match in team_matches:

                        if match not in matches:
                            matches.append(match)
                except:
                    return

            vals = [
                ['competition', 'actual time', 'blue alliance dq team keys', 'blue alliance score',
                 'blue alliance surrogate team keys', 'blue alliance team keys', 'red alliance dq team keys',
                 'red alliance score', 'red alliance surrogate team keys', 'red alliance team keys',
                 'competition level', 'event key', 'match key', 'match number', 'predicted time', 'set number', 'time',
                 'winning alliance']
            ]

            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/competition_teams_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

        else:
            # Matches for all teams
            matches = []
            for team in COMPETITION_TEAMS:
                team_matches = tba.team_matches(team=team, simple=simple)

                try:
                    for match in team_matches:

                        if match not in matches:
                            matches.append(match)
                except:
                    return

            vals = [
                ['competition', 'actual time', 'blue alliance dq team keys', 'blue alliance score',
                 'blue alliance surrogate team keys', 'blue alliance team keys', 'red alliance dq team keys',
                 'red alliance score', 'red alliance surrogate team keys', 'red alliance team keys',
                 'competition level', 'event key', 'match key', 'match number', 'predicted time', 'set number',
                 'time',
                 'winning alliance']
            ]

            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                # Event name
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/competition_teams_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

    else:
        if event_key:
            matches = []

            for team in COMPETITION_TEAMS:
                team_matches = tba.team_matches(team=team, event=event_key, year=year, simple=simple)

                try:
                    for match in team_matches:

                        if match not in matches:
                            matches.append(match)
                except:
                    return

            try:
                baseMatch = matches[0]
            except:
                return

            # Define headers
            vals = []

            try:
                keys = matches[0].keys()
            except:
                return

            headers = ['competition']

            for key in keys:
                key_string = ""
                if type(baseMatch[key]) == dict:
                    key_string += key + '.'
                    newKeys = baseMatch[key].keys()

                    for newKey in newKeys:
                        if type(baseMatch[key][newKey]) == dict:
                            key_string += newKey + '.'

                            moreKeys = baseMatch[key][newKey].keys()

                            for mKey in moreKeys:
                                headers.append(key_string + mKey)

                        else:
                            headers.append(key_string + newKey)

                else:
                    headers.append(key)

            vals.append(headers)

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/competition_teams_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

        else:
            matches = []

            for team in COMPETITION_TEAMS:
                team_matches = tba.team_matches(team=team, year=year, simple=simple)

                for match in team_matches:
                    event_name = tba.event(match['event_key'])['name']

                    if match not in matches:
                        matches.append(match)

            try:
                baseMatch = matches[0]
            except:
                return

            # Define headers
            vals = []

            try:
                keys = matches[0].keys()
            except:
                return

            headers = ['competition']

            for key in keys:
                key_string = ""
                if type(baseMatch[key]) == dict:
                    key_string += key + '.'
                    newKeys = baseMatch[key].keys()

                    for newKey in newKeys:
                        if type(baseMatch[key][newKey]) == dict:
                            key_string += newKey + '.'

                            moreKeys = baseMatch[key][newKey].keys()

                            for mKey in moreKeys:
                                headers.append(key_string + mKey)

                        else:
                            headers.append(key_string + newKey)

                else:
                    headers.append(key)

            vals.append(headers)

            # iterate over matches
            for match in matches:
                # values of dictionaries
                values = match.values()

                # A temporary holder to make vals an array
                tmp_holder = [tba.event(match['event_key'])['name']]

                # iterate over the match values
                for val in values:
                    # If the value is a dictionary
                    if type(val) == dict:
                        # Get values from dictionary
                        dictionary_values = val.values()

                        # iterate over values
                        for dictionary_value in dictionary_values:
                            # For dictionary array
                            item_value = dictionary_value.values()

                            # Append each item to tmp_holder
                            for item in item_value:
                                tmp_holder.append(item)
                    else:
                        # If the value is not a dictionary, just append it to tmp_holder
                        tmp_holder.append(val)

                # Append tmp_holder to vals
                vals.append(tmp_holder)

            with open('output/competition_teams_matches_info_output.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerows(vals)

    # Return lines
    return vals


# Get event insights
# eg. average score, climb, taxi, etc.
def get_event_insights(event_key='2022week0', t='playoff'):
    ins = tba.event_insights(event_key)[t]

    keys = []
    insights = []

    for s in ins:
        keys.append(s)

    insights.append(keys)

    tmp_holder = []

    for key in keys:
        tmp_holder.append(ins[key])

    insights.append(tmp_holder)

    with open('output/event_insight_info_output.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(insights)

    return insights


'''
    Helper functions/actual function to be used in main.py
'''


# Get all types of rankings
def get_ranking(competition=False, year=False, event_key=False):
    if not event_key:
        if not year:
            return
        if not competition:
            return
        try:
            return get_competition_ranking(year)
        except:
            return 1
    else:
        try:
            return get_event_ranking(event_key)
        except:
            return 1


# Get all matches for
def get_matches(team=False, competition=False, year=False, event_key=False, simple=False):
    if not event_key:
        if not year:
            return
        if competition:
            try:
                return get_competition_matches(year)
            except:
                return 1
        else:
            try:
                return get_team_matches(team=team, year=year, simple=simple)
            except:
                return 1
        return
    else:
        if not year:
            return
        if competition:
            try:
                return get_competition_matches(year=year, event_key=event_key, simple=simple)
            except:
                return 1
        if team != False:
            try:
                return get_team_matches(team=team, year=year, simple=simple, event_key=event_key)
            except:
                return 1
        return


# Get all event insight
def get_insight(event_key=False, type=False):
    if not event_key:
        return
    if not type:
        try:
            return get_event_insights(event_key=event_key)
        except:
            return 1
    else:
        try:
            return get_event_insights(event_key=event_key, t=type)
        except:
            return 1
    return

