from time import gmtime, strftime
# C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt
fh = open("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_2018-04-22_02-55-10.txt", 'r', encoding = 'utf-8')
D = []
for l in fh:
    D.append(l)
fh.close()

AIA = []
AIA.append('Movie_name' + '\t' + 'Critics_Score' + '\t' + 'Audience_Score' + '\t' + 'Critic_Consensus' + '\t' + 'Rating' + '\t' + 'Genre' + '\t' + 'Directed_By' + '\t' + 'Written_By' + '\t' + 'Studio' + '\t' + 'In_Theaters_date' + '\t' + 'On_Disc_Streaming_date' + '\t' + 'Box_Office' + '\t' + 'Runtime' + '\t' + 'Summary' + '\t' + 'Cast' + '\t' + 'Critics_Reviews' + '\t' + 'Audience_Reviews' + '\t' + 'Critics_Reviewer_Count' + '\t' + 'Audience_Reviewer_Count' + '\n')
for x in D[1:]:
    a = ''
    i = 0
    for s in x.split('\t'):
        i += 1
        if i == 13:
            a += str(s.strip()[0:-8]) + '\t'
        elif i == 19:
            a += str(s.strip()) + '\n'
        else:
            a += str(s.strip()) + '\t'
    AIA.append(a)

fh = open("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/test_" + strftime("%Y-%m-%d_%H-%M-%S") + '.txt', 'w', encoding = 'utf-8')
for x in AIA:
	fh.write(x)
fh.close()





## REstart!
