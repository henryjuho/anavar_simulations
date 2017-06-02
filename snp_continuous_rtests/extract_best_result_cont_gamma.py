#!/usr/bin/env python

import argparse
import os

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r_dir', help='Results file from anavar', required=True)
parser.add_argument('-t1', help='Theta 1', required=True)
parser.add_argument('-shape', help='Shape of the gamma distribution', required=True)
parser.add_argument('-scale', help='Scale parameter', required=True)
parser.add_argument('-e1', help='Error 1', required=True)
args = parser.parse_args()

# variables
r_files = sorted(sum([[[r + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                       for x in os.listdir(r) if x.endswith('results.txt')] for r in args.r_dir], []),
                 key=lambda y: [y[1], y[2]])
theta1 = args.t1
shape = args.shape
scale = args.scale
e1 = args.e1
counter = 0

columns = ['run', 'imp', 'exit_code', 'theta', 'shape', 'scale', 'e', 'lnL']

# process files
for x in r_files:
    counter += 1
    results_file = x[0]
    rep = results_file.split('.')[-4]
    model = results_file.split('.')[-3]

    # extract and print best result
    results = open(results_file).readlines()[4:6]

    header_line = results[0].rstrip('\n')
    header = header_line.split('\t')
    header_line += '\tsim_theta\tsim_shape\tsim_scale\tsim_e\tmodel\trep'
    hpos = {header[x]: x for x in range(0, len(header))}

    if counter == 1:
        print header_line
    best_result = results[1].rstrip('\n').split('\t')
    result_line = ''
    for col in columns:
        try:
            result_line += best_result[hpos[col]] + '\t'
        except KeyError:
            result_line += 'NA\t'

    sim_output_info = '\t'.join([theta1, shape, scale, e1, model, rep])
    print(result_line + sim_output_info)
