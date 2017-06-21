```bash
$ mkdir /fastdata/bop15hjb/anavar_sims/indel_comb13_rtest
$ cd /fastdata/bop15hjb/anavar_sims/indel_comb13_rtest

$ wolfram -script ~/anavar_simulations/scripts/indeldfe_spike_gen_2e6.m 50 0.0005 0.001 " -5" " -15" 0.08 0.04 100 100_sfs_indels_comb13_2e6.txt

$ cat 100_sfs_indels_comb13_2e6.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param13.control.txt -mode INDEL -out_dir full/ -model full

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py

$ ~/anavar_simulations/scripts/extract_best_result_1.2_indel_disc.py -ti 0.0005 -td 0.001 -gi " -5" -gd " -15" -ei 0.08 -ed 0.04 -r_dir full/ > comb_13_full.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_indel_disc.py -lnL comb_13_full.bestlnL.txt > comb_13_full.csv 
```