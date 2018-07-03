#!/bin/bash
source activate scpn

SRC_FOLDER="/auto/nlg-05/huan183/scpn"
DATA_FOLDER="$SRC_FOLDER/data"
OUT_FOLDER="/auto/nlg-05/huan183/generated_paraphrases"

cd $SRC_FOLDER

python $SRC_FOLDER/generate_paraphrases.py \
  --parsed_input_file $DATA_FOLDER/generated_input.tsv \
  --out_file $OUT_FOLDER/scpn_ex.out
