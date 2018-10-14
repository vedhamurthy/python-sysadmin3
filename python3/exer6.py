#!/usr/bin/env python3.6

import subprocess
import os
from argparse import ArgumentParser
from sys import exit
parser = ArgumentParser(description='kill the running process listing on a given port')

parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port


try:
    result = subprocess.run(
            ['lsof', '-n', "-i4TCP:%s" % port],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    """
    print(result)
    print(result.stdout)
    print(result.stdout.splitlines())
    """
except subprocess.CalledProcessError:
    print(f"No process listening on port {port}")
    exit(1)

else:
    listening = None


    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            #print(listening)
            #print(listening.split()[2])
            break
    if listening:
        # PID is the second column in the output
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on port {port}")
        exit(1)



