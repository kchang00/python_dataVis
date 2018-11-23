import csv
import numpy as np
import matplotlib.pyplot as plt

# cannot pull in title
# strip out title, set up an array, only pull in values you need

medal = []  # men vs women medals
gold = 1
silver = 2
bronze = 3

# open csv and parse it

with open('data/olympics_canada_men_women.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:  # strip headers out
            print('pushing text row to medal array')
            medal.append(row)  # append = add
            line_count += 1
        else:
            # collect the medal info, append into medal array
            medalData = row[4]

            # print('collect the rest of data')
            # count number of rows over (from 0), push data into array
            # installs.append(row[5]) # gives raw data
            # removes plus, get clean number you can work with
            line_count += 1

print('processed', line_count, 'rows of data')
print('first line:', medal[0])  # gets first row inside array
print('last line:', medal[-1])

np_medal = np.array(medal)

# how many ratings are greater than 4
popular_apps = np_medal == 1
pop_pct = int(len(np_medal[popular_apps]) / len(np_ratings) * 100)
print(pop_pct)

unpopular_apps = np_medal < 2
not_pop_pct = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(not_pop_pct)

total_medals = (gold + silver + bronze)

# now we can plot stuff!

labels = 'Sucks, Meh, Love it!'
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title('Do We Loves Our Apps?')
plt.xlabel('User Ratings - Google Play Store App Installs')
plt.show()
