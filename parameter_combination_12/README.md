```bash
$ mkdir /fastdata/bop15hjb/anavar_sims/indel_comb12_1class_rtest
$ cd /fastdata/bop15hjb/anavar_sims/indel_comb12_1class_rtest

$ wolfram -script ~/anavar_simulations/scripts/indeldfe_gamma_gen_2e6.m 50 0.0005 0.001 0.5 0.25 10 50 0.02 0.02 100 100_sfs_indels_continuous_2e6.txt

$ cat 100_sfs_indels_continuous_2e6.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param12.control.txt -mode INDEL -out_dir full/ -model full

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
```