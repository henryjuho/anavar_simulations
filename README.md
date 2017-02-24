# Pipeline for testing anavar1.1 with simulated data

This repository contains scripts for simulating site frequency spectra with different distributions of fitness effects and classes of sites. 

# Required scripts

* snpdfe_spike_gen.withopts.m
* test_anavar1.1_1class.py

# Simple testing

A simple implementation of the model with one class of sites can be run on a set of neutral simulated SNPs with no polarisation error as follows:

```
$ python test_anavar1.1_1class.py -n 20 -t1 1000 -g1 0 -e1 0 -o /fastdata/bop15hjb/anavar_sims/pipelinetest
```