import sys
from Bio import SeqIO

fasta = input("input your fasta file: ")
a = 0
for record in SeqIO.parse(fasta,"fasta"):
    name = record.id
    a +=1
    with open(name+".txt", "w") as f:
        f.write(">{}\n{}\n".format(name,record.seq))
print("total {} files are splited".format(a))
