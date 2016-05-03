from Bio import SeqIO
import os

'''
2. Find approximate occurrences of "likely" and "dubious" replication of origins in the resulting samples
'''

def occurences(origin, chromosome, distance):
    count = 0
    for i in range(0, len(chromosome) - len(origin)):
        if hamming_distance(origin, chromosome[i:i+len(origin)]) <= distance:
            count += 1
    return count

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

data_path = 'Saccharomyces-Cerevisiae'
preprocessed_data_path = 'Preprocessed'
samples_path = 'Samples'
chromosomes = ["dummy"]     # just include a dummy value at location 0
replication_origins = {}


for chromosome_number in range(1, 2):
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

    likely_origins_file = data_path + '/chr%02d'%chromosome_number + '-likely.fsa'
    dubious_origins_file = data_path + '/chr%02d'%chromosome_number + '-dubious.fsa'

    fasta_sequences = SeqIO.parse(open(likely_origins_file),'fasta')
    for fasta in fasta_sequences:
        name, origin = fasta.id, str(fasta.seq)

        d = len(origin) / 2     # try to find an origin with at most half of its length mismatched
        # test against RNN
        number_of_candidates = 0
        i = 1
        for sample in rnn_samples:
            print 'RNN sample ' + str(i) + ' is now being tested ..'
            i += 1
            number_of_candidates += occurences(origin, sample, d)
        print 'The likely origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of RNN'

        # test against LSTM
        number_of_candidates = 0
        i = 1
        for sample in lstm_samples:
            print 'LSTM sample ' + str(i) + ' is now being tested ..'
            i += 1
            number_of_candidates += occurences(origin, sample, d)
        print 'The likely origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of LSTM'

        # test against GRU
        number_of_candidates = 0
        i = 1
        for sample in gru_samples:
            print 'GRU sample ' + str(i) + ' is now being tested ..'
            i += 1
            number_of_candidates += occurences(origin, sample, d)
        print 'The likely origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of GRU'
        print ''

    print ''
    fasta_sequences = SeqIO.parse(open(dubious_origins_file),'fasta')
    for fasta in fasta_sequences:
        name, origin = fasta.id, str(fasta.seq)

        d = len(origin) / 2     # try to find an origin with at most half of its length mismatched
        # test against RNN
        number_of_candidates = 0
        for sample in rnn_samples:
            number_of_candidates += occurences(origin, sample, d)
        print 'The dubious origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of RNN'

        # test against LSTM
        number_of_candidates = 0
        for sample in lstm_samples:
            number_of_candidates += occurences(origin, sample, d)
        print 'The dubious origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of LSTM'

        # test against GRU
        number_of_candidates = 0
        for sample in gru_samples:
            number_of_candidates += occurences(origin, sample, d)
        print 'The dubious origin ' + name + ' has found ' + str(number_of_candidates) + ' occurences with ' + str(d) + ' mismatches in the samples of GRU'