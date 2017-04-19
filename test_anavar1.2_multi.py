#!/usr/bin/env python

from __future__ import print_function
import argparse
import sys
from qsub import *


def read_sim_sfs(sfs_file):
    """
    reads in sfs file from mathmatica script output
    :param sfs_file: str
    :return: list
    """
    sfs_line = ['\t'.join(x.rstrip('\n').split()) for x in open(sfs_file).readlines()]
    return sfs_line


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1', help='Theta 1', required=True)
    parser.add_argument('-t2', help='Theta 2', default='None')
    parser.add_argument('-shape', help='Shape of the gamma distribution', required=True)
    parser.add_argument('-scale', help='Scale parameter', required=True)
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
    shape = args.shape
    scale = args.scale
    e1 = args.e1
    e2 = args.e2
    nreps = args.nrep
    out = args.o
    folded = str(args.folded)
    sfs_file = out + '.sfs.txt'
    classes = 2

    # constraint dict
    constraint_dict = {'full': {1: 'none', 2: 'none'},
                       'reduced': {1: 'no_pol_error', 2: 'no_pol_error'}}

    # checks
    if 'None' in [theta2, e2]:
        if theta2 == e2 == 'None':
            classes = 1
        else:
            sys.exit('Either all second class parameters must be specified or none!')

    # simulate data and read it in
    if classes == 2:
        # sim_cmd = ('wolfram -script ~/anavar_simulations/snpdfe_spike_gen.v2.withopts_2class_reps_foldopt.m ' +
        #            ' '.join([n, theta1, theta2, shape, scale, e1, e2, nreps, folded, sfs_file]))
        sys.exit('Only 1 class of sites supported at present')
    else:
        sim_cmd = ('wolfram -script ~/anavar_simulations/snpdfe_gamma_gen.m ' +
                   ' '.join([n, theta1, shape, scale, e1, nreps, folded, sfs_file]))

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
            control_contents = ('search_algorithm: NLOPT_LD_SLSQP\n'
                                'maxeval: 100000\n'
                                'maxtime: 600\n'
                                'num_searches: 100\n'
                                'nnoimp: 3\n'
                                'maximp: 5\n\n'
                                'optional: false\n\n'
                                'model: SNP_1\n'
                                'n: ' + n + '\n'
                                'm: 1\n'
                                'folded: ' + folded.lower() + '\n'
                                'sfs: ' + spectrum + '\n'
                                'dfe: continuous\n'
                                'distribution: reflected_gamma\n'
                                'theta_range: 1, 200000\n'
                                'shape_range: 0.1, 200\n'
                                'scale_range: 0.1, 200\n'
                                'e_range: 0, 1\n'
                                'constraint: ' + constraint_dict[x][classes] + '\n'
                                'optional: true\n'
                                'fraction: 0.001\n'
                                'delta: 1e-7\n'
                                'degree: 75')
            with open(control_file, 'w') as control:
                control.write(control_contents)

            # run anavar1.2 on simulated data
            anavar_cmd = 'anavar1.2 ' + control_file + ' ' + results_file + ' ' + log_file
            q_sub([anavar_cmd], out=results_file + '_runout', evolgen=True)

            # # extract and print best result
            # results = open(results_file).readlines()[4:6]
            # header_line = results[0].rstrip('\n')
            # if classes == 2:
            #     # header_line += '\tsim_theta_1\tsim_theta_2\tsim_gamma_1\tsim_gamma_2\tsim_e_1\tsim_e_2\tmodel\trep'
            #     # best_result = results[1].rstrip('\n') + '\t' + \
            #     #     '\t'.join([theta1, theta2, gamma1, gamma2, e1, e2, x, str(rep_counter)])
            #     pass
            # else:
            #     header_line += '\tsim_theta_1\tshape\tscale\tsim_e_1\tmodel\trep'
            #     best_result = results[1].rstrip('\n') + '\t' + \
            #         '\t'.join([theta1, shape, scale, e1, x, str(rep_counter)])
            # if rep_counter == 1 and x == 'full':
            #     print(header_line)
            # print(best_result)

if __name__ == '__main__':
    main()
