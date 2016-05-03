from Bio import SeqIO
import os

'''
Test the samples resulting from the models (RNN, GRU, LSTM):
1. Compute hamming distance between the sample and the original training data
'''

data_path = 'Saccharomyces-Cerevisiae'
preprocessed_data_path = 'Preprocessed'
samples_path = 'Samples'
chromosomes = ["dummy"]     # just include a dummy value at location 0

def hamming_distance(genome1, genome2):
    hammingdistance = 0
    # truncate to the shorter string
    if len(genome1) < len(genome2):
        genome2 = genome2[:len(genome1)]
    elif len(genome1) > len(genome2):
        genome1 = genome1[:len(genome2)]

    for i in range(0, len(genome1)):
        if genome1[i] != genome2[i]:
            hammingdistance += 1
    return hammingdistance

for chromosome_number in range(1, 4):
    chromosome = preprocessed_data_path + '/chr%02d-input.txt'%chromosome_number
    confirmed_origins = data_path + '/chr%02d-confirmed.fsa'%chromosome_number

    with open(chromosome, 'r') as chromosome_file:
        chromosome = chromosome_file.readline()
        chromosome = chromosome.replace(' ', '')
        chromosomes.append(chromosome)

    # Samples of RNN
    rnn_samples = []
    path=samples_path + '/RNN/chr-%02d/'%chromosome_number
    s_128_2 = [f for f in os.listdir(path + '/128-2/')]
    for sample_file in s_128_2:
        path=samples_path + '/RNN/chr-%02d/'%chromosome_number + '/128-2/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            rnn_samples.append(sample)
    path=samples_path + '/RNN/chr-%02d/'%chromosome_number
    s_256_3 = [f for f in os.listdir(path + '/256-3/')]
    for sample_file in s_256_3:
        path=samples_path + '/RNN/chr-%02d/'%chromosome_number + '/256-3/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            rnn_samples.append(sample)
    path=samples_path + '/RNN/chr-%02d/'%chromosome_number
    s_512_4 = [f for f in os.listdir(path + '/512-4/')]
    for sample_file in s_512_4:
        path=samples_path + '/RNN/chr-%02d/'%chromosome_number + '/512-4/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            rnn_samples.append(sample)

    print 'Chromosome ' + str(chromosome_number)
    print 'Hamming Distance in RNN Samples (from smallest RNN size to largest RNN size):'
    hamming = []
    for sample in rnn_samples:
        hamming.append(hamming_distance(sample, chromosome))
    average = sum(hamming) / len(hamming)
    print ', '.join(map(str, hamming))
    print 'average hamming distance is ' + str(average)
    print 'percentage of mismatches is ' + str(float(average)/float(len(chromosome))*100) + '%'
    print ''

    # Samples of LSTM
    lstm_samples = []
    path=samples_path + '/LSTM/chr-%02d/'%chromosome_number
    s_128_2 = [f for f in os.listdir(path + '/128-2/')]
    for sample_file in s_128_2:
        path=samples_path + '/LSTM/chr-%02d/'%chromosome_number + '/128-2/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            lstm_samples.append(sample)
    path=samples_path + '/LSTM/chr-%02d/'%chromosome_number
    s_256_3 = [f for f in os.listdir(path + '/256-3/')]
    for sample_file in s_256_3:
        path=samples_path + '/LSTM/chr-%02d/'%chromosome_number + '/256-3/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            lstm_samples.append(sample)
    path=samples_path + '/LSTM/chr-%02d/'%chromosome_number
    s_512_4 = [f for f in os.listdir(path + '/512-4/')]
    for sample_file in s_512_4:
        path=samples_path + '/LSTM/chr-%02d/'%chromosome_number + '/512-4/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            lstm_samples.append(sample)

    print 'Hamming Distance in LSTM Samples (from smallest RNN size to largest RNN size):'
    hamming = []
    for sample in lstm_samples:
        hamming.append(hamming_distance(sample, chromosome))
    average = sum(hamming) / len(hamming)
    print ', '.join(map(str, hamming))
    print 'average hamming distance is ' + str(average)
    print 'percentage of mismatches is ' + str(float(average)/float(len(chromosome))*100) + '%'
    print ''

    # Samples of GRU
    gru_samples = []
    path=samples_path + '/GRU/chr-%02d/'%chromosome_number
    s_128_2 = [f for f in os.listdir(path + '/128-2/')]
    for sample_file in s_128_2:
        path=samples_path + '/GRU/chr-%02d/'%chromosome_number + '/128-2/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            gru_samples.append(sample)
    path=samples_path + '/GRU/chr-%02d/'%chromosome_number
    s_256_3 = [f for f in os.listdir(path + '/256-3/')]
    for sample_file in s_256_3:
        path=samples_path + '/GRU/chr-%02d/'%chromosome_number + '/256-3/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            gru_samples.append(sample)
    path=samples_path + '/GRU/chr-%02d/'%chromosome_number
    s_512_4 = [f for f in os.listdir(path + '/512-4/')]
    for sample_file in s_512_4:
        path=samples_path + '/GRU/chr-%02d/'%chromosome_number + '/512-4/' + sample_file
        with open(path, 'r') as f:
            sample = f.readline()
            sample = sample.replace(' ', '')
            gru_samples.append(sample)

    print 'Hamming Distance in GRU Samples (from smallest RNN size to largest RNN size):'
    hamming = []
    for sample in gru_samples:
        hamming.append(hamming_distance(sample, chromosome))
    average = sum(hamming) / len(hamming)
    print ', '.join(map(str, hamming))
    print 'average hamming distance is ' + str(average)
    print 'percentage of mismatches is ' + str(float(average)/float(len(chromosome))*100) + '%'
    print ''
    print ''