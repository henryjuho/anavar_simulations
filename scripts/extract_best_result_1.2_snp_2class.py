#!/usr/bin/env python

import argparse
import os

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r_dir', help='Results file from anavar', required=True, action='append')
parser.add_argument('-t1', help='Theta 1', required=True)
parser.add_argument('-t2', help='Theta 2', required=True)
parser.add_argument('-g1', help='Insertion 1', required=True)
parser.add_argument('-g2', help='Deletions 2', required=True)
parser.add_argument('-e1', help='Error 1', required=True)
parser.add_argument('-e2', help='Error 2', required=True)
args = parser.parse_args()

# variables
r_files = sorted(sum([[[r + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                       for x in os.listdir(r) if x.endswith('results.txt')] for r in args.r_dir], []),
                 key=lambda y: [y[1], y[2]])
ti = args.t1
td = args.t2
gi = args.g1
gd = args.g2
ei = args.e1
ed = args.e2
counter = 0

columns = ['run', 'imp', 'exit_code', 'theta_1', 'gamma_1', 'e_1', 'theta_2', 'gamma_2', 'e_2', 'lnL']

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
    hpos = {header[x]: x for x in range(0, len(header))}

    header_line += ('\tsim_theta_1\tsim_theta_2\tsim_gamma_1\tsim_gamma_2\t'
                    'sim_e_1\tsim_e_2\tmodel\trep')
    if counter == 1:
        print header_line
    best_result = results[1].rstrip('\n').split('\t')
    result_line = ''
    for col in columns:
        try:
            result_line += best_result[hpos[col]] + '\t'
        except KeyError:
            result_line += '0\t'

    sim_output_info = '\t'.join([ti, td, gi, gd, ei, ed, model, rep])
    print(result_line + sim_output_info)
