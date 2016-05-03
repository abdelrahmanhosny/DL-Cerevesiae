from Bio import SeqIO
import numpy as np
import re


# WILL HAVE TO UPDATE THIS PATH TO THE CHROMOSOME FILE IN ORDER TO RUN
# FUTURE PLANS INCLUDE SETTING UP A SCRIPT SIMILAR TO WHAT IS DONE ON THE DISCRIMINATE SIDE
# THIS SCRIPT WILL LOOP THOUGH ALL CHROMOSOME FILES
chromosome_file = '/Users/anthonyparziale/Development/DNA/chr01.fsa'
confirmed_origins = '/Users/anthonyparziale/Development/DNA/chr01-confirmed.fsa'


def char_to_number(ch):
    if ch == 'A':
        return -1
    elif ch == 'C':
        return -2
    elif ch == 'G':
        return -3
    elif ch == 'T':
        return -4
    elif ch == 'a':
        return 1
    elif ch == 'c':
        return 2
    elif ch == 'g':
        return 3
    elif ch == 't':
        return 4

def char_to_label(value):
    if value < 0:
        return 0
    else:
        return 1


def importData():
    input_matrix = []
    labels = []

    fasta_sequences = SeqIO.parse(open(chromosome_file),'fasta')
    chrLength = 0
    for fasta in fasta_sequences:
        name, cerevisie_chromosome = fasta.id, str(fasta.seq)
        chrLength = len(cerevisie_chromosome)
        

    fasta_sequences = SeqIO.parse(open(confirmed_origins),'fasta')
    for fasta in fasta_sequences:
        name, descrip, replication_origin = fasta.id, fasta.description, str(fasta.seq)
          
        m = re.search('range=(.+?) ', descrip)
        if m:
            start = int(m.group(1)[m.group(1).index(':')+1 : m.group(1).index('-')])
            end = int(m.group(1)[m.group(1).index('-')+1:])

        beginning = np.zeros(start)
        ending = np.zeros(chrLength - end)
        
        site = np.array(map(char_to_number, replication_origin))

        
        inputData = np.hstack((beginning,site))
        inputData = np.hstack((inputData,ending))
        
        input_matrix.append(inputData)
         
        #print inputData

    
    return input_matrix