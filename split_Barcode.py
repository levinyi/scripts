import sys
from Bio import SeqIO
import gzip
#python split_barcode.py barcode.list xxx.fastq -f 9 -l 28 -e 2

header = gzip.open("/cygene/work/10.ANCCR180494_PM-CR180494-05_2018-12-31/RP1G10E1L2_R1.fq.gz")
tso =0
for record in SeqIO.parse(header,"fastq"):
    read = str(record.seq)
    #if read[8:36] == 'GCAGTGGTATCAACGCAGAGTACATGGG' :
    #    tso += 1
    #else:
    #    print read[8:36]
    print read[8:34]
header.close()
