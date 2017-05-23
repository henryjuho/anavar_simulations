#!/usr/bin/env python

import sys
from qsub import *

for line in sys.stdin:

    control_file = line.rstrip()
    results_file = control_file.replace('.control.txt', '.results.txt')
    log_file = control_file.replace('.control.txt', '.log.txt')

    q_sub(['~/anavar1.2_23_05_17 {} {} {}'.format(control_file, results_file, log_file)],
          out=control_file.replace('.control.txt', ''), t=2)
