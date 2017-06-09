#!/usr/bin/env python

import sys
from qsub import *
import os

for line in sys.stdin:

    pwd = os.getcwd()

    control_file = line.rstrip()
    results_file = control_file.replace('.control.txt', '.results.txt')
    log_file = control_file.replace('.control.txt', '.log.txt')

    q_sub(['cd {}'.format(pwd),
           '~/anavar1.2_24_05_17 {} {} {}'.format(control_file, results_file, log_file)],
          out=pwd + '/' + control_file.replace('.control.txt', ''), t=2)
