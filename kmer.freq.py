import sys

kmer_length = int(sys.argv[1])

kmer_list = []
cdr3_list = []
with open("71.CDR3.id", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        cdr3_list.append(line)
        for i in range(len(line)):
            kmer = line[i:kmer_length + i]
            if len(kmer) == kmer_length:
                kmer_list.append(kmer)
                '''
                if kmer not in kmer_dict:
                    kmer_dict[kmer] = 1
                else:
                    kmer_dict[kmer] = kmer_dict[kmer] + 1
                '''
                
new_kmer_list= list(set(kmer_list))

print "\t","\t".join(new_kmer_list)
for i in range(len(cdr3_list)):
    print cdr3_list[i],"\t",
    for j in range(len(new_kmer_list)):
        if new_kmer_list[j] in cdr3_list[i]:
            print 1,"\t",
        else:
            print 0,"\t",
    print ""

