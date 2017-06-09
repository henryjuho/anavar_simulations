#!/usr/bin/env python

import argparse
from qsub import *
import time
import sys


def q_wait(cmd, out, t, jid, evolgen, no_job_limit):
    qstat_grep = "Qstat | grep -c ^' '"
    no_sub = subprocess.Popen(qstat_grep, shell=True, stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
    no_sub = int(no_sub)
    if no_sub >= no_job_limit:
        time.sleep(15)
        q_wait(cmd, out, t, jid, evolgen, no_job_limit)
    else:
        q_sub([cmd], out=out, t=t, jid=jid, evolgen=evolgen)
    return


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1_r', help='Theta 1 range in form start,end,step', required=True)
    parser.add_argument('-t2_r', help='Theta 2 range in form start,end,step', default='None')
    parser.add_argument('-g1_r', help='Gamma 1 range in form start,end,step', required=True)
    parser.add_argument('-g2_r', help='Gamma 2 range in form start,end,step', default='None')
    parser.add_argument('-e1_r', help='Error 1 range in form start,end,step', required=True)
    parser.add_argument('-e2_r', help='Error 2 range in form start,end,step', default='None')
    parser.add_argument('-nrep', help='Number of replicates per parameter combination', required=True)
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    parser.add_argument('-sub', help='if specified will submit to cluster', default=False, action='store_true')
    parser.add_argument('-evolgen', help='If specified will run on evolgen', default=False, action='store_true')
    args = parser.parse_args()

    # submission loop
    if args.sub is True:
        command_line = [' '.join([x for x in sys.argv if x != '-sub'])]
        q_sub(command_line, args.o + '.controlscript', jid='test_anavar_control.sh', t=72, evolgen=args.evolgen)
        sys.exit()

    # variables
    n = args.n
    theta_range = [int(x) for x in args.t1_r.split(',')]
    theta_1s = range(theta_range[0], theta_range[1], theta_range[2])
    gamma_range = [int(x) for x in args.g1_r.split(',')]
    gamma_1s = range(gamma_range[0], gamma_range[1], gamma_range[2])
    e_range = [int(x) for x in args.e1_r.split(',')]
    error_1s = [float(x)/10.0 for x in range(e_range[0], e_range[1], e_range[2])]
    out = args.o
    nrep = args.nrep
    evolgen = args.evolgen

    # set second class variables
    if 'None' in [args.t2_r, args.g2_r, args.e2_r]:
        if 'None' == args.t2_r == args.g2_r == args.e2_r:
            theta_2s = ['None']
            gamma_2s = ['None']
            error_2s = ['None']
        else:
            sys.exit('Either all second class parameter ranges must be specified or none!')
    else:
        theta2_range = [int(x) for x in args.t2_r.split(',')]
        theta_2s = range(theta2_range[0], theta2_range[1], theta2_range[2])
        gamma2_range = [int(x) for x in args.g2_r.split(',')]
        gamma_2s = range(gamma2_range[0], gamma2_range[1], gamma2_range[2])
        e2_range = [int(x) for x in args.e2_r.split(',')]
        error_2s = [float(x)/10.0 for x in range(e2_range[0], e2_range[1], e2_range[2])]

    # all combinations
    counter = 0
    for t in theta_1s:
        for t2 in theta_2s:
            for g in gamma_1s:
                for g2 in gamma_2s:
                    if g2 == 'None':
                        g2_str = g2
                    else:
                        g2_str = '" ' + str(g2) + '"'
                    for e in error_1s:
                        for e2 in error_2s:
                            counter += 1
                            new_out = out + '.paramcomb' + str(counter)
                            best_out = new_out + '.bestlnL.txt'
                            test_script_cmd = ('~/anavar_simulations/test_anavar1.1.py '
                                               '-n ' + n + ' '
                                               '-t1 ' + str(t) + ' '
                                               '-t2 ' + str(t2) + ' '
                                               '-g1 " ' + str(g) + '" '
                                               '-g2 ' + g2_str + ' '
                                               '-e1 ' + str(e) + ' '
                                               '-e2 ' + str(e2) + ' '
                                               '-nrep ' + nrep + ' '
                                               '-o ' + new_out + ' '
                                               '>> ' + best_out)
                            q_wait(test_script_cmd, new_out, 24, 'paramcomb' + str(counter) + '.sh', evolgen, 1500)


if __name__ == '__main__':
    main()
