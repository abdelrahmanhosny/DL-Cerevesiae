from Bio import SeqIO
import os

'''
This file prepares the data to serve as input to the RNN/GRU/LSTM models
In these models. we have a vocabulary of 8 characters:
a, c, g, t -> are for the genome sequence
A, C, G, T -> are for the origin of replication
We separate the whole string characters with spaces to treat each character as a standalone word
The models are designed to capture the long-term dependencies between these sequences of characters
'''

data_path = 'Saccharomyces-Cerevisiae'
preprocessed_data_path = 'Preprocessed'

chromosomes = ["dummy"]     # just include a dummy value at location 0
replication_origins = {}

for chromosome_number in range(1, 17):
    chromosome = data_path + '/chr%02d.fsa'%chromosome_number
    confirmed_origins = data_path + '/chr%02d-confirmed.fsa'%chromosome_number

    fasta_sequences = SeqIO.parse(open(chromosome),'fasta')
    for fasta in fasta_sequences:
        name, cerevisiae_chromosome = fasta.id, str(fasta.seq)
    chromosomes.append(cerevisiae_chromosome)
    replication_origins[chromosome_number] = []


    fasta_sequences = SeqIO.parse(open(confirmed_origins),'fasta')
    for fasta in fasta_sequences:
        name, description, replication_origin = fasta.id, fasta.description, str(fasta.seq)
        replication_origins[chromosome_number].append(replication_origin)

# now we have all chromosomes loaded and their replication origins
# prepared the input to be fed into the models
for i in range(1, 17):
    chromosome = chromosomes[i].lower()
    for oric in replication_origins[i]:
        chromosome = chromosome.replace(oric.lower(), oric.upper())
    input_file = os.path.join(preprocessed_data_path, 'chr%02d-input.text'%i)
    with open(input_file, 'w') as f:
        parsed_chromosome = ''
        for c in chromosome:
            parsed_chromosome += c + ' '
        parsed_chromosome = parsed_chromosome.strip()
        f.write(parsed_chromosome)