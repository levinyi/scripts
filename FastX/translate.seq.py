import sys
from Bio import SeqIO
from Bio.Seq import Seq

seq = sys.argv[1]
aa = Seq(seq).translate()
print(aa)
