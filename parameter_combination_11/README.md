```bash
$ cd /fastdata/bop15hjb/anavar_sims/indel_1class_rtest
$ wolfram -script ~/anavar_simulations/scripts/indeldfe_spike_gen_2e6.m 50 0.0005 0.001 " -5" " -15" 0.02 0.02 100 100_sfs_indels_1class_2e6.txt

$ cat 100_sfs_indels_1class_2e6.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param11.control.txt -mode INDEL -out_dir full/ -model full
$ cat 100_sfs_indels_1class_2e6.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param11.equal_gamma.control.txt -mode INDEL -out_dir equal_gamma/ -model reduced
$ cat 100_sfs_indels_1class_2e6.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file indel_param11.no_pol.control.txt -mode INDEL -out_dir no_pol/ -model reduced

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
$ ls no_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
$ ls equal_gamma/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
```