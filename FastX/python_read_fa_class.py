import sys


class Fasta:
    def __init__(self, name, seq):
        """docstring for """
        self.name = name
        self.seq = seq
    
    def str(self):
        """docstring for str"""
        return str(self)
        

fastafile = sys.argv[1]
seq = {}
fasta_record = []
with open(fastafile, "r") as f:
    for line in f:
        line = line.rstrip("\n")
        if line.startswith(">"):
            name = line
            seq[name] = ''
            flag = 1
        else:
            seq[name] = seq[name] + line
            flag = 0

        if flag == 1:
            aninstance = Fasta(name, seq)
            fasta_record.append(aninstance)

for record in fasta_record:
    print(">{}\n{}".format(record.name, record.seq))
