```bash
# likelihood ratio tests - length 10^5 bp - both gamma negative
$ cd /fastdata/bop15hjb/anavar_sims/snp_2class_rtest_2neg_g_1e5bp/
$ wolfram -script 4.m

$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file rtest_2class_snp_full.txt -model full -out_dir full/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_t.txt -model reduced -out_dir equal_t/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_e.txt -model reduced -out_dir equal_e/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_all.txt -model reduced -out_dir equal_all/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file rtest_2class_snp_no_pol.txt -model reduced -out_dir no_pol/

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls equal_t/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls equal_e/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls equal_all/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
$ ls no_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 

$ ~/anavar_simulations/scripts/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_all/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_all_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_t/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_t_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_e/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_e_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir no_pol/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_no_pol_2neg_g_1e5bp.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_all_2neg_g_1e5bp.bestlnL.txt -df 3 > rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_t_2neg_g_1e5bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_t_2neg_g_1e5bp.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_e_2neg_g_1e5bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_e_2neg_g_1e5bp.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_no_pol_2neg_g_1e5bp.bestlnL.txt -df 2 > rtest_2class_snp_full_no_pol_2neg_g_1e5bp.csv

$ head -n 1 rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv | while read i; do echo $i,reduction; done > rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv | while read i; do echo $i,1class; done >> rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_t_2neg_g_1e5bp.csv | while read i; do echo $i,equal_t; done >> rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_e_2neg_g_1e5bp.csv | while read i; do echo $i,equal_e; done >> rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_no_pol_2neg_g_1e5bp.csv | while read i; do echo $i,no_pol; done >> rtest_2class_snp_2neg_g_1e5bp.csv
```