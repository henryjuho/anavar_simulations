```bash
$ mkdir /fastdata/bop15hjb/anavar_sims/indel_comb14
$ cd /fastdata/bop15hjb/anavar_sims/indel_comb14

$ cp ~/anavar_simulations/parameter_combination_14/indel_param14.control.txt ./
$ mkdir full/

$ wolfram -script ~/anavar_simulations/scripts/indeldfe_gamma_gen_2e7.m 50 0.0005 0.001 0.5 0.25 10 50 0.08 0.04 100 100_sfs_indels_continuous_2e7.txt

$ cat 100_sfs_indels_continuous_2e7.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param14.control.txt -mode INDEL -out_dir full/ -model full

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -t 48

$ ~/anavar_simulations/scripts/extract_best_result_1.2_indel.py -ti 0.0005 -td 0.001 -shi 0.5 -shd 0.25 -sci 10 -scd 50  -ei 0.08 -ed 0.04 -r_dir full/ > comb_14_full.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_indel.py -lnL comb_14_full.bestlnL.txt > comb_14_full.csv
```