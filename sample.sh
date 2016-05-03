#!/usr/bin/env bash

chr='03'
chromosome_length=316620
sample_length=$((chromosome_length*2))
model='GRU'
size='128-2'

for i in 0{1..5} ; do
    python sample.py --save_dir $(pwd)'/models/'$model'/chr-'$chr'/'$size -n $sample_length > $(pwd)'/data/Samples/'$model'/chr-'$chr'/'$size'/sample-'$i'.txt'
done