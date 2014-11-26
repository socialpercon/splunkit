#!usr/bin/python
# coding: utf-8
import re
import sys
import os
import time
from time import strftime

import json
import uuid
import datetime

def generator_file(filename, target):
    frontback = re.compile(r"(.*? UTC)(.*)")
    path = os.getcwd()
    dict = {}
    try:
        f = open(filename, 'r')
        parsing = open(target, 'w')
    except (IOError, OSError), e:
        print "error: %s" %e
    try:    
        parsing.write("{ \"data\" : [")
        while True:
            chunk = f.readline()
            if chunk:
                match = frontback.match(chunk).group(1,2)
                front = match[0]
                back = match[1]
                dict['id'] = front + str(uuid.uuid4())
                    #match = reg.match(row).group(1,2)
                    #print "frontdate : %s, match[0] : %s" % (frontdate, match[0])
                dict['atimestamp'] = front
                dict['event'] = front + back
                parsing.write(json.dumps(dict)+",\n")
            else:
                break

        parsing.seek(-2, 1)
        parsing.write(json.dumps(dict)+"]}")

    finally:
        f.close()
        parsing.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        generator_file(sys.argv[1], sys.argv[2])
    else:
        print "failed : wrong argument"
