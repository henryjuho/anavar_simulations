#!/usr/bin/env python

import argparse
import os

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r_dir', help='Results file from anavar', required=True)
parser.add_argument('-ti', help='Theta insertions', required=True)
parser.add_argument('-td', help='Theta deletions', required=True)
parser.add_argument('-shi', help='Shape of the insertion gamma distribution', required=True)
parser.add_argument('-shd', help='Shape of the deletion gamma distribution', required=True)
parser.add_argument('-sci', help='Insertion scale parameter', required=True)
parser.add_argument('-scd', help='Deletion scale parameter', required=True)
parser.add_argument('-ei', help='Error insertion', required=True)
parser.add_argument('-ed', help='Error deletion', required=True)
args = parser.parse_args()

# variables
r_files = sorted([[args.r_dir + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                  for x in os.listdir(args.r_dir) if x.endswith('results.txt')], key=lambda y: [y[1], y[2]])
ti = args.ti
td = args.td
shape_i = args.shi
shape_d = args.shd
scale_i = args.sci
scale_d = args.scd
ei = args.ei
ed = args.ed
counter = 0

# process files
for x in r_files:
    counter += 1
    results_file = x[0]
    rep = results_file.split('.')[-4]
    model = results_file.split('.')[-3]

    # extract and print best result
    results = open(results_file).readlines()[4:6]
    header_line = results[0].rstrip('\n')
    header_line += ('\tsim_ins_theta\tsim_del_theta\tsim_ins_shape\tsim_del_shape\t'
                    'sim_ins_scale\tsim_del_scale\tsim_ins_e\tsim_del_e\tmodel\trep')
    if counter == 1:
        print header_line
    best_result = results[1].rstrip('\n') + '\t' + '\t'.join([ti, td, shape_i, shape_d, scale_i,
                                                              scale_d, ei, ed, model, rep])
    print(best_result)
