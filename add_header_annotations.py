# Code originally from http://crazyhottommy.blogspot.com.au/2014/07/use-python-to-change-header-of-fasta.html, 
# accessed & modified 18th Sept 2017 & 5th June 2018
# original author: Tommy Tang
# modified by: Kate Wathen-Dunn

#    The 'annotationList.txt' file is a single-column csv table containing the contig name (contig-#, no spaces in name) and the matching 
#    best blast description from  hits to the NCBI nr database. Blast annotation may contain spaces. 
#    Contig name and blast annotation were in the same cell, separated by a space, and with quotation marks removed.
#    This script will not overwrite/add headers that are not in the annotationList, so can be used to add annotations progressively 
#    with new annotationList files if required.

# Execute by: python add_header_annotations.py annotationList input-fastafile output-fastafile

import sys


with open(sys.argv[1], "rU") as annotFile:
    annotation_dict = {}
    for line in annotFile:
        line = line.split()
        if line:           #test whether it is an empty line
            annotation_dict[line[0]]=line[1:]
        else:
            continue

outfile = open(sys.argv[3], "w")

with open (sys.argv[2], "rU") as myfasta:
    for line in myfasta:
        if line.startswith (">"):
            line = line[1:] # skip the ">" character
            linesplit = line.split()
            if linesplit[0] in annotation_dict:
                new_line = ">" + str(linesplit[0]) + " " + " ".join(annotation_dict[linesplit[0]])
                outfile.write(new_line + "\n")
            else:
                outfile.write(">" + str(line) + "\n")
        else:
            outfile.write(line)

outfile.close()             # close the file
