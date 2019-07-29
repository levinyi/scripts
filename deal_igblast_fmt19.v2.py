import sys
import re
'''
update:
    15-03-2019: if two genes in one read, print two genes separatly. see line 59.

'''

def rm_dup_gene(gene):
    p = re.compile(r'\*\d+')
    genes = gene.split(",")
    new_list = []
    for each in genes:
        new = re.sub(p, "", each)
        new = new.replace("/","_")
        new_list.append(new)

    new_list = list(set(new_list))
    return new_list

igblast_file = sys.argv[1]
flag = str(sys.argv[2])
flag_dict = {
    'TRA': 'TRB',
    'TRB': 'TRA'
}

no_flag_error = 0
AB_error = 0
two_gene = 0
correct =0
mismatch =0
total_read = 0
with open(igblast_file, "r") as f, open(sys.argv[3],"w") as output_handle :
    for line in f:
        total_read +=1
        line = line.rstrip("\n")
        blast_out = line.split("\t")
        if blast_out[0].startswith("reversed"):
            read_id = blast_out[0].replace("reversed|", "")
            uniq_gene_list = rm_dup_gene(blast_out[7])
            if len(uniq_gene_list) == 1:
                if flag in uniq_gene_list[0]:
                    correct +=1
                    output_handle.write("%s\t%s\n" % (read_id, uniq_gene_list[0]))
                else:
                    no_flag_error += 1
                    # print read_id,"no_flag_error"
            else:
                if flag not in "_".join(uniq_gene_list):
                    no_flag_error += 1
                    # print read_id, "no_flag_error"
                elif flag in "_".join(uniq_gene_list) and flag_dict[flag] in "_".join(uniq_gene_list):
                    AB_error += 1
                    # print uniq_gene_list, "AB_error"
                else:
                    two_gene += 1
                    for each in uniq_gene_list:
                        output_handle.write("%s\t%s\n" % (read_id, each))
                    # print read_id, uniq_gene_list
        else:
            mismatch +=1
print "correct:%s\n no_flag_error:%s\n AB_error:%s\n two_gene:%s\n mismatch:%s\ntotal_read:%s\n"%(correct,no_flag_error,AB_error,two_gene,mismatch,total_read)
