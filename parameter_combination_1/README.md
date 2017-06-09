```bash
# likelihood ratio tests - length 10^5 bp
$ cd /fastdata/bop15hjb/anavar_sims/snp_2class_ratio_tests/
$ wolfram -script snpdfe_spike_gen.m 

$ cat sfs/100_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_full.txt -model full -out_dir full/
$ cat sfs/100_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_t.txt -model reduced -out_dir equal_t/
$ cat sfs/100_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_e.txt -model reduced -out_dir equal_e/
$ cat sfs/100_sfs.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_all.txt -model reduced -out_dir equal_all_1class/

$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_t/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_e/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_all_1class/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 

$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_all_1class/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_all.bestlnL.txt 
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_t/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_t.bestlnL.txt 
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_e/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_e.bestlnL.txt 

$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_all.bestlnL.txt -df 3 > rtest_2class_snp_full_equal_all.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_t.bestlnL.txt > rtest_2class_snp_full_equal_t.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_e.bestlnL.txt > rtest_2class_snp_full_equal_e.csv

$ head -n 1 rtest_2class_snp_full_equal_all.csv | while read i; do echo $i,reduction; done > rtest_2class_snp.csv
$ grep -v ^e rtest_2class_snp_full_equal_all.csv | while read i; do echo $i,1class; done >> rtest_2class_snp.csv 
$ grep -v ^e rtest_2class_snp_full_equal_t.csv | while read i; do echo $i,equal_t; done >> rtest_2class_snp.csv 
$ grep -v ^e rtest_2class_snp_full_equal_e.csv | while read i; do echo $i,equal_e; done >> rtest_2class_snp.csv  
```