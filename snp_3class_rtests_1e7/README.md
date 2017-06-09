```bash
$ cd /fastdata/bop15hjb/anavar_sims/snp_3class_rtest_1e7
$ wolfram -script 9_1e7bp.m

$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file comb_9_full.txt -model full -out_dir full/
$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file comb_9_equal_pol.txt -model reduced -out_dir equal_pol/
$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file comb_9_2class.txt -model reduced -out_dir 2class/   

$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_pol/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls 2class/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 

$
```