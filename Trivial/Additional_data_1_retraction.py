fh = open("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt", 'r', encoding = 'utf-8')
test = {}
for line in fh:
    if line.startswith('Movie_name'):
        continue
    a = line.strip().split('\t')
    test[str(a[0])] = a[1:]
fh.close()

fh = open('C:/Local/RT/Addtional_data_1.txt', 'w')
fh.write('Movie_name' + '\t' + 'Crtics_reviewer_count' + '\t' + 'Audience_reviewer_count' + '\n')
for x in test:
    fh.write(str(x) + '\t' + str(test[x][16].replace(',','')) + '\t' + str(test[x][17][1:-1].replace(',','')) + '\n')
fh.close()