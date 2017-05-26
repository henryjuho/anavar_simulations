```bash
# comb 1
$ wolfram -script snpdfe_spike_gen.m
$ cat ../sim_data_kaiparam.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_1.txt
$ ls *control.txt | cut -d '.' -f 1-2 | while read i; do ../anavar1.2/anavar $i.control.txt $i.results.txt $i.log.txt; done
$ ls *results.txt | cut -d '.' -f 1,2 | while read i; do mv $i.results.txt $i.full.results.txt; done
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir ./ -t1 500 -t2 1000 -g1 0 -g2 " -10" -e1 0.01 -e2 0.05 > snp_2class_anavar1.2.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -in_dir ./ > snp_2class_anavar1.2.summarised.csv

# comb 2
$ wolfram -script snpdfe_spike_gen.m 
$ cat snp2_class_1.2_comb2.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_1.txt
$ ls *control.txt | cut -d '.' -f 1,2 | while read i; do mv $i.control.txt $i.full.control.txt; done
$ ls *control.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir ./ -t1 0.005 -t2 0.01 -g1 0 -g2 " -10" -e1 0.01 -e2 0.05 > snp_2class_anavar1.2_comb2.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -in_dir ./ > snp_2class_anavar1.2_comb2.summarised.csv

# comb 3
$ wolfram -script snpdfe_spike_gen.m 
$ cat snp2_class_1.2_comb3.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file comb3_5fold_increase_t.txt 
$ ls *control.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir ./ -t1 0.005 -t2 0.01 -g1 0 -g2 " -10" -e1 0.01 -e2 0.05 > snp_2class_anavar1.2_comb3.bestlnL.txt

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


# likelihood ratio tests - length 10^5 bp - both gamma negative
$ cd /fastdata/bop15hjb/anavar_sims/snp_2class_rtest_2neg_g_1e5bp/
$ wolfram -script 4.m
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_full.txt -model full -out_dir full/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_t.txt -model reduced -out_dir equal_t/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_e.txt -model reduced -out_dir equal_e/
$ cat 100sfs_2neg_g_1e5bp.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file rtest_2class_snp_equal_all.txt -model reduced -out_dir equal_all/
$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_t/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_e/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls equal_all/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_all/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_all_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_t/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_t_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir full/ -r_dir equal_e/ -t1 0.005 -t2 0.01 -g1 " -5" -g2 " -20" -e1 0.05 -e2 0.01 > rtest_2class_snp_full_equal_e_2neg_g_1e5bp.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_all_2neg_g_1e5bp.bestlnL.txt -df 3 > rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_t_2neg_g_1e5bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_t_2neg_g_1e5bp.csv
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -lnL rtest_2class_snp_full_equal_e_2neg_g_1e5bp.bestlnL.txt -df 1 > rtest_2class_snp_full_equal_e_2neg_g_1e5bp.csv
$ head -n 1 rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv | while read i; do echo $i,reduction; done > rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_all_2neg_g_1e5bp.csv | while read i; do echo $i,1class; done >> rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_t_2neg_g_1e5bp.csv | while read i; do echo $i,equal_t; done >> rtest_2class_snp_2neg_g_1e5bp.csv
$ grep -v ^e rtest_2class_snp_full_equal_e_2neg_g_1e5bp.csv | while read i; do echo $i,equal_e; done >> rtest_2class_snp_2neg_g_1e5bp.csv

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