import time
import math
def f(x):
    return print(x*x)
start_time = time.clock()
for x in range(10000):
    f(x)
print("--- %s seconds ---" % (time.clock() - start_time))