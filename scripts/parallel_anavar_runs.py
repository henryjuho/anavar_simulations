#!/usr/bin/env python

import sys
from qsub import *
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-evolgen', help='If specified will run on lab queue', default=False, action='store_true')
args = parser.parse_args()

for line in sys.stdin:

    pwd = os.getcwd()

    control_file = line.rstrip()
    results_file = control_file.replace('.control.txt', '.results.txt')
    log_file = control_file.replace('.control.txt', '.log.txt')

    q_sub(['cd {}'.format(pwd),
           '~/anavar1.2_24_05_17 {} {} {}'.format(control_file, results_file, log_file)],
          out=pwd + '/' + control_file.replace('.control.txt', ''), t=2,
          evolgen=args.evolgen)
