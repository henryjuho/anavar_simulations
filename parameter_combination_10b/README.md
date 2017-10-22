```bash
$ mkdir /fastdata/bop15hjb/anavar_sims/snp_3class_rtest_1e7_b
$ cd /fastdata/bop15hjb/anavar_sims/snp_3class_rtest_1e7_b
$ cp ~/anavar_simulations/parameter_combination_10b/9_1e7bp.m ./
$ cp ~/anavar_simulations/parameter_combination_10b/comb_10b_* ./
$ mkdir full equal_pol 2class no_pol
$ wolfram -script 9_1e7bp.m

$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_10b_full.txt -model full -out_dir full/
$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_10b_equal_pol.txt -model reduced -out_dir equal_pol/
$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_10b_2class.txt -model reduced -out_dir 2class/   
$ cat 100sfs_3class_1e7.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_10b_no_pol.txt -model reduced -out_dir no_pol/

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -t 96
$ ls equal_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -t 96
$ ls 2class/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -t 96
$ ls no_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -t 96

$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir equal_pol/ > comb_10b_full_equal_pol.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir 2class/ > comb_10b_full_2class.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir no_pol/ > comb_10b_full_no_pol.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_10b_full_equal_pol.bestlnL.txt -df 2 > comb_10b_full_equal_pol.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_10b_full_2class.bestlnL.txt -df 3 > comb_10b_full_2class.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_10b_full_no_pol.bestlnL.txt -df 3 > comb_10b_full_no_pol.csv

$ head -n 1 comb_10b_full_equal_pol.csv | while read i; do echo $i,reduction; done > rtest_snp_3class_comb10b.csv
$ grep -v ^e comb_10b_full_equal_pol.csv | while read i; do echo $i,equal_pol; done >> rtest_snp_3class_comb10b.csv
$ grep -v ^e comb_10b_full_2class.csv | while read i; do echo $i,2_class; done >> rtest_snp_3class_comb10b.csv
$ grep -v ^e comb_10b_full_no_pol.csv | while read i; do echo $i,no_pol; done >> rtest_snp_3class_comb10b.csv 

$ cp *best* ~/anavar_simulations/parameter_combination_10b/
$ cp *csv ~/anavar_simulations/parameter_combination_10b/
```