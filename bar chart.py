import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
men_scores = (22, 30, 33, 30, 26)


# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
Transparency = 1

rects1 = plt.bar(index, men_scores, bar_width,
alpha=Transparency,
color='r',
label='Men')


plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index , ('Kohli', 'Parthiv Patel', 'ABd', 'Moeen Ali', 'Pawan Negi'))
plt.legend()

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Kohli', 'ABd', 'Parthiv Patel', 'Moeen Ali' , 'Pawan Negi'
sizes = [22, 30, 33, 30, 26]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
