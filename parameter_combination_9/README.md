```bash
$ cd /fastdata/bop15hjb/anavar_sims/snp_3class_rtest
$ wolfram -script 9.m

$ cat 100sfs_3class.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_9_full.txt -model full -out_dir full/
$ cat 100sfs_3class.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_9_equal_pol.txt -model reduced -out_dir equal_pol/
$ cat 100sfs_3class.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_9_2class.txt -model reduced -out_dir 2class/   
$ cat 100sfs_3class.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file comb_9_no_pol_gmax200.txt -model reduced -out_dir no_pol_gmax200/

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls equal_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls 2class/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls no_pol_gmax200/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py -evolgen

$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir equal_pol/ > comb_9_full_equal_pol.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir 2class/ > comb_9_full_2class.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 -r_dir full/ -r_dir no_pol_gmax200/ > comb_9_full_no_pol_gmax200.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_9_full_equal_pol.bestlnL.txt -df 2 > comb_9_full_equal_pol.csv 
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_9_full_2class.bestlnL.txt -df 3 > comb_9_full_2class.csv         
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_9_full_no_pol_gmax200.bestlnL.txt -df 3 > comb_9_full_no_pol_gmax200.csv

$ head -n 1 comb_9_full_equal_pol.csv | while read i; do echo $i,reduction; done > rtest_snp_3class.csv
$ grep -v ^e comb_9_full_equal_pol.csv | while read i; do echo $i,equal_pol; done >> rtest_snp_3class.csv
$ grep -v ^e comb_9_full_2class.csv | while read i; do echo $i,2_class; done >> rtest_snp_3class.csv
$ grep -v ^e comb_9_full_no_pol_gmax200.csv | while read i; do echo $i,no_pol_gmax200; done >> rtest_snp_3class.csv
```