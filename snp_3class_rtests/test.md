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

## class 1


| algorithm  | t1_sim  | t1                  | g1_sim | g1                 | e1_sim | e1                 |
|:-----------|:-------:|:-------------------:|:------:|:------------------:|:------:|:------------------:|
| lbfgs      | 0.002   | 0.00518015050123047 | -30    | -20.4893214278676  | 0.01   | 0.0581505624669593 |
| slsqp      | 0.002   | 0.0049769205711556  | -30    | -20.3818282560781  | 0.01   | 0.0427560550164048 |

## class 2

| algorithm  | t2_sim  | t2                  | g2_sim | g2               | e2_sim | e2                 |
|:-----------|:-------:|:-------------------:|:------:|:----------------:|:------:|:------------------:|
| lbfgs      | 0.002   | 0.00105368954219491 | 0      | 5.13414718474554 | 0.05   | 0.179975591721926  |
| slsqp      | 0.002   | 0.00129982704605483 | 0      | 3.30717425770066 | 0.05   | 0.0216148473255148 |

## class 3

| algorithm  | t3_sim  | t3                  | g3_sim | g3                  | e3_sim | e3                  |
|:-----------|:-------:|:-------------------:|:------:|:-------------------:|:------:|:-------------------:|
| lbfgs      | 0.006   | 0.0132675353693578  | -5     |  -3.46121293739909  | 0.02   | 0.00159055716210438 |
| slsqp      | 0.006   | 0.0131942695061416  | -5     |  -3.57533684424745  | 0.02   | 0.0199314199688972  |
