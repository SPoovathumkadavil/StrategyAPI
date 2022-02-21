import tbapy as t
import event_info

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

tba = t.TBA('import tbapy')
tba = t.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

team_info = []

for i in competition_teams:
    info = tba.team(i)
    team_info.append(info)

competition_cities = set()
for i in team_info:
    competition_cities.add(i['city'])

competition_cities = list(competition_cities)

print(competition_cities)

print("\n")

events = tba.events(2022)
for i in events:
    print(i)

print("\n")

competition_events = []
for i in events:
    if i['city'] in competition_cities:
        competition_events.append(i['key'])

for i in competition_events:
    print(i)
