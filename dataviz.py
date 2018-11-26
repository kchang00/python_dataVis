import csv
import numpy as np
import matplotlib.pyplot as plt

# cannot pull in title
# strip out title, set up an array, only pull in values you need

categories = []  # strip out first row of text
installs = []  # push installs data here
reviews = []  # push the reviews data here

# open csv and parse it

with open('data/googleplaystore.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:  # strip headers out
            print('pushing text row to categories array')
            categories.append(row)  # append = add
            line_count += 1
        else:
            # collect the reviews info, append into reviews array
            reviewsData = row[2]
            reviewsData = reviewsData.replace('NaN', '0')
            # float = number with a decimal, intergers = whole number
            reviews.append(float(reviewsData))

            # print('collect the rest of data')
            # count number of rows over (from 0), push data into array
            installData = row[5]
            installData = installData.replace(',', '')  # clean numbers
            installData = installData.replace('Free', '0')
            # installs.append(row[5]) # gives raw data
            # removes plus, get clean number you can work with
            installs.append(int(np.char.strip(installData, '+')))
            line_count += 1

print('processed', line_count, 'rows of data')
print('first line:', reviews[0])  # gets first row inside array
print('last line:', reviews[-1])

np_reviews = np.array(reviews)

# how many reviews are greater than 4
popular_apps = np_reviews > 4
pop_pct = int(len(np_reviews[popular_apps]) / len(np_reviews) * 100)
print(pop_pct)

unpopular_apps = np_reviews < 2
not_pop_pct = int(len(np_reviews[unpopular_apps]) / len(np_reviews) * 100)
print(not_pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)

# now we can plot stuff!

labels = 'Sucks', 'Meh', 'Love it!'
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')

plt.legend(labels, loc = 1)
plt.title('Do We Loves Our Apps?')
plt.xlabel('User reviews - Google Play Store App Installs')
plt.show()
