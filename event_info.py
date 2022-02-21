import tbapy
import csv

tba = tbapy.TBA('import tbapy')

tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

peoria_teams = [
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
8122]

#pt_info = []
#for i in peoria_teams:
#    pt_info.append(tba.team(i))

#print(pt_info)

#print(tba.events(2021))
def get_event_info(event_key):
    x = tba.event_rankings(event_key)

    fieldnames = ['dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders', 'team_key']

    with open('output.csv', 'w', newline="") as output:
        writer = csv.writer(output)
        vals = [['dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders', 'team_key']]
        for i in x["rankings"]:
            t = []
            for n in i:
                val = i[n]
                t.append(val)
            vals.append(t)
        writer.writerows(vals)

    output.close()