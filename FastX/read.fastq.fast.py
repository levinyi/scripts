"""  """
import sys
import datetime
import gzip
from Bio import SeqIO


def usage():
    """
    docstring for usage
    
    Try me:
        python read.fastq.fast.py /cyg/data/20190712_MG_G22_G23_G27_G28_G29_G30/G30E1L2_BKDL190819904-1a/G30E1L2_BKDL190819904-1a_1.fq.gz
    """
    
def print_current_time():
    """this is the module docstring """
    time_stamp = datetime.datetime.now()
    return time_stamp.strftime('%Y.%m.%d-%H:%M:%S')


print '{0} start'.format(print_current_time())
with gzip.open(sys.argv[1], "r") as inp:
    NUM_LINES = sum([1 for line in inp])
print NUM_LINES
print "%s finished" % print_current_time()

print "%s start" % print_current_time()
HEADER = gzip.open(sys.argv[1], "r")

try:
    NUM_LINES = sum([1 for each in SeqIO.parse(HEADER, "fastq")])
    print NUM_LINES
    print "%s start" % print_current_time()
finally:
    HEADER.close()
