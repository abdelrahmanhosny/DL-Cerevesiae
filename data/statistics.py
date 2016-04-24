from Bio import SeqIO
import numpy as np
import re

'''
For each chromosome, this file answers the following questions:
1. What is the length of the chromosome?
2. How many confirmed replication origins?
3. What is the length of each confirmed replication origin? Start? Finish?
4. What is the length of the whole genome?

'''
data_path = 'Saccharomyces-Cerevisiae'
genome_length = 0
stats = ''
for chromosome_number in range(1, 17):
    chromosome = data_path + '/chr%02d.fsa'%chromosome_number
    confirmed_origins = data_path + '/chr%02d-confirmed.fsa'%chromosome_number

    fasta_sequences = SeqIO.parse(open(chromosome),'fasta')
    for fasta in fasta_sequences:
        name, cerevisiae_chromosome = fasta.id, str(fasta.seq)
    subtitle = '## Chromosome ' + str(chromosome_number) + ' has ' + str(len(cerevisiae_chromosome)) + ' base pairs'
    details = ''
    genome_length += len(cerevisiae_chromosome)

    origins = 0
    origins_length = 0
    fasta_sequences = SeqIO.parse(open(confirmed_origins),'fasta')
    for fasta in fasta_sequences:
        name, description, replication_origin = fasta.id, fasta.description, str(fasta.seq)
        origins += 1
        origins_length += len(replication_origin)
        m = re.search('range=(.+?) ', description)
        if m:
            details += str(origins) + ". The confirmed replication origin **" + name + "** range is *" + m.group(1) + "*, with a length of **" + str(len(replication_origin)) + "** base pairs\n"

    subtitle += ", and " + str(origins) + " confirmed replication origins with an average length of " + str((origins_length/origins)) +  " base pairs\n"
    stats += subtitle + details + "\n\n"

title = "# Saccharomayces Ceravesiae genome length is " + str(genome_length) + "\n\n"

with open('README.md', 'w') as f:
    f.write(title)
    f.write(stats)
    print "Stats print to file successfully"