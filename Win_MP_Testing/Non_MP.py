import time
start_time = time.clock()
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(100000):
    print(x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x)
print("--- %s seconds ---" % (time.clock() - start_time))