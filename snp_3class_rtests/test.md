```bash
$ cd /fastdata/bop15hjb/anavar_sims/snp_3class_rtest/test
$ wolfram -script snpdfe_spike_gen_test.m 

$ cat test_3class_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp1_3class_test_slsqp.txt -model full -out_dir ./
$ cat test_3class_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp1_3class_test_lbfgs.txt -model full -out_dir ./

$ ls *control.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py
```

# algorithm comparison

| algorithm  | max likelihood   |
|:-----------|:----------------:|
| lbfgs      | 173879.314827899 |
| slsqp      | 173879.3005447   |