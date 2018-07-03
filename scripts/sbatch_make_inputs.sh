#!/bin/bash

sbatch --ntasks=1 --cpus-per-task=1 --partition=isi --time=96:00:00 --mem-per-cpu=48GB ./make_inputs.sh

squeue -n make_inputs.sh