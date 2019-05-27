#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)....' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for all subprcesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
