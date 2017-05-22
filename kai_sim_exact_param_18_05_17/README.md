```bash
$ wolfram -script snpdfe_spike_gen.m
$ cat ../sim_data_kaiparam.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_1.txt
$ ls *control.txt | cut -d '.' -f 1-2 | while read i; do ../anavar1.2/anavar $i.control.txt $i.results.txt $i.log.txt; done
$ ls *results.txt | cut -d '.' -f 1,2 | while read i; do mv $i.results.txt $i.full.results.txt; done
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/extract_best_result_1.2_snp_2class.py -r_dir ./ -t1 500 -t2 1000 -g1 0 -g2 " -10" -e1 0.01 -e2 0.05 > snp_2class_anavar1.2.bestlnL.txt
$ ~/anavar_simulations/kai_sim_exact_param_18_05_17/process_anavar1.2_reps_snp_2class.py -in_dir ./ > snp_2class_anavar1.2.summarised.csv
```