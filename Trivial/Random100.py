from os import listdir
from random import sample
a = sample(listdir('C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML'), 100)
for x in a:
    fh = open('C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x, 'r')
    c = fh.read()
    fh.close()
    fh1 = open('C:/Local/RT/Random100/' + x, 'w')
    fh1.write(c)
    fh1.close()
