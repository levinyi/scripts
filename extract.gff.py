import sys
import os
import argparse
import re
import gzip
from Bio import SeqIO


def _argparse():
    parser = argparse.ArgumentParser(description='This is description')
    parser.add_argument('-g', '--gff', action='store', dest='gff', help='help info')
    parser.add_argument('-f', '--fasta', action='store', dest='fasta', help='help info')
    return parser.parse_args()


class GFF(object):
    """docstring for GFF"""
    # gff file have 9 split region

    def __init__(self, seq_id, source, types, start, ends, core, strand, phase, attributes):
        self.seq_id = seq_id
        self.source = source
        self.types = types
        self.start = start
        self.ends = ends
        self.core = core
        self.strand = strand
        self.phase = phase
        self.attributes = attributes

    def get_attr_name(self):
        p = re.compile(r'.*gene_id=([\w*\.?]+);.*?gene_type=(\w*?);gene_name=([\w*\.?\-?\/?\(?\)?]+);.*?')
        # result = p.findall(self.attributes)
        result = p.match(self.attributes)
        # print result
        if result:
            # print result.groups()
            gene_id, gene_type, gene_name = result.groups()
        else:
            print self.attributes
            # sys.exit(self.attributes)
        if len(result.groups()) == 2:
            print result
        # print(gene_id, gene_type, gene_name)
        return gene_id, gene_type, gene_name

    def print_all_feature(self):
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.seq_id, self.source, self.types, self.start, self.ends, self.core, self.strand, self.phase, self.attributes))


def two_dimension_dict(dict_name, key_1, key_2, value):
    ''' key,value is a dict: d={a1:{b1:c1,d1:e1},a2:{b2:c2,d2:e2}}'''
    if key_1 in dict_name:
        dict_name[key_1].setdefault(key_2, value)
    else:
        dict_name.update({key_1: {key_2: value}})
    return dict_name


def addtwodimdict(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict '''
    if key_a in thedict:
        thedict[key_a].setdefault(key_b, []).append(val)
    else:
        thedict.update({key_a: {key_b: [val]}})
    return thedict


def deal_fasta(fasta):
    fasta_dict = {}
    if fasta.endswith(".gz"):
        header = gzip.open(fasta, "r")
    else:
        header = open(fasta, "r")
    for record in SeqIO.parse(header, "fasta"):
        fasta_dict[record.id] = record.seq
    return fasta_dict


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


def trim_fasta(fasta_dict, chrm, start, end, strand):
    # vdict is like : {TRGV11 {'seq_id': 'chr7', 'five_prime_UTR': '38291925_38292078', 'exon': ['38291616_38292078'], 'CDS': ['38291616_38291924'], 'gene': '38291616_38292078', 'strand': '-'}}

    if strand == '-':
        newseq = DNA_reverse(DNA_complement(str(fasta_dict[chrm][start-1: end])))
    else:
        newseq = fasta_dict[chrm][start-1: end]
    return newseq


def main():
    parser = _argparse()
    # deal fasta file
    fasta_dict = deal_fasta(parser.fasta)
    print "finished deal fasta, stored as a dict."

    # deal gff file
    if parser.gff.endswith(".gz"):
        header = gzip.open(parser.gff, "r")
    else:
        header = open(parser.gff, "r")

    gff_list = []
    for line in header:
        line = line.rstrip("\n")
        if line.startswith("#"):
            continue
        a, b, c, d, e, f, g, h, j = line.split("\t")

        aninstance = GFF(a, b, c, d, e, f, g, h, j)
        gff_list.append(aninstance)
    header.close()
    print "finished deal gff, stored as a list of object."

    # deal gff list. stored to the dict.
    gene_dict = {}
    for gff_line in gff_list:
        # print gff_line.get_attr_name()
        gene_id, gene_type, gene_name = gff_line.get_attr_name()
        # print gene_type, gene_name
        if gene_type == 'TR_V_gene':
            two_dimension_dict(gene_dict, gene_id, 'gene_name', gene_name)
            two_dimension_dict(gene_dict, gene_id, 'seq_id', gff_line.seq_id)
            two_dimension_dict(gene_dict, gene_id, 'strand', gff_line.strand)

            if gff_line.types == 'gene':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_id, 'gene', region)
            elif gff_line.types == 'exon':
                region = '_'.join([gff_line.start, gff_line.ends])
                addtwodimdict(gene_dict, gene_id, 'exon', region)
            elif gff_line.types == 'CDS':
                region = '_'.join([gff_line.start, gff_line.ends])
                addtwodimdict(gene_dict, gene_id, "CDS", region)
            elif gff_line.types == 'start_codon':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_id, "start_codon", region)
            elif gff_line.types == 'five_prime_UTR':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_id, "five_prime_UTR", region)

            # print gene_type, gene_name, gff_line.print_all_feature()
    print "convert gff object to a dict"

    #  get result
    print "start print result"
    with open("TRV_gene.fa","w") as f1, open("TRV_UTR.fa","w") as f2:
        for k, v in gene_dict.items():
            # print k, v
            if 'gene' in v.keys():
                start, end = v['gene'].split("_")
                gene_seq = trim_fasta(fasta_dict, v['seq_id'], int(start), int(end), v['strand'])
                f1.write(">%s %s %s %s %s %s\n%s\n" % (v['gene_name'], v['seq_id'], k, start, end, v['strand'], gene_seq))
                # verified.
            if 'start_codon' in v.keys():
                start, end = v['start_codon'].split("_") # codon is :142308589-142308591 but utr is:142308542-142308588
                # start_codon_seq = trim_fasta(fasta_dict, v['seq_id'], int(start), int(end),v['strand'])
                if v['strand'] == "+":
                    start, end = int(start) - 201, int(start)-1
                else:
                    # print("start_codon:%s"%(start_codon_seq))
                    # codon is :38349822-38349824 but utr is 38349825-38350022
                    start, end = int(end)+1, int(end) + 201
                UTR_seq = trim_fasta(fasta_dict, v['seq_id'], int(start), int(end), v['strand'])
                f2.write(">%s %s %s utr %s %s %s\n%s\n" % (v['gene_name'], v['seq_id'], k, start, end, v['strand'], UTR_seq))
            elif 'five_prime_UTR' in v.keys():
                start, end = v['five_prime_UTR'].split("_")
                if v['strand'] == "+":
                    # utr is: 142308542-142308588
                    start,end = int(end) - 200, int(end)
                else:
                    # utr is 38349825-38350022
                    start, end = int(start),int(start) + 200
                UTR_seq = trim_fasta(fasta_dict, v['seq_id'], int(start), int(end), v['strand'])
                f2.write(">%s %s %s utr %s %s %s\n%s\n" % (v['gene_name'], v['seq_id'], k, start, end, v['strand'], UTR_seq))
    # print len(gene_dict)

if __name__ == '__main__':
    main()
