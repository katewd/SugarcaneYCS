#! /usr/bin python
# need to change the above line to suit the path to python on your system
#
# code originally from Eric Normandeau on www.biostars.org/p/1709/  accessed 23 May 2018
# modified by Kate Wathen-Dunn

# This script takes a list of read header names, from reads that need to be excluded from a
# multifasta reads file, and writes a new fasta file that only has the reads NOT on the reads list.  
# Reads list is one read header name per line, with no quotes, > symbols or other details.

# Execute by: python seq_clean.py readsList fastafile outputfile


from Bio import SeqIO
import sys


readsList = open(sys.argv[1], 'rU')
fastafile = sys.argv[2]
outputfile = open(sys.argv[3], 'w')

 
unwanted = set()
with readsList as f:
    for line in f:
        line = line.strip()
        if line != "":
            unwanted.add(line)
 
fasta_sequences = SeqIO.parse(open(fastafile),'fasta')

with outputfile as i:
    for seq in fasta_sequences:
        if seq.id not in unwanted:
            SeqIO.write([seq], i, "fasta")


readsList.close()
outputfile.close()
