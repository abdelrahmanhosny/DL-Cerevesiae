#!/usr/bin/env bash
# A script to train all models on all chromosomes with all variations
# WARNING: this script will suck your machine resources for a long time.


for i in 0{1..9} {10..16} ; do
    train_file=$(pwd)'/data/Preprocessed/chr'$i'-input.txt'

    echo 'Training on' $train_file >> training.log

    # LSTM model with different hyper-parameters
    model=LSTM
    rnn_size=128
    number_layers=2
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=256
    number_layers=3
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=512
    number_layers=4
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    # RNN model with different hyper-parameters
    model=RNN
    rnn_size=128
    number_layers=2
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=256
    number_layers=3
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=512
    number_layers=4
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    # GRU model with different hyper-parameters
    model=GRU
    rnn_size=128
    number_layers=2
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=256
    number_layers=3
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    rnn_size=512
    number_layers=4
    save_dir=$(pwd)'/models/'$model'/chr-'$i'/'$rnn_size'-'$number_layers
    echo 'model='$model', Hidden state size='$rnn_size', Number of layers='$number_layers >> training.log
    SECONDS=0
    python train.py --train_file $train_file --save_dir $save_dir
    duration=$SECONDS
    echo "Training finished after $(($duration / 60)) minutes and $(($duration % 60)) seconds." >> training.log

    # remove temp files from data/Preprocessed directory
    rm $(pwd)'/data/Preprocessed/data.npy'
    rm $(pwd)'/data/Preprocessed/vocab.pkl'
    echo '' >> training.log
done