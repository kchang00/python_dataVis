import csv
import numpy as np
import matplotlib.pyplot as plt

# cannot pull in title
# strip out title, set up an array, only pull in values you need

categories = []  # strip out first row of text
installs = []  # push installs data here
ratings = []  # push the ratings data here

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
            # print('collect the rest of data')
            # count number of rows over (from 0), push data into array
            installData = row[5]
            installData = installData.replace(',', '')  # makes number, not text
            installData = installData.replace('Free', '0')
            # installs.append(row[5]) # gives raw data
            # removes plus, get clean number you can work with
            installs.append(int(np.char.strip(installData, '+')))
            line_count += 1

print('processed', line_count, 'rows of data')
print('first line:', installs[0])  # gets first row inside array
print('last line:', installs[-1])
