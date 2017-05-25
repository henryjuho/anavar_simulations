#!/usr/bin/env python

from __future__ import print_function
import argparse
import os
from scipy import stats
import numpy as np


def lnl_ratio_test(l_full, l_reduced, df):
    diff = 2 * (l_full - l_reduced)
    pval = stats.chi2.sf(diff, df)
    return pval


def summarise_estimates(est_list):
    est_list = np.array(est_list, dtype=float)
    mean = np.mean(est_list)
    std_dev = np.std(est_list)
    ci = np.percentile(est_list, [2.5, 97.5])
    return mean, std_dev, ci[0], ci[1]


def perecent_sig(lnl_list):
    number_sig = 0
    for z in lnl_list:
        if z <= 0.05:
            number_sig += 1
    return round(number_sig/float(len(lnl_list))*100.0, 2)


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-lnL', help='best lnL file', required=True)
    parser.add_argument('-df', help='degrees of freedom', default=1, type=int)
    args = parser.parse_args()

    # variables
    lnl_files = args.lnL  # [args.in_dir + x for x in os.listdir(args.in_dir) if x.endswith('.bestlnL.txt')]
    df = args.df

    # get mean, sd, 95% CIs and do log likelihood test for each file
    file_counter = 0
    #for param_comb in lnl_files:
    file_counter += 1
    pc_data = open(lnl_files).readlines()
    header = pc_data[0].split('\t')
    reps = pc_data[1:]
    hpos = {header[x]: x for x in range(0, len(header))}
    simulated_values = {}
    estimates = {}
    ratio_ps = []

    # extract data from file, perform ratio test
    for i in range(0, len(reps), 2):
        full = reps[i].split('\t')
        reduced = reps[i+1].split('\t')

        sim_same_pred = True
        for par in ['theta_', 'gamma_', 'e_']:
            data_1 = full[hpos[par + '1']]
            data_2 = full[hpos[par + '2']]
            sim_1 = full[hpos['sim_' + par + '1']]
            sim_2 = full[hpos['sim_' + par + '2']]

            if par == 'theta_':
                if abs(float(data_1)-float(sim_1)) < abs(float(data_1)-float(sim_2)):
                    sim_same_pred = True
                else:
                    sim_same_pred = False

            if sim_same_pred is True:
                pred_1 = data_1
                pred_2 = data_2
            else:
                pred_1 = data_2
                pred_2 = data_1

            if par + '1' not in estimates.keys():
                estimates[par + '1'] = [pred_1]
                estimates[par + '2'] = [pred_2]
                simulated_values[par + '1'] = sim_1
                simulated_values[par + '2'] = sim_2
            else:
                estimates[par + '1'].append(pred_1)
                estimates[par + '2'].append(pred_2)

        full_lnl = float(full[hpos['lnL']])
        reduced_lnl = float(reduced[hpos['lnL']])
        p = lnl_ratio_test(full_lnl, reduced_lnl, df)
        ratio_ps.append(p)

    # fire up the calculator
    header = ''
    output_string = ''
    for param in sorted(estimates.keys()):
        header += param.join(['', '_sim,', '_mean,', '_sd,', '_lwr,', '_upr,'])
        output_string += simulated_values[param] + ','
        output_string += ','.join([str(x) for x in summarise_estimates(estimates[param])]) + ','
    header += 'percent_sig'
    output_string += str(perecent_sig(ratio_ps))

    if file_counter == 1:
        print(header)
    print(output_string)

if __name__ == '__main__':
    main()
