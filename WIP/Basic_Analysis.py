"""
Key = Movie's name
Value:
    0: Critics_Score
    1: Audienc_Score
    2: Critic_Consensus
    3: Rating
    4: Genre
    5: Directed_By
    6: Written_By
    7: Studio
    8: In_Theaters_date
    9: On_Disc_Streaming_date
    10: Box_Office
    11: Runtime
    12: Summary
    13: Cast
    14: Critics_Reviews
    15: Audience_Reviews
    16: Critics_Reviewer_Count
    17: Audience_Reviewer_Count
"""

PATH = "C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt"
fh = open(PATH, 'r', encoding = 'utf-8')
test = {}
for line in fh:
    if line.startswith('Movie_name'):
        continue
    a = line.strip().split('\t')
    test[str(a[0])] = a[1:]
fh.close()
# print(test['10'])

a = []
b = []
c = []
for x in test:
    try:
        b.append(int(test[x][0]))
    except:
        pass
    try:
        c.append(int(test[x][1]))
    except:
        pass
    try:
        a.append(int(test[x][0]) - int(test[x][1]))
    except:
        pass
sum(a)/len(a)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# ax.hist(a, bins = 80)
ax.hist(b, bins = 90, label = 'Critics')
ax.hist(c, bins = 120, label = 'Audience')
ax.set_title('Critics-Audience Score Difference Histogram')
ax.legend(loc = 'best')
plt.show()

import numpy as np
# help(np)
