import sys
import os
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description='This is description')
    parser.add_argument('-f', '--gff', action='store', dest='gff', help='help info')
    parser.add_argument('-r', '--fasta', action='store', dest='fasta', help='help info')


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

    def attributes(self.attributes):
        attr = self.attributes.split("\t")
        for each in attr:
            ID = 
            gene_id = 
            gene_type = 

def main():
    parser = _argparse()
    if not parser.gff or not parser.fasta:
        sys.exit("no input file")
    gff_list = []
    with open(parser.gff,"r") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("#"):
                pass

            aninstance = GFF(line.split("\t"))
            gff_list.append(aninstance)
    for each in gff_list:
        print each.attributes()
if __name__ == '__main__':
    main()
