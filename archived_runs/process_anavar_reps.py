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
    parser.add_argument('-in_dir', help='Directory containing best lnL files', required=True)
    args = parser.parse_args()

    # variables
    lnl_files = [args.in_dir + x for x in os.listdir(args.in_dir) if x.endswith('.bestlnL.txt')]

    # get mean, sd, 95% CIs and do log likelihood test for each file
    file_counter = 0
    for param_comb in lnl_files:
        file_counter += 1
        pc_data = open(param_comb).readlines()
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

            # one class model
            if len(header) == 12:
                for est in ['theta', 'gamma', 'e']:
                    data = full[hpos['data_1_' + est + '_1']]
                    sim = full[hpos['sim_' + est + '_1']]
                    if est not in estimates.keys():
                        estimates[est] = [data]
                        simulated_values[est] = sim
                    else:
                        estimates[est].append(data)

            # two class model
            else:
                number_conserved = True
                for est in ['theta', 'gamma', 'e']:
                    data_a = full[hpos['data_1_' + est + '_1']]
                    sim_1 = full[hpos['sim_' + est + '_1']]
                    data_b = full[hpos['data_1_' + est + '_2']]
                    sim_2 = full[hpos['sim_' + est + '_2']]

                    # order by theta
                    if est == 'theta':
                        if abs(float(data_a) - float(sim_1)) < abs(float(data_a) - float(sim_2)):
                            number_conserved = True
                        else:
                            number_conserved = False
                    if number_conserved is True:
                        data_tup = (data_a, data_b)
                    else:
                        data_tup = (data_b, data_a)

                    sim_tup = (sim_1, sim_2)

                    # add data to dict
                    for site_class in [1, 2]:
                        if est + '_' + str(site_class) not in estimates.keys():
                            estimates[est + '_' + str(site_class)] = [data_tup[site_class-1]]
                            simulated_values[est + '_' + str(site_class)] = sim_tup[site_class-1]
                        else:
                            estimates[est + '_' + str(site_class)].append(data_tup[site_class-1])

            full_lnl = float(full[hpos['lnL']])
            reduced_lnl = float(reduced[hpos['lnL']])
            p = lnl_ratio_test(full_lnl, reduced_lnl, 1)
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
