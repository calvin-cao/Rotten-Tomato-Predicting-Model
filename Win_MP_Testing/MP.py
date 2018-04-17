from multiprocessing import Pool
import time
import TF as tf

if __name__ == '__main__':
    start_time = time.clock()
    p = Pool(20)
    d = p.map(tf.f, range(10000))
    print(d)
    """
    with Pool(processes = 20) as p:
        print(p.map(tf.f, range(100000)))
    """
    print("--- %s seconds ---" % (time.clock() - start_time))