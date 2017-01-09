#! /usr/bin python

# Code from Cara Magnabosco's blog at https://caramagnabosco.wordpress.com/
# accessed in August 2016. Thanks Cara!

# Code allows you to keep the contigs from a fasta file that are above a designated size, and filter out all those
# that are smaller.

# Execute with: python length_filter.py length2filter inputfile outputfile

# where length2filter = n (whatever number you want as min contig size)

import sys          		#module allows you to designate arguments in command line
from Bio import SeqIO 		#module allows you to easily read and write fasta files

n = int(float(sys.argv[1]))      #sys.argv[1] = n, converted to an int
input = open(sys.argv[2], 'rU')  #sys.argv[2] = input file
out = open(sys.argv[3], 'w')     #sys.argv[3] = output file

for record in SeqIO.parse(input, 'fasta'):
    sequence = record.seq
    if len(sequence)>n:
        SeqIO.write(record, out, 'fasta')

input.close()
out.close()
