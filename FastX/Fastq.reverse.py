import sys
from Bio import SeqIO

fq_file = sys.argv[1]
#out_file = sys.argv[2]

header = open(fq_file,"r")
for record in SeqIO.parse(header,"fastq"):
#    print record.seq
    seq = record.seq.reverse_complement()
    print seq
