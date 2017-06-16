```bash
$ mkdir /fastdata/bop15hjb/anavar_sims/snp_3class_rtest_5e6
$ cd /fastdata/bop15hjb/anavar_sims/snp_3class_rtest_5e6

$ wolfram -script ~/anavar_simulations/parameter_combination_8/8.m
$ mkdir full equal_pol 2class no_pol no_pol_gmax200 no_pol_gmax5000
$ cp ~/anavar_simulations/parameter_combination_8/*txt ./

$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_full.txt -model full -out_dir full/
$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_equal_pol.txt -model reduced -out_dir equal_pol/
$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_2class.txt -model reduced -out_dir 2class/
$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_no_pol.txt -model reduced -out_dir no_pol/
$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_no_pol_gmax200.txt -model reduced -out_dir no_pol_gmax200/
$ cat 100_sfs_comb8.txt | ~/anavar_simulations/scripts/sim_sfs2control_file.py -control_file snp_1_comb8_control_no_pol_gmax5000.txt -model reduced -out_dir no_pol_gmax5000/

$ ls full/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls equal_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls 2class/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py 
$ ls no_pol/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
$ ls no_pol_gmax200/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py
$ ls no_pol_gmax5000/*txt | ~/anavar_simulations/scripts/parallel_anavar_runs.py

# awaiting gmax5000 results

$ ~/anavar_simulations/scripts/extract_best_result_3class.py -r_dir full/ -r_dir equal_pol/ -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 > comb_8_full_equal_pol.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -r_dir full/ -r_dir 2class/ -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 > comb_8_full_2class.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -r_dir full/ -r_dir no_pol/ -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 > comb_8_full_no_pol.bestlnL.txt
$ ~/anavar_simulations/scripts/extract_best_result_3class.py -r_dir full/ -r_dir no_pol_gmax200/ -t 0.002,0.006,0.002 -g 0,-5,-30 -e 0.05,0.02,0.01 > comb_8_full_no_pol_gmax200.bestlnL.txt

$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_8_full_equal_pol.bestlnL.txt -df 2 > comb_8_full_equal_pol.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_8_full_2class.bestlnL.txt -df 3 > comb_8_full_2class.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_8_full_no_pol.bestlnL.txt -df 3 > comb_8_full_no_pol.csv
$ ~/anavar_simulations/scripts/process_anavar1.2_reps_snp_3class.py -lnL comb_8_full_no_pol_gmax200.bestlnL.txt -df 3 > comb_8_full_no_pol_gmax200.csv

$ head -n 1 comb_8_full_equal_pol.csv | while read i; do echo $i,reduction; done > rtest_snp_3class_5e6.csv
$ grep -v ^e comb_8_full_equal_pol.csv | while read i; do echo $i,equal_pol; done >> rtest_snp_3class_5e6.csv
$ grep -v ^e comb_8_full_2class.csv | while read i; do echo $i,2_class; done >> rtest_snp_3class_5e6.csv
$ grep -v ^e comb_8_full_no_pol.csv | while read i; do echo $i,no_pol; done >> rtest_snp_3class_5e6.csv
$ grep -v ^e comb_8_full_no_pol_gmax200.csv | while read i; do echo $i,no_pol_gmax_200; done >> rtest_snp_3class_5e6.csv
```