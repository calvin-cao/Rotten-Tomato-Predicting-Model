from multiprocessing import Pool
import time
import TF as defs

if __name__ == '__main__':
    start_time = time.clock()
    with Pool(2) as p:
        print(p.map(defs.f, range(100000)))
    print("--- %s seconds ---" % (time.clock() - start_time))