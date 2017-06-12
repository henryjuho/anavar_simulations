#!/usr/bin/env python

import argparse
import os

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r_dir', help='Results file from anavar', required=True, action='append')
parser.add_argument('-ti', help='Theta insertions', required=True)
parser.add_argument('-td', help='Theta deletions', required=True)
parser.add_argument('-gi', help='Insertion gamma', required=True)
parser.add_argument('-gd', help='Deletions gamma', required=True)
parser.add_argument('-ei', help='Error insertion', required=True)
parser.add_argument('-ed', help='Error deletion', required=True)
args = parser.parse_args()

# variables
r_files = sorted(sum([[[r + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                       for x in os.listdir(r) if x.endswith('results.txt')] for r in args.r_dir], []),
                 key=lambda y: [y[1], y[2]])
ti = args.ti
td = args.td
gi = args.gi
gd = args.gd
ei = args.ei
ed = args.ed
counter = 0

columns = ['run', 'imp', 'exit_code',
           'ins_theta_1', 'ins_gamma_1', 'ins_e_1',
           'del_theta_1', 'del_gamma_1', 'del_e_1',
           'lnL']

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

    header_line += ('\tsim_ins_theta_1\tsim_del_theta_1\tsim_ins_gamma_1\tsim_del_gamma_1\t'
                    'sim_ins_e_1\tsim_del_e_1\tmodel\trep')
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
