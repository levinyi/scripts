import sys

input_blast_file = sys.argv[1]
with open(input_blast_file,"r") as f:
    for line in f:
        if line.startswith("Contig"):
            match = line.split()
            print "%s\t%s\t%s\t%s"%(match[1],match[8],match[9],match[0])
