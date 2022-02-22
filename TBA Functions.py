import tbapy
import csv

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


# specific event ranking info
def get_event_ranking(event_key='2019mosl', f=False):
    # get name of the event
    event = tba.event(event_key)['name']

    # get event rankings using the event key eg. '2019mosl'
    # returns list of dictionaries with teams sorted by ranking
    rankings = tba.event_rankings(event_key)['rankings']

    # Collect keys from dictionary
    keys = rankings[0].keys()

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

    # Go through all event rankings and get info for competition teams
    for event in events:
        # Get rank data for each event
        rank_data = get_event_ranking(event, True)


