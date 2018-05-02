from multiprocessing import Pool, Process, cpu_count
import time
import TF as tf
import math

if __name__ == '__main__':
    start_time = time.clock()
    """
    for i in range(10000):
        p = Process(target = tf.f, args = (i,))
        p.start()
    """
    
    p = Pool(cpu_count())
    d = p.map(tf.f, range(100000))
    p.close()
    # print(d)
    
    """
    with Pool(processes = 20) as p:
        print(p.map(tf.f, range(100000)))
    """
    print("--- %s seconds ---" % (time.clock() - start_time))