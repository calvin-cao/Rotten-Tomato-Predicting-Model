fh = open("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt", 'r', encoding = 'utf-8')
test = {}
for line in fh:
    if line.startswith('Movie_name'):
        continue
    a = line.strip().split('\t')
    test[str(a[0])] = a[1:]
fh.close()

for x in test:
    # for i in range(3):
    if ',Jr' in test[x][13]:
        test[x][13] = test[x][13].replace(',Jr','.Jr')
    else:
        continue

a = []
for x in test:
    if ',Jr' in test[x][13][1:-2]:
        a.append(test[x][13][1:-2])
    else:
        continue
print(len(a))

ACTR_TM = {}
for x in test:
    for s in test[x][13][1:-2].strip().split(','):
        ACTR_TM[s] = ACTR_TM.get(s, 0) + 1
print(ACTR_TM['TomHanks'])

ACTR_BO = dict()
for x in test:
    # BO = test[x][10][1:-1].strip().replace('$','').replace(',','')
    # CA = test[str(every_movie)][13][1:-2].strip().split(',')
    for s in test[x][13][1:-2].strip().split(','):
        if not s in ACTR_BO:
            ACTR_BO[s] = 0
            try:
                ACTR_BO[s] += int(test[x][10][1:-1].strip().replace('$','').replace(',',''))
            except:
                continue
        elif s in ACTR_BO:
            try:
                ACTR_BO[s] += int(test[x][10][1:-1].strip().replace('$','').replace(',',''))
            except:
                continue
        else:
            continue
print(ACTR_BO['TomHanks'])

ACTR_ACR_temp = {}
for x in test:
    for s in test[x][13][1:-2].strip().split(','):
        if not s in ACTR_ACR_temp:
            ACTR_ACR_temp[s] = []
            try:
                ACTR_ACR_temp[s].append(int(test[x][0].strip()))
            except:
                continue
        elif s in ACTR_ACR_temp:
            try:
                ACTR_ACR_temp[s].append(int(test[x][0].strip()))
            except:
                continue
        else:
            continue
print(ACTR_ACR_temp['TomHanks'])
ACTR_ACR = {}
for x in ACTR_ACR_temp:
    s = 0
    for n in ACTR_ACR_temp[x]:
        s += int(n)
    l = len(ACTR_ACR_temp[x])
    if l == 0:
        ACTR_ACR[x] = None
    else:
        ACTR_ACR[x] = s/l
print(ACTR_ACR['TomHanks'])

ACTR_AAR_temp = {}
for x in test:
    for s in test[x][13][1:-2].strip().split(','):
        if not s in ACTR_AAR_temp:
            ACTR_AAR_temp[s] = []
            try:
                ACTR_AAR_temp[s].append(int(test[x][1].strip()))
            except:
                continue
        elif s in ACTR_AAR_temp:
            try:
                ACTR_AAR_temp[s].append(int(test[x][1].strip()))
            except:
                continue
        else:
            continue
print(ACTR_AAR_temp['TomHanks'])
ACTR_AAR = {}
for x in ACTR_AAR_temp:
    s = 0
    for n in ACTR_AAR_temp[x]:
        s += int(n)
    l = len(ACTR_AAR_temp[x])
    if l == 0:
        ACTR_AAR[x] = None
    else:
        ACTR_AAR[x] = s/l
print(ACTR_AAR['TomHanks'])

fh = open('C:/Local/RT/Addtional_data_2.txt', 'w', encoding = 'utf-8')
fh.write('Actor' + '\t' + 'Total_movie' + '\t' + 'Total_Boxoffice' + '\t' + 'Average_Critics_Score' + '\t' + 'Average_Audience_Score' + '\n')
for x in ACTR_TM:
    fh.write(x + '\t' + str(ACTR_TM[x]) + '\t' + str(ACTR_BO[x]) + '\t' + str(ACTR_ACR[x]) + '\t' + str(ACTR_AAR[x]) + '\n')
fh.close()

# Igonore the 'o's cause they are Null values