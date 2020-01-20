import time
import os

time.sleep(10)
i=0
while True:
    fname="output/demofile{}.txt".format(i)
    print("creating file ", fname)
    f = open(fname, "a")
    f.write("Now the file has more content!")
    f.close()
    i+=1
    time.sleep(60*2)
