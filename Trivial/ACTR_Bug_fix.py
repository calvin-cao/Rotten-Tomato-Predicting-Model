fh = open("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt", 'r', encoding = 'utf-8')
test = {}
for line in fh:
    if line.startswith('Movie_name'):
        continue
    a = line.strip().split('\t')
    test[str(a[0])] = a[1:]
fh.close()

a = []
for x in test:
    if test[x][13][1:-2] == 'o':
        a.append(test[x][13][1:-2])
        print(str(x), test[x][13][1:-2])
    else:
        continue
print(len(a))