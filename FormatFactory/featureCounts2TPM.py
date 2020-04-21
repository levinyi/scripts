''' these modules were used.'''
import os
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description = "A feature tpm.")
    parser.add_argument('-a', '--countsFile', action='store', dest='countsfile')
    parser.add_argument('-o', '--outfile', action='store',dest='outfile')
    # parser.add_argument('-g', '--gtfFile', action='store', dest='gtffile')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()    

def print_TPM(gene_ratio_dict, total_ratio, outfile):
    with open(outfile, "w") as f:
        for gene in gene_ratio_dict:
            TPM = (gene_ratio_dict[gene]*1000000) / float(total_ratio)
            f.write("{}\t{}\n".format(gene,TPM))

def main():
    ''' docstring for main'''
    parser = _argparse()
    countsfile = parser.countsfile
    outfile = parser.outfile

    gene_ratio_dict = {}
    total_ratio = 0
    with open(countsfile, "r") as f:
        for line in f:
            if line.startswith("#") or line.startswith("Geneid"):
                continue
            Geneid, Chr, Start, End, Strand, Length, Counts = line.rstrip("\n").split("\t")
            counts_ratio = int(Counts) / float(Length)
            total_ratio += counts_ratio
            gene_ratio_dict[Geneid] = counts_ratio

    print_TPM(gene_ratio_dict, total_ratio, outfile)

if __name__ == '__main__':
    main()

