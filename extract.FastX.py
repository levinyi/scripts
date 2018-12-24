import sys
from Bio import SeqIO
import argparse
import gzip

def _argparse():
    pass

if sys.argv[1].endswith(".gz"):
    header = gzip.open(sys.argv[1],"r")
else:
    header = open(sys.argv[1],"r")
if sys.argv[1].replace(".gz","").endswith("fa"):
    types = "fasta"
else:
    types = "fastq"

chrome = sys.argv[2]
start = int(sys.argv[3])
ends = int(sys.argv[4])
for record in SeqIO.parse(header,types):
    if record.id == chrome:
        print record.seq[start:ends]
