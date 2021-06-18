import sys
from Bio import SeqIO
import gzip


fastq_file = gzip.open(sys.argv[1], "r")
name = sys.argv[2]
R = sys.argv[3]

with gzip.open(name+"_S1_L002_" + R + "_001.fastq.gz", "w") as output_handle:
    for record in SeqIO.parse(fastq_file, "fastq"):
        record.id = str(record.id).replace("/"," ")
        SeqIO.write(record, output_handle, "fastq")

