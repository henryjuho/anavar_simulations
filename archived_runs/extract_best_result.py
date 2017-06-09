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
r_files = sorted([[args.r_dir + x, int(x.split('.')[-4].strip('rep')), x.split('.')[-3]]
                  for x in os.listdir(args.r_dir) if x.endswith('results.txt')], key=lambda y: [y[1], y[2]])
theta1 = args.t1
shape = args.shape
scale = args.scale
e1 = args.e1
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
    header_line += '\tsim_theta\tsim_shape\tsim_scale\tsim_e\tmodel\trep'
    if counter == 1:
        print header_line
    best_result = results[1].rstrip('\n') + '\t' + '\t'.join([theta1, shape, scale, e1, model, rep])
    print(best_result)
