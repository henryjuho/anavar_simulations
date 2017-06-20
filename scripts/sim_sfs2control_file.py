#!/usr/bin/env python

import argparse
import sys

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-control_file', help='control file to use as template', required=True)
parser.add_argument('-model', choices=['full', 'reduced'], default='full')
parser.add_argument('-mode', help='SNP or INDEL', default='SNP')
parser.add_argument('-out_dir', default='./')
args = parser.parse_args()

# variables
c_file = args.control_file
mode = args.mode
out_dir = args.out_dir
model = args.model

counter = 0
if mode == 'SNP':
    for sfs_line in sys.stdin:
        counter += 1
        with open(out_dir + c_file[:c_file.rfind('.')] + '.rep' + str(counter) + '.' + model + '.control.txt', 'w') \
                as out_control:
            for line in open(c_file):
                if line.startswith('sfs'):
                    out_control.write('sfs: ' + sfs_line)
                else:
                    out_control.write(line)
else:
    sfs_holder = []
    rep_count = 1
    for sfs_line in sys.stdin:
        counter += 1
        if counter % 3 == 0:
            sfs_holder = []
            rep_count += 1
            continue
        else:
            sfs_holder.append(sfs_line)

            if len(sfs_holder) == 2:
                with open(out_dir + c_file[:c_file.rfind('.')] + '.rep' + str(rep_count) +
                          '.' + model + '.control.txt', 'w') as out_control:
                    for line in open(c_file):
                        if line.startswith('ins_sfs'):
                            out_control.write('ins_sfs: ' + sfs_holder[0])
                        elif line.startswith('del_sfs'):
                            out_control.write('del_sfs: ' + sfs_holder[1])
                        else:
                            out_control.write(line)
