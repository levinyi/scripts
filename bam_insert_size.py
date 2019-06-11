import pysam
import sys

bamfile = pysam.AlignmentFile(sys.argv[1],"rb")

for r in bamfile:
    print r.qname, r.flag, r.reference_name, r.pos, r.mapq, r.cigarstring, r.next_reference_id, r.seq, r.isize
