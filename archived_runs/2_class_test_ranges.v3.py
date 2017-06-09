#!/usr/bin/env python

import argparse
from qsub import *
import time
import sys


def q_wait(cmd, out, t, jid, no_job_limit):
    qstat_grep = "Qstat | grep -c ^' '"
    no_sub = subprocess.Popen(qstat_grep, shell=True, stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
    no_sub = int(no_sub)
    if no_sub >= no_job_limit:
        time.sleep(15)
        q_wait(cmd, out, t, jid, no_job_limit)
    else:
        q_sub([cmd], out=out, t=t, jid=jid)
    return


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='Sample size', required=True)
    parser.add_argument('-t1_r', help='Theta 1 range in form start,end,step', required=True)
    parser.add_argument('-t2_r', help='Theta 2 range in form start,end,step', required=True)
    parser.add_argument('-g1_r', help='Gamma 1 range in form start,end,step', required=True)
    parser.add_argument('-g2_r', help='Gamma 2 range in form start,end,step', required=True)
    parser.add_argument('-e1_r', help='Error 1 range in form start,end,step', required=True)
    parser.add_argument('-e2_r', help='Error 2 range in form start,end,step', required=True)
    parser.add_argument('-nrep', help='Number of replicates per parameter combination', required=True)
    parser.add_argument('-o', help='Output dir and file prefix', required=True)
    parser.add_argument('-bestlnL', help='File to append best result to', required=True)
    parser.add_argument('-sub', help='if specified will submit to cluster', default=False, action='store_true')
    args = parser.parse_args()

    # submission loop
    if args.sub is True:
        command_line = [' '.join([x for x in sys.argv if x != '-sub'])]
        q_sub(command_line, args.o + '.controlscript', jid='two_class_control.sh', t=72)
        sys.exit()

    # variables
    n = args.n
    theta_range = [int(x) for x in args.t1_r.split(',')]
    gamma_range = [int(x) for x in args.g1_r.split(',')]
    e_range = [int(x) for x in args.e1_r.split(',')]
    theta2_range = [int(x) for x in args.t2_r.split(',')]
    gamma2_range = [int(x) for x in args.g2_r.split(',')]
    e2_range = [int(x) for x in args.e2_r.split(',')]
    out = args.o
    nrep = args.nrep
    best_result_file = args.bestlnL

    # all combinations
    counter = 0
    for t in range(theta_range[0], theta_range[1], theta_range[2]):
        for t2 in range(theta2_range[0], theta2_range[1], theta2_range[2]):
            for g in range(gamma_range[0], gamma_range[1], gamma_range[2]):
                for g2 in range(gamma2_range[0], gamma2_range[1], gamma2_range[2]):
                    for e in range(e_range[0], e_range[1], e_range[2]):
                        error = float(e)/10.0
                        for e2 in range(e2_range[0], e2_range[1], e2_range[2]):
                            error2 = float(e2)/10.0
                            counter += 1
                            new_out = out + '.paramcomb' + str(counter)
                            test_script_cmd = ('~/anavar_simulations/test_anavar1.1_2class_reps.py '
                                               '-n ' + n + ' '
                                               '-t1 ' + str(t) + ' '
                                               '-t2 ' + str(t2) + ' '
                                               '-g1 " ' + str(g) + '" '
                                               '-g2 " ' + str(g2) + '" '
                                               '-e1 ' + str(error) + ' '
                                               '-e2 ' + str(error2) + ' '
                                               '-nrep ' + nrep + ' '
                                               '-o ' + new_out + ' '
                                               '>> ' + best_result_file)
                            q_wait(test_script_cmd, new_out, 24, 'paramcomb' + str(counter) + '.sh', 1500)


if __name__ == '__main__':
    main()
