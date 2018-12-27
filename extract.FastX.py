import os
import sys
from Bio import SeqIO
import argparse
import gzip
'''https://www.jianshu.com/p/22051fc6e0a3'''

def deal_fastq(fastq, id_list, file_true):
    for record in SeqIO.parse(fastq, "fastq"):
        if record.id in id_list:
            if file_true == True:
                SeqIO.write(record, "extract.id.fastq", "fastq")
            elif file_true == False:
                SeqIO.write(record, sys.stdout, "fastq")


def deal_fasta(fasta, chrome, flag, start=0, end=0):
    for record in SeqIO.parse(fasta, "fasta"):
        if record.id == chrome and flag == 'Ture':
            print record.seq[start - 1: end]  # start include; ends exclude
        elif record.id == chrome and flag == 'False':
            print record.seq

# check file header.
if sys.argv[1].endswith(".gz"):
    header = gzip.open(sys.argv[1], "r")
else:
    header = open(sys.argv[1], "r")

# input is fasta format.
if sys.argv[1].replace(".gz", "").endswith("fa") or sys.argv[1].replace(".gz", "").endswith("fasta"):
    # extract specific region sequence.
    if len(sys.argv) == 5:
        flag = 'Ture'
        chrome = sys.argv[2]
        starts = int(sys.argv[3])
        ends = int(sys.argv[4])
        deal_fasta(header, chrome, flag, starts, ends)
    # extract whole chrome sequence.
    elif len(sys.argv) == 3:
        flag = 'False'
        chrome = sys.argv[2]
        deal_fasta(header, chrome,flag)
    # argument error
    else:
        sys.exit("error with input format. see example.")

# input is fastq format
elif sys.argv[1].replace(".gz", "").endswith("fq") or sys.argv[1].replace(".gz", "").endswith("fastq"):
    # read id is a file
    if os.path.isfile(sys.argv[2]) :
        id_list = [line.rstrip("\n") for line in open(sys.argv[2], "r")]
        file_true = True
    # specific read id
    else:
        id_list = []
        id_list.append(sys.argv[2])
        file_true = False
    deal_fastq(header, id_list, file_true)

# input format error. do not support other format file.
else:
    sys.exit("please check your input file types: fastq or fasta ?")

