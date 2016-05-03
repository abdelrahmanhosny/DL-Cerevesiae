#!/usr/bin/env bash

chr='02'
chromosome_length=813184
sample_length=$((chromosome_length*2))
model='LSTM'
size='512-4'

for i in 0{1..5} ; do
    python sample.py --save_dir $(pwd)'/models/'$model'/chr-'$chr'/'$size -n $sample_length > $(pwd)'/data/Samples/'$model'/chr-'$chr'/'$size'/sample-'$i'.txt'
done