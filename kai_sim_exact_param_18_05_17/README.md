```bash
$ wolfram -script snpdfe_spike_gen.m
$ cat ../sim_data_kaiparam.txt | ~/anavar_simulations/kai_sim_exact_param_18_05_17/sim_sfs2control_file.py -control_file snp_1.txt
$ ls *control.txt | cut -d '.' -f 1-2 | while read i; do ../anavar1.2/anavar $i.control.txt $i.results.txt $i.log.txt; done
```