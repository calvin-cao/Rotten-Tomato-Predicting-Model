import os

PATH = input("Please enter html files' path: ")
if len(PATH) < 1:
	PATH = "/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/"
a = [PATH + x for x in os.listdir(PATH) if x.endswith('.html')]
b = {}
i = 0
for x in range(0,len(a),200):
	i += 1
	b[str(i)] = []
	for s in a[x : x + 200]:
		b[str(i)].append(s)
print(b.keys())