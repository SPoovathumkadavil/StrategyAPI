import tbapy
import csv

tba = tbapy.TBA('import tbapy')

tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')


def get_event_info(kl):
    try:
        x = tba.event_rankings(kl[0])['rankings']
    except KeyError:
        return False
    keys = x[len(x)-1].keys()

    with open('event_info_output.csv', 'w', newline="") as output:
        writer = csv.writer(output)

        vals = [['competition', 'dq', 'extra_stats', 'matches_played', 'qual_average', 'rank', 'record', 'sort_orders', 'team_key']]

        if x is not None:
            for i in x:
                t = [kl[1]]
                for j in keys:
                    t.append(i[j])

                vals.append(t)
            writer.writerows(vals)
        else:
            return False

    output.close()
    return vals
