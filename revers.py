import sys

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

#DNA="GGACAAAGCCTTGAGCAGCCCTCTGAAGTGACAGCTGTGGAAGGAGCCATTGTCCAGATAAACTGCACGTACCAGACATCTGGGTTTTATGGGCTGTCCTGGTACCAGCAACATGATGGCGGAGCACCCACATTTCTTTCTTACAATGCTCTGGATGGTTTGGAGGAGACAGGTCGTTTTTCTTCATTCCTTAGTCGCTCTGATAGTTATGGTTACCTCCTTCTACAGGAGCTCCAGATGAAAGACTCTGCCTCTTACTTCTGCGCTGTGAGAGA"
#DNA="GGATATAGGGCAGCACGGACAATCTGGTTCCGGGACCAAAGACAAAATTCTGACCATAGTTCCAACCACTCAGAGCACAGAAGTACACCGCTGAGTCTGACACTTGAACTGAGCCTTTCTCCAAGTGGAAAGAAGTGGTTTCTTTACGGTATGTGGCTTCAAAACCTTTGTTGCTTCCCTTGTCATCAGCCTTCGTGGCTCTCAGGAGGAGCTGTAGACCTTCTCCAGGATATTGGACATACCAGAAAAGGGAAGGGTATCCTGTGGCTGTGTACGTGCAGTTTATAGTCAGGAAGGCCTCTTCTGATAGAGTCACTGTCCCTTCCATCTGGTTCACTGAATTTCCACGGTTTCTTCCAAGCAGTAAGAGTAGCAGAGATACTAAGCCTGGCGACTAGTT"
DNA = sys.argv[1]
print DNA_reverse(DNA)
print DNA_reverse(DNA_complement(DNA))
