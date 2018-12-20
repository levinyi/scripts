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

    for each in gff_list:
        gene_type, gene_name = each.get_attr_name()
        # print gene_type, gene_name
        if gene_type == 'TR_V_gene':
            print gene_type, gene_name
            each.print_all_feature()
        #     print "yes"
        # print(gene_type,gene_name)
        # each.print_all_feature()


if __name__ == '__main__':
    main()
