#!/usr/bin/env python

from __future__ import print_function
import argparse
import subprocess


def read_sim_sfs(sfs_file):
    sfs_line = ',\t'.join(open(sfs_file).readlines()[0].rstrip('\n').split())
    return sfs_line


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1', help='Theta 1', required=True)
    parser.add_argument('-g1', help='Gamma 1', required=True)
    parser.add_argument('-e1', help='Error 1', required=True)
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    parser.add_argument('-H', help='If specified will print header in output', default=False, action='store_true')
    args = parser.parse_args()

    # variables
    n = args.n
    theta = args.t1
    gamma = args.g1
    e = args.e1
    out = args.o
    sfs_file = out + '.sfs.txt'
    control_file = out + '.control.txt'
    results_file = out + '.results.txt'
    log_file = out + '.log.txt'
    header = args.H

    # simulate data and read it in
    sim_cmd = 'wolfram -script snpdfe_spike_gen.withopts.m ' + n + ' ' + theta + ' ' + gamma + ' ' + e + ' ' + sfs_file
    subprocess.call(sim_cmd, shell=True)
    sfs = read_sim_sfs(sfs_file)

    # write control file
    control_contents = ('num_sets: 1\n'
                        'search_algorithm: NLOPT_LD_SLSQP\n'
                        'maxeval: 100000\n'
                        'maxtime: 600\n'
                        'num_searches: 100\n'
                        'nnoimp: 3\n'
                        'maximp: 5\n\n'
                        'begin[data_1]\n'
                        'type: snp\n'
                        'n: ' + n + '\n'
                        'm: 1\n'
                        'folded: false\n'
                        'sfs: ' + sfs + '\n'
                        'dfe: discrete\n'
                        'c: 1\n'
                        'theta_range: 1, 10000\n'
                        'gamma_range: -500, 100\n'
                        'e_range: 0, 1\n'
                        'end[data_1]')
    with open(control_file, 'w') as control:
        control.write(control_contents)

    # run anavar1.1 on simulated data
    anavar_cmd = 'anavar1.1 ' + control_file + ' ' + results_file + ' ' + log_file
    subprocess.call(anavar_cmd, shell=True)

    # extract and print best result
    results = open(results_file).readlines()[4:6]
    header_line = results[0].rstrip('\n') + '\tsim_theta_1\tsim_gamma_1\tsim_e_1'
    best_result = results[1].rstrip('\n') + '\t' + '\t'.join([theta, gamma, e])
    if header is True:
        print(header_line)
    print(best_result)

if __name__ == '__main__':
    main()
