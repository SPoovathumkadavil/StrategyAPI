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

    for team in competition_teams:
        events = tba.team_events(team, year)
        for event in events:
            tmp_events.append(event['key'])

    events = []
    for event in tmp_events:
        if event not in events:
            events.append(event)

    competition_event_results = []
    for event in events:
        event_ranking = tba.event_rankings(event)['rankings']

        if event_ranking is not None:
            for team in event_ranking:
                tmp_holder = [tba.event(event)['name']]

                if int(team['team_key'][3:]) in competition_teams:
                    tmp_holder.append(team)
                    competition_event_results.append(tmp_holder)

        with open('competition_info_output.csv', 'w', newline='') as output:
            writer = csv.writer(output)

            vals = [
                ['competition', 'dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders',
                 'team_key']]

            for i in competition_event_results:
                tmp_holder = [i[0]]
                keys = i[1].keys()
                for j in keys:
                    tmp_holder.append(i[1][j])
                vals.append(tmp_holder)

            writer.writerows(vals)
        return vals

