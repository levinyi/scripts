from Bio.SeqIO.QualityIO import FastqGeneralIterator
import sys
import gzip


def DNA_complement(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace('A', 't')
    sequence = sequence.replace('T', 'a')
    sequence = sequence.replace('C', 'g')
    sequence = sequence.replace('G', 'c')
    return sequence.upper()


def DNA_reverse(sequence):
    sequence = sequence.upper()
    return sequence[::-1]

input_file = sys.argv[1]
output_file = sys.argv[2]

if input_file.endswith(".gz"):
    input_header = gzip.open(input_file, "r")
else:
    input_header = open(input_file, "r")

if output_file.endswith(".gz"):
    output_header = gzip.open(output_file, "w")
else:
    output_header = open(output_file, "w")

try:
    for title, seq, qual in FastqGeneralIterator(input_header):
        #output_header.write("@%s\n%s\n+\n%s\n" % (title, DNA_reverse(DNA_complement(seq)), DNA_reverse(qual))) # old fashion.
        outpur_header.write('@{0}\n{1}\n+{2}\n'.format(title, DNA_reverse(DNA_complement(seq)), DNA_reverse(qual)))
finally:
    input_header.close()
    output_header.close()
