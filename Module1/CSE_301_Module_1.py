

import pandas as pd
import statistics as stats


#########################################################################################
# Finding Day Which Day Users Tend To Walk The Farthest.
#########################################################################################
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

    # If the distance walked on the current day is
    # greater than the last greatest distance recorded,
    # then the value of the last 'best_day' variable is
    # replaced with the distance for the current day.
    if dist > most:
        most = dist
        best_day = day

    # I am using Sunday to mark the end of each week.
    # Therefore, each time we reach the day Sunday,
    # The day with the greatest distance walked will be
    # Added to the best_days list and the variables 'best_day'
    # and 'most' will be reset so that the next week can be analyzed.
    if day == 'Sun':
        best_days.append(best_day)
        best_day = str()
        most = 0

result = stats.mode(best_days) # Computes the mode of the list of days.

print("Users tend to walk the farthest on ({})".format(full_days[result]))


#########################################################################################
# Finding Day Which Day Users Tend To Perform The Most Vigorus Exercise.
#########################################################################################
days_distance = data_set[['ActivityDay', 'VeryActiveDistance']]

most = 0
best_days = []
best_day = str()
for index, row in days_distance.iterrows():
    day = row['ActivityDay']
    active_dist = row['VeryActiveDistance']

    # If the amount of activity performed on the current day is
    # greater than the last greatest amount of activity recorded,
    # then the value of the last 'best_day' variable is
    # replaced with the amount of activity for the current day.
    if active_dist > most:
        most = active_dist
        best_day = day

    # I am using Sunday to mark the end of each week.
    # Therefore, each time we reach the day Sunday,
    # The day with the greatest amount of activity will be
    # Added to the best_days list and the variables 'best_day'
    # and 'most' will be reset so that the next week can be analyzed.
    if day == 'Sun':
        best_days.append(best_day)
        best_day = str()
        most = 0

result = stats.mode(best_days)
print("Users tend to perform the most vigorus exercise on ({})".format(full_days[result]))

