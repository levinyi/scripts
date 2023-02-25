import sys
import gzip
import re
sys.path.append("/cygene/script/python_packages")
import edit_distance
from Bio import SeqIO

primers = {}
with open(sys.argv[1], "r") as ff:
    for line in ff:
        line = line.rstrip("\n")
        id, primer = line.split()
        primers[id] = primer
print "finished deal primers, stored as dict."


def addtwodimdict(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict '''
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})
    return thedict
                      
_TRAC = 'ATATCCAGAACCCTGACTCCGGATCCGGA'
pattern = re.compile(r'ATATCCAGAACCCTGACCCTGCGTACCAGCACAAGTTTGTACAAAAAAGCAGGCTACC')

total_number = 0
ATG_number = 0
non_atg = 0
reads_info_dict = {}

header = gzip.open("b0005p1_S1_L001_R1_001.fastq.gz","r")
record_number = 0

middle_dict = {}
for record in SeqIO.parse(header,"fastq"):
    record_number +=1
    small_dict = {}
    m = pattern.search(str(record.seq))
    if m:
        newseq = str(record.seq)[m.span()[1]:]
        if newseq.startswith("ATG"):
            ATG_number += 1
            for primer_id, primer_seq, in primers.items():
                if len(primer_seq) <= newseq[:len(primer_seq)]:
                    distance = edit_distance.minEditDist(primer_seq, newseq[:len(primer_seq)])
                    # addtwodimdict(reads_info_dict,record.id,primer_id,distance)
                    addtwodimdict(small_dict,record.id,primer_id,distance)

        for read_id, read_dict in small_dict.items():
            for primer, distance in read_dict.items():
                if min(read_dict.values()) ==0:
                    if distance == min(read_dict.values()):
                        middle_dict[primer].update({'0',1})
                        print read_id, primer, distance, primers[primer], newseq
                if min(read_dict.values()) ==1:
                    if distance == min(read_dict.values()):
                        print read_id, primer, distance, primers[primer], newseq
                if min(read_dict.values()) ==2:
                    if distance == min(read_dict.values()):
                        print read_id, primer, distance, primers[primer], newseq
# print(total_number, ATG_number, non_atg)
# print reads_info_dict
# final_dict:
# other_structure
for read_id,read_dict in reads_info_dict.items():
    for primer, distance in read_dict.items():
        if distance == min(read_dict.values()):
            print primer, distance
        # if 0 in y:
            # pass
        # elif 1 in y:
        #     pass
        # elif 2 in y:
