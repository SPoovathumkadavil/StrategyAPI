import tbapy
import csv

tba = tbapy.TBA('import tbapy')

tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

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