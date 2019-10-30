from multiprocessing import Process
from datetime import datetime
import time
import os
today = datetime.now()
def t(s):
    while True:
        time.sleep(s)
        print(today)
def main():
    p = Process(target=t, args=(1,))
    p.start()
    for i in range (10):
        time.sleep(0.5)
        print 'Process id:', os.getpid()
    p.terminate()

    print("fii")


main()
