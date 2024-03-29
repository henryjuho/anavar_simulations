#!/usr/bin/env python

import argparse
import sys

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-control_file', help='control file to use as template', required=True)
parser.add_argument('-model', choices=['full', 'reduced'], default='full')
parser.add_argument('-out_dir', default='./')
args = parser.parse_args()

# variables
c_file = args.control_file
out_dir = args.out_dir
model = args.model

counter = 0
for sfs_line in sys.stdin:
    counter += 1
    with open(out_dir + c_file[:c_file.rfind('.')] + '.rep' + str(counter) + '.' + model + '.control.txt', 'w') \
            as out_control:
        for line in open(c_file):
            if line.startswith('sfs'):
                out_control.write('sfs: ' + sfs_line)
            else:
                out_control.write(line)
