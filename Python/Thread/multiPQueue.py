from multiprocessing import Process, Queue
import os, time, random

# write data from Queue
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C'] :
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# read data from Queue
def read(q):
    print('Process to read: %s' % os.getpid())
    while True :
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__' :
    # parent process create Queue and send it to child process
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr is while(True) which can't stop only if manual
    pr.terminate()