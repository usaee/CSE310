

import pandas as pd
import statistics as stats


# Part 1

fname = "Daily_Activity_2022_27_02.csv"
data_set = pd.read_csv(fname)

full_days = {'Sun':'Sunday',
             'Mon':'Monday',
             'Tue':'Tuesday',
             'Wed':'Wednesday',
             'Thu':'Thursday',
             'Fri':'Friday',
             'Sat':'Saturday'}

days_distance = data_set[['ActivityDay', 'TotalDistance']]

most = 0
best_days = []
best_day = str()
for index, row in days_distance.iterrows():
    day = row['ActivityDay']
    dist = row['TotalDistance']

    if dist > most:
        most = dist
        best_day = day

    if day == 'Sun':
        best_days.append(best_day)
        best_day = str()
        most = 0

result = stats.mode(best_days)
print("This person tends to do the most walking on ({})".format(full_days[result]))

# Part 2

days_distance = data_set[['ActivityDay', 'VeryActiveDistance']]

most = 0
best_days = []
best_day = str()
for index, row in days_distance.iterrows():
    day = row['ActivityDay']
    dist = row['VeryActiveDistance']

    if dist > most:
        most = dist
        best_day = day

    if day == 'Sun':
        best_days.append(best_day)
        best_day = str()
        most = 0

result = stats.mode(best_days)
print("This person tends to be the most active on ({})".format(full_days[result]))
