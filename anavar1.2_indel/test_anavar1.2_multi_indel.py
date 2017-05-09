#!/usr/bin/env python

from __future__ import print_function
import argparse
from qsub import *


def read_sim_sfs(sfs_file):
    """
    reads in sfs file from mathmatica script output
    :param sfs_file: str
    :return: list
    """
    sfs_line = ['\t'.join(x.rstrip('\n').split()) for x in open(sfs_file).readlines() if not x.startswith('\n')]
    indel_sfs = [(sfs_line[i], sfs_line[i+1]) for i in range(0, len(sfs_line), 2)]
    return indel_sfs


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-ti', help='Theta insertions', required=True)
    parser.add_argument('-td', help='Theta deletions', required=True)
    parser.add_argument('-shi', help='Shape of the insertion gamma distribution', required=True)
    parser.add_argument('-shd', help='Shape of the deletion gamma distribution', required=True)
    parser.add_argument('-sci', help='Insertion scale parameter', required=True)
    parser.add_argument('-scd', help='Deletion scale parameter', required=True)
    parser.add_argument('-ei', help='Error insertion', required=True)
    parser.add_argument('-ed', help='Error deletion', required=True)
    parser.add_argument('-nrep', help='Number of replicates', required=True)
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    parser.add_argument('-evolgen', help='If specified will run on lab queue', default=False, action='store_true')
    args = parser.parse_args()

    # variables
    n = args.n
    ti = args.ti
    td = args.td
    shape_i = args.shi
    shape_d = args.shd
    scale_i = args.sci
    scale_d = args.scd
    ei = args.ei
    ed = args.ed
    nreps = args.nrep
    out = args.o
    sfs_file = out + '.sfs.txt'
    classes = 2

    # constraint dict
    constraint_dict = {'full': {1: 'none', 2: 'none'},
                       'reduced': {1: 'no_pol_error', 2: 'no_pol_error'}}

    # simulate data and read it in
    sim_cmd = ('wolfram -script ~/anavar_simulations/anavar1.2_indel/indeldfe_gamma_gen.m ' +
               ' '.join([n, ti, td, shape_i, shape_d, scale_i, scale_d, ei, ed, nreps, sfs_file]))

    subprocess.call(sim_cmd, shell=True)
    sfs = read_sim_sfs(sfs_file)

    rep_counter = 0
    for spectrum in sfs:
        # set rep specific variables
        rep_counter += 1
        i_sfs = spectrum[0]
        d_sfs = spectrum[1]

        for x in ['full']:  # , 'reduced']:

            control_file = out + '.rep' + str(rep_counter) + '.' + x + '.control.txt'
            results_file = out + '.rep' + str(rep_counter) + '.' + x + '.results.txt'
            log_file = out + '.rep' + str(rep_counter) + '.' + x + '.log.txt'

            # write control file
            control_contents = ('[algorithm_commands]\n'
                                'search_algorithm: NLOPT_LD_SLSQP\n'
                                'maxeval: 100000\n'
                                'maxtime: 600\n'
                                'num_searches: 20\n'
                                'nnoimp: 1\n'
                                'maximp: 5\n\n'
                                'optional: false\n\n'
                                '[model_commands]\n'
                                'model: INDEL_1\n'
                                'n: ' + n + '\n'
                                'm: 1\n'
                                'ins_sfs: ' + i_sfs + '\n'
                                'del_sfs: ' + d_sfs + '\n'
                                'dfe: continuous\n'
                                'distribution: reflected_gamma\n'
                                'ins_theta_range: 1, 200000\n'
                                'ins_shape_range: 0.1, 200\n'
                                'ins_scale_range: 0.1, 200\n'
                                'ins_e_range: 0, 1\n'
                                'del_theta_range: 1, 200000\n'
                                'del_shape_range: 0.1, 200\n'
                                'del_scale_range: 0.1, 200\n'
                                'del_e_range: 0, 1\n'
                                'constraint: ' + constraint_dict[x][classes] + '\n'
                                'optional: true\n'
                                'fraction: 0.001\n'
                                'delta: 1e-7\n'
                                'degree: 75')
            with open(control_file, 'w') as control:
                control.write(control_contents)

            # run anavar1.2 on simulated data
            anavar_cmd = '~/anavar1.2_indel/anavar ' + control_file + ' ' + results_file + ' ' + log_file
            q_sub([anavar_cmd], out=results_file + '_runout', evolgen=args.evolgen)

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
