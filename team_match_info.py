import matches as matches
import tbapy as t
import csv


def team_match_info_gatherer(team=4500, event=False, year=2019):
    tba = t.TBA('import tbapy')
    tba = t.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

    if not event:
        matches = tba.team_matches(team=team, year=year)

        with open('team_match_info_output.csv', 'w', newline='') as output:
            writer = csv.writer(output)

            vals = []

            keys = matches[0].keys()

            vals.append(keys)

            for match in matches:
                tmp_holder = []

                for key in keys:
                    tmp_holder.append(match[key])
                vals.append(tmp_holder)

            writer.writerows(vals)

        return matches
    else:
        matches = tba.team_matches(team=team, event=event, year=year)

        with open('team_match_info_output.csv', 'w', newline='') as output:
            writer = csv.writer(output)

            vals = []
            keys = matches[0].keys()

            vals.append(keys)
            for match in matches:

                tmp_holder = []

                for key in keys:
                    tmp_holder.append(match[key])
                vals.append(tmp_holder)

            writer.writerows(vals)

        return matches


