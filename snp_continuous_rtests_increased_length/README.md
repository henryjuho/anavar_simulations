```bash
$ cd /home/bop15hjb/anavar_simulations/snp_continuous_rtests_increased_length/
$ wolfram -script snpdfe_gamma_gen.m 
$ cp 100sfs_cont_gamma_long.txt /fastdata/bop15hjb/anavar_sims/snp_cont_rtest_longer/
$ cd /fastdata/bop15hjb/anavar_sims/snp_cont_rtest_longer/

$ cat 100sfs_cont_gamma_long.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_cont_gamma_full.txt -model full -out_dir full/
$ cat 100sfs_cont_gamma_long.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_cont_gamma_1class.txt -model reduced -out_dir 1class/
$ cat 100sfs_cont_gamma_long.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_cont_gamma_no_pol.txt -model reduced -out_dir no_pol/

$ ls full/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 
$ ls no_pol/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py
$ ls 1class/*txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/parallel_anavar_runs.py 

$ watch 'echo -e "r\nqw" | while read i; do Qstat | grep -cw $i; done'

$ ~/anavar_simulations/snp_continuous_rtests/extract_best_result_cont_gamma.py -r_dir full/ -r_dir no_pol/ -t1 0.005 -shape 0.3 -scale 50 -e1 0.05 > rtest_snp_cont_gamma_long_full_nopol.bestlnL.txt
$ ~/anavar_simulations/snp_continuous_rtests/extract_best_result_cont_gamma.py -r_dir full/ -r_dir 1class/ -t1 0.005 -shape 0.3 -scale 50 -e1 0.05 > rtest_snp_cont_gamma_long_full_1class.bestlnL.txt

$ ~/anavar_simulations/snp_continuous_rtests/process_anavar1.2_reps_snp_cont.py -lnL rtest_snp_cont_gamma_long_full_nopol.bestlnL.txt -df 2 > rtest_snp_cont_gamma_long_full_nopol.csv
$ ~/anavar_simulations/snp_continuous_rtests/process_anavar1.2_reps_snp_cont.py -lnL rtest_snp_cont_gamma_long_full_1class.bestlnL.txt > rtest_snp_cont_gamma_long_full_1class.csv

$ head -n 1 rtest_snp_cont_gamma_long_full_nopol.csv | while read i; do echo $i,reduction; done > rtest_snp_cont_gamma_long.csv
$ grep -v ^e rtest_snp_cont_gamma_long_full_nopol.csv | while read i; do echo $i,no_pol; done >> rtest_snp_cont_gamma_long.csv
$ grep -v ^e rtest_snp_cont_gamma_long_full_1class.csv | while read i; do echo $i,1_class; done >> rtest_snp_cont_gamma_long.csv
```