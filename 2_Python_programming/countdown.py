#!/usr/bin/python3
import sys, time

for i in range(10):
    sys.stdout.write('{0}/10\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)
