import sys
import os
import argparse
import re


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
        p = re.compile(r'.*?gene_type=(\w*?);gene_name=([\w*\.?\-?\/?]+);.*?')
        # result = p.findall(self.attributes)
        result = p.match(self.attributes)
        if result:
            gene_type, gene_name = result.groups()
        return gene_type, gene_name

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
        thedict[key_a].setdefault(key_b,[]).append(val)
    else:
        thedict.update({key_a:{key_b:[val]}})
    return thedict

class GeneStruture(object):
    """docstring for GeneStruture"""

    def __init__(self, gene_name, seq_id, five_prime_UTR, CDS, intron, exon, start_code):
        self.gene_name = gene_name
        self.seq_id = seq_id
        self.five_prime_UTR = five_prime_UTR
        self.CDS = CDS
        self.intron = intron
        self.exon = exon
        self.start_code = start_code


def main():
    parser = _argparse()

    if parser.gff.endswith(".gz"):
        import gzip
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

    gene_dict = {}
    for gff_line in gff_list:
        gene_type, gene_name = gff_line.get_attr_name()
        # print gene_type, gene_name
        if gene_type == 'TR_V_gene':
            two_dimension_dict(gene_dict, gene_name, 'seq_id', gff_line.seq_id)
            two_dimension_dict(gene_dict, gene_name, 'strand', gff_line.strand)

            if gff_line.types == 'gene':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_name, 'gene', region)
            elif gff_line.types == 'exon':
                region = '_'.join([gff_line.start, gff_line.ends])
                addtwodimdict(gene_dict, gene_name, 'exon', region)
            elif gff_line.types == 'CDS':
                region = '_'.join([gff_line.start, gff_line.ends])
                addtwodimdict(gene_dict, gene_name, "CDS", region)
            elif gff_line.types == 'start_codon':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_name, "start_codon", region)
            elif gff_line.types == 'five_prime_UTR':
                region = '_'.join([gff_line.start, gff_line.ends])
                two_dimension_dict(gene_dict, gene_name, "five_prime_UTR", region)

            # print gene_type, gene_name, gff_line.print_all_feature()

    gene_structure_list = []
    for k, v in gene_dict.items():
        # print k, v
        # if 'five_prime_UTR' not in v.keys():
        #     print k,v 
        if 'start_codon' not in v.keys():
            print k,v

        # aninstance = GeneStruture(seqid, five_prime_UTR, cds, intron, gene_type, gene_name)
        # gene_structure_list.append(aninstance)

        #     print "yes"
        # print(gene_type,gene_name)
        # each.print_all_feature()


if __name__ == '__main__':
    main()
