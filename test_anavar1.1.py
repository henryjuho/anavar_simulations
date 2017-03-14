#!/usr/bin/env python

from __future__ import print_function
import argparse
import subprocess
import sys


def read_sim_sfs(sfs_file):
    """
    reads in sfs file from mathmatica script output
    :param sfs_file: str
    :return: list
    """
    sfs_line = [',\t'.join(x.rstrip('\n').split()) for x in open(sfs_file).readlines()]
    return sfs_line


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1', help='Theta 1', required=True)
    parser.add_argument('-t2', help='Theta 2', default='None')
    parser.add_argument('-g1', help='Gamma 1', required=True)
    parser.add_argument('-g2', help='Gamma 2', default='None')
    parser.add_argument('-e1', help='Error 1', required=True)
    parser.add_argument('-e2', help='Error 2', default='None')
    parser.add_argument('-nrep', help='Number of replicates', required=True)
    parser.add_argument('-folded', help='If specified will run in folded mode', default=False, action='store_true')
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    args = parser.parse_args()

    # variables
    n = args.n
    theta1 = args.t1
    theta2 = args.t2
    gamma1 = args.g1
    gamma2 = args.g2
    e1 = args.e1
    e2 = args.e2
    nreps = args.nrep
    out = args.o
    folded = str(args.folded)
    sfs_file = out + '.sfs.txt'
    classes = 2

    # constraint dict
    constraint_dict = {'full': {1: 'none', 2: 'none'},
                       'reduced': {1: 'constant{data_1_e_1, 0}', 2: 'constant{data_1_e_1, 0}; constant{data_1_e_2, 0}'}}

    # checks
    if 'None' in [theta2, gamma2, e2]:
        if theta2 == gamma2 == e2 == 'None':
            classes = 1
        else:
            sys.exit('Either all second class parameters must be specified or none!')

    # simulate data and read it in
    if classes == 2:
        sim_cmd = ('wolfram -script ~/anavar_simulations/snpdfe_spike_gen.v2.withopts_2class_reps_foldopt.m ' +
                   ' '.join([n, theta1, theta2, gamma1, gamma2, e1, e2, nreps, folded, sfs_file]))
    else:
        sim_cmd = ('wolfram -script ~/anavar_simulations/snpdfe_spike_gen.v2.withopts_1class_reps_foldopt.m ' +
                   ' '.join([n, theta1, gamma1, e1, nreps, folded, sfs_file]))

    subprocess.call(sim_cmd, shell=True)
    sfs = read_sim_sfs(sfs_file)

    rep_counter = 0
    for spectrum in sfs:
        # set rep specific variables
        rep_counter += 1
        for x in ['full', 'reduced']:

            control_file = out + '.rep' + str(rep_counter) + '.' + x + '.control.txt'
            results_file = out + '.rep' + str(rep_counter) + '.' + x + '.results.txt'
            log_file = out + '.rep' + str(rep_counter) + '.' + x + '.log.txt'

            # write control file
            control_contents = ('num_sets: 1\n\n'
                                'use_r: false\n'
                                'r_range:\n\n'
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
                                'folded: ' + folded.lower() + '\n'
                                'sfs: ' + spectrum + '\n'
                                'dfe: discrete\n'
                                'c: ' + str(classes) + '\n'
                                'theta_range: 1, 100000\n'
                                'gamma_range: -500, 100\n'
                                'e_range: 0, 1\n'
                                'constraint: ' + constraint_dict[x][classes] + '\n\n'
                                'end[data_1]')
            with open(control_file, 'w') as control:
                control.write(control_contents)

            # run anavar1.1 on simulated data
            anavar_cmd = 'anavar1.1 ' + control_file + ' ' + results_file + ' ' + log_file
            subprocess.call(anavar_cmd, shell=True)

            # extract and print best result
            results = open(results_file).readlines()[4:6]
            header_line = results[0].rstrip('\n')
            if classes == 2:
                header_line += '\tsim_theta_1\tsim_theta_2\tsim_gamma_1\tsim_gamma_2\tsim_e_1\tsim_e_2\tmodel'
                best_result = results[1].rstrip('\n') + '\t' + '\t'.join([theta1, theta2, gamma1, gamma2, e1, e2, x])
            else:
                header_line += '\tsim_theta_1\tsim_gamma_1\tsim_e_1\tmodel'
                best_result = results[1].rstrip('\n') + '\t' + '\t'.join([theta1, gamma1, e1, x])
            if rep_counter == 1 and x == 'full':
                print(header_line)
            print(best_result)

if __name__ == '__main__':
    main()
