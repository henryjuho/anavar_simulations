```bash
# likelihood ratio tests - length 10^6 bp
$ cd /fastdata/bop15hjb/anavar_sims/snp_2class_ratio_tests_1e6bp/
$ wolfram -script snpdfe_spike_gen.m 

$ cat 100sfs_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_full.1e6bp.txt -model full -out_dir full/
$ cat 100sfs_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_all.1e6bp.txt -model full -out_dir equal_all/
$ cat 100sfs_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_t.1e6bp.txt -model full -out_dir equal_t/
$ cat 100sfs_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_e.1e6bp.txt -model full -out_dir equal_e/

$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_t/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_e/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_all/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py

$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_all/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_all_1e6bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_t/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_t_1e6bp.bestlnL.txt 
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_e/ -t1 0.005 -t2 0.01 -g1 0 -g2 ' -10' -e1 0.01 -e2 0.05 > rtest_2class_snp_full_equal_e_1e6bp.bestlnL.txt 

$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_all_1e6bp.bestlnL.txt -df 3 > rtest_2class_snp_full_equal_all_1e6bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_t_1e6bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_t_1e6bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_e_1e6bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_e_1e6bp.csv
```