#!/usr/bin/env python

import argparse
import os


def both_files_pass(file1, file2):

    for x in [file1, file2]:
        length = len(open(x).readlines())

        if length < 10:
            return False

    return True


# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r_dir', help='Results file from anavar', required=True, action='append')
parser.add_argument('-t', help='Thetas, comma sep', required=True)
parser.add_argument('-g', help='Gammas, comma sep', required=True)
parser.add_argument('-e', help='Error, comma sep', required=True)
args = parser.parse_args()

# variables
r_files = sorted(sum([[[r + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                       for x in os.listdir(r) if x.endswith('results.txt')] for r in args.r_dir], []),
                 key=lambda y: [y[1], y[2]])
theta = args.t.split(',')
gamma = args.g.split(',')
e = args.e.split(',')
counter = 0

columns = ['run', 'imp', 'exit_code',
           'theta_1', 'gamma_1', 'e_1',
           'theta_2', 'gamma_2', 'e_2',
           'theta_3', 'gamma_3', 'e_3', 'lnL']

# process files
for i in range(0, len(r_files), 2):

    # check contents
    paired_files = r_files[i: i+2]

    if not both_files_pass(paired_files[0][0], paired_files[1][0]):
        continue

    for x in paired_files:

        counter += 1
        results_file = x[0]
        rep = results_file.split('.')[-4]
        model = results_file.split('.')[-3]

        # extract and print best result
        results = open(results_file).readlines()[4:6]

        header_line = results[0].rstrip('\n')
        header = header_line.split('\t')
        header_line += ('\tsim_theta_1\tsim_gamma_1\tsim_e_1\t'
                        'sim_theta_2\tsim_gamma_2\tsim_e_2\t'
                        'sim_theta_3\tsim_gamma_3\tsim_e_3\t'
                        'model\trep')
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

        sim_output_info = '\t'.join([theta[0], gamma[0], e[0],
                                     theta[1], gamma[1], e[1],
                                     theta[2], gamma[2], e[2],
                                     model, rep])
        print(result_line + sim_output_info)
