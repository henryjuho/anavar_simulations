# Pipeline for testing anavar1.1 with simulated data

This repository contains scripts for simulating site frequency spectra with different distributions of fitness effects and classes of sites. 

## Required programs

* anavar1.1

## Required scripts

* snpdfe_spike_gen.withopts.m
* test_anavar1.1_1class.py

## Simple testing

A simple implementation of the model with one class of sites can be run on a set of neutral simulated SNPs with no polarisation error as follows:

```
$ python test_anavar1.1_1class.py -n 20 -t1 1000 -g1 0 -e1 0 -o /fastdata/bop15hjb/anavar_sims/1class_tests_1setsnps -H > /fastdata/bop15hjb/anavar_sims/1class_tests_1setsnps.bestlnL.txt
$
$ cat 1class_tests_1setsnps.bestlnL.txt 
run	imp	exit_code	data_1_theta_1	data_1_gamma_1	data_1_e_1	lnL	sim_theta_1	sim_gamma_1	sim_e_1
70	3	3	1055.99173407747	-0.441685579330643	0.0114752385708097	16677.7198398418	1000	0	0
```

## Multiple parameter combinations
### 1 set of SNPs, 1 class of sites

660 parameter combinations run as follows:

```
anavar_simulations/1_class_test_ranges.py -n 20 -t1_r 100,1100,50 -g1_r ' -50,60,10' -e1_r 1,4,1 -o /fastdata/bop15hjb/anavar_sims/1class_tests_1setsnps -bestlnL /fastdata/bop15hjb/anavar_sims/1class_tests_1setsnps.bestlnL.txt 
```

The resulting data was then plotted as follows:

```
rscript 1class_anavar1.1_plots.R 1class_tests_1setsnps.bestlnL.txt 
```

theta_plot: [](1class.1snps.anavar1.1.theta.jpg)
gamma plot:[](1class.1snps.anavar1.1.gamma.jpg)
error plot: [](1class.1snps.anavar1.1.error.jpg)

### 1 set of SNPs, 2 classes of sites

17820 parameter combinations with two site classes were run as follows:

```
anavar_simulations/2_class_test_ranges.py -n 20 -t1_r 100,1100,50 -t2_r 100,1100,450 -g1_r "' -50,60,10'" -g2_r "' -50,20,30'" -e1_r 1,4,1 -e2_r 1,4,1 -o /fastdata/bop15hjb/anavar_sims/2class_sims/2class_test_1setsnps -bestlnL /fastdata/bop15hjb/anavar_sims/2class_sims/2class_test_1setsnps.bestlnL.txt -sub
```

The resulting data was then plotted as follows:

```
rscript 2class_anavar1.1_plots.R 2class_test_1setsnps.bestlnL.txt 
```

theta plot: [](2class.1snps.anavar1.1.theta.jpg)
gamma plot: [](2class.1snps.anavar1.1.gamma.jpg)
error plot: [](2class.1snps.anavar1.1.error.jpg)

### 1 set of SNPs, 2 class of sites, 100 replicates per combination

16 parameter combinations, each repeated 100 times were run as follows:

```
anavar_simulations/2_class_test_ranges.v2.py -n 20 -t1_r 500,1100,500 -t2_r 100,400,200 -g1_r "' -25,0,20'" -g2_r "' -10,5,10'" -e1_r 0,1,1 -e2_r 0,1,1 -nrep 100 -o /fastdata/bop15hjb/anavar_sims/2class_sims_reps/16_paramcombs -bestlnL /fastdata/bop15hjb/anavar_sims/2class_sims_reps/16_paramcombs_bestlnL.txt -sub
```

### 1 set of SNPs, 2 class of sites, 100 replicates per combination high theta

16 parameter combinations, each repeated 100 times were run as follows:

```
anavar_simulations/2_class_test_ranges.v3.py -n 20 -t1_r 5000,11000,5000 -t2_r 1000,4000,2000 -g1_r ' -25,0,20' -g2_r ' -10,5,10' -e1_r 0,1,1 -e2_r 0,1,1 -nrep 100 -o /fastdata/bop15hjb/anavar_sims/2class_sims_reps_corrected_highertheta/16_paramcombs_hightheta -bestlnL /fastdata/bop15hjb/anavar_sims/2class_sims_reps_corrected_highertheta/16_paramcombs_hightheta_bestlnL.txt
```

### 1 set of folded SNPs, 2 class of sites, 100 reps, 1 parameter combination

```bash
#!/bin/bash

#$-l arch=intel*
#$-l h_rt=8:00:00
#$-l mem=6G
#$-l rmem=2G

#$-P evolgen
#$-q evolgen.q

#$-N qsub_1_folded_comb_job.sh
#$-o /fastdata/bop15hjb/anavar_sims/2class_sims_hightheta_folded/1_folded_comb.out
#$-e /fastdata/bop15hjb/anavar_sims/2class_sims_hightheta_folded/1_folded_comb.error

anavar_simulations/test_anavar1.1_2class_reps_foldopts.py -n 20 -t1 10000 -t2 3000 -g1 ' -5' -g2 0 -e1 0 -e2 0 -nrep 100 -folded -o /fastdata/bop15hjb/anavar_sims/2class_sims_hightheta_folded/1_folded_comb >> /fastdata/bop15hjb/anavar_sims/2class_sims_hightheta_folded/1_folded_comb_bestlnL.txt
```
Submitted as follows:

```
qsub /fastdata/bop15hjb/anavar_sims/2class_sims_hightheta_folded/one_comb_job.sh
```

# anavar1.2 testing
## intial test 1 param comb 100 reps

```
anavar_simulations/test_anavar1.2_multi.py -n 50 -t1 100000 -shape 0.3 -scale 50 -e1 0 -nrep 100 -o /fastdata/bop15hjb/anavar_sims/anavar1.2/run_two_multi/test2
~/anavar_simulations/extract_best_result.py -r_dir ./ -t1 100000 -shape 0.3 -scale 50 -e1 0 > test2.bestlnL.txt
./process_anavar1.2_reps.py -in_dir ~/iceberg_fastdata/anavar_sims/anavar1.2/run_two_multi/> anavar1.2_estimates_run1.csv
```

results: <https://github.com/henryjuho/anavar_simulations/blob/master/anavar1.2_estimates_run1.csv>