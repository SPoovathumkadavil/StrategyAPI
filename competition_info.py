import tbapy as t
import event_info
import csv

competition_teams = [
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
competition_teams.sort()

def get_competition_info(year):
    tba = t.TBA('import tbapy')
    tba = t.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

    tmp_events = []
    for i in competition_teams:
        tmp_events.append(tba.team_events(i, year))

    events = []
    for i in tmp_events:
        for j in i:
            keeper = []
            if j['key'] not in events:
                keeper.append(j['key'])
                keeper.append(j['name'])
            events.append(keeper)

    # For each competition event, iterate once
    with open('competition_info_output.csv', 'w', newline="") as output:
        writer = csv.writer(output)

        vals = [
            ['competition', 'dq', 'extra_stats', 'matches_played', 'qualifying_average', 'rank', 'record', 'sort_orders', 'team_key']
        ]

        # For each competition event iterate once
        for i in events:
            er = event_info.get_event_info(i)
            if not er:
                continue

            # For each team, iterate once
            times = 0
            for j in er:
                if times == 0:
                    times += 1
                    continue
                CurrentKey = j[8]

                num = ""
                for e in CurrentKey:
                    if e == 'f':
                        continue
                    elif e == 'r':
                        continue
                    elif e == 'c':
                        continue
                    else:
                        num += e
                num = int(num)

                for team in competition_teams:
                    if num < team:
                        break
                    TeamKey = "frc" + str(team)
                    if CurrentKey == TeamKey:
                        vals.append(j)
        writer.writerows(vals)

    output.close()
    return vals
