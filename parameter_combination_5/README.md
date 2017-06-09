```bash
# likelihood ratio tests - length 10^6 bp - both gamma negative
$ cd /fastdata/bop15hjb/anavar_sims/snp_2class_rtest_2neg_g_1e6bp
$ wolfram -script 5.m

$ cat 100sfs_2neg_g_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_all.1e6bp.txt -model reduced -out_dir equal_all/
$ cat 100sfs_2neg_g_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_t.1e6bp.txt -model reduced -out_dir equal_t/
$ cat 100sfs_2neg_g_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_e.1e6bp.txt -model reduced -out_dir equal_e/
$ cat 100sfs_2neg_g_1e6bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_full.1e6bp.txt -model full -out_dir full/

$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_t/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_e/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_all/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py

$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_all/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_all_2neg_g_1e6bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_t/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_t_2neg_g_1e6bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_e/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_e_2neg_g_1e6bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_all_2neg_g_1e6bp.bestlnL.txt -df 3 > rtest_2class_snp_full_equal_all_2neg_g_1e6bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_t_2neg_g_1e6bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_t_2neg_g_1e6bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_e_2neg_g_1e6bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_e_2neg_g_1e6bp.csv

$ head -n 1 rtest_2class_snp_full_equal_all_2neg_g_1e6bp.csv | while read i; do echo $i,reduction; done > rtest_2class_snp_2neg_g_1e6bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_all_2neg_g_1e6bp.csv | while read i; do echo $i,1class; done >> rtest_2class_snp_2neg_g_1e6bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_t_2neg_g_1e6bp.csv | while read i; do echo $i,equal_t; done >> rtest_2class_snp_2neg_g_1e6bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_e_2neg_g_1e6bp.csv | while read i; do echo $i,equal_e; done >> rtest_2class_snp_2neg_g_1e6bp.csv
```