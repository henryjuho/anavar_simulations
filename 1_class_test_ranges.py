#!/usr/bin/env python

import argparse
from qsub import *


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1_r', help='Theta 1', required=True)
    parser.add_argument('-g1_r', help='Gamma 1', required=True)
    parser.add_argument('-e1_r', help='Error 1', required=True)
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    parser.add_argument('-bestlnL', help='File to append best result to', required=True)
    args = parser.parse_args()

    # variables
    n = args.n
    theta_range = [int(x) for x in args.t1_r.split(',')]
    gamma_range = [int(x) for x in args.g1_r.split(',')]
    e_range = [int(x) for x in args.e1_r.split(',')]
    out = args.o
    best_result_file = args.bestlnL

    # all combinations
    counter = 0
    for t in range(theta_range[0], theta_range[1], theta_range[2]):
        for g in range(gamma_range[0], gamma_range[1], gamma_range[2]):
            for e in range(e_range[0], e_range[1], e_range[2]):
                counter += 1
                new_out = out + '.combi' + str(counter)
                test_script_cmd = ('~/anavar_simulations/test_anavar1.1_1class.py '
                                   '-n ' + n + ' '
                                   '-t1 ' + str(t) + ' '
                                   '-g1 ' + str(g) + ' '
                                   '-e1 ' + str(e) + ' '
                                   '-o ' + new_out + ' '
                                   '>> ' + best_result_file)
                q_print([test_script_cmd], out=new_out)


if __name__ == '__main__':
    main()
