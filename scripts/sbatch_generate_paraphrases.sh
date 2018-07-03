#!/bin/bash

sbatch --ntasks=1 --cpus-per-task=1 --partition=isi --time=72:00:00 --mem-per-cpu=48GB --gres=gpu:1 ./generate_paraphrases.sh

squeue -n generate_paraphrases.sh