import sys
import os 
import pandas as pd
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('-f', '--geneid', action='store', dest='geneid_file', default='geneid_file.txt', help="this is gene id file(table format)")
    parser.add_argument('-s', '--species', action='store', dest="tax_id", default='9606', help="tax id")
    parser.add_argument('-d', '--destId', action='store', dest="destId", default="Ensembl_gene_identifier",help="tax_id;GeneID;Ensembl_gene_identifier;RNA_nucleotide_accession.version;Ensembl_rna_identifier;protein_accession.version;Ensembl_protein_identifier")
    return parser.parse_args()

def main():
    parser = _argparse()
    
    database = pd.read_table("/cygene/database/gencode/Gencode_human/release_19/gene2ensembl", sep="\t")

    input_file = parser.geneid_file
    tax_id = parser.tax_id
    geneid_file = pd.read_table(input_file, sep="\t")
    for index, row in iterrows():
        if row[0] in database[,"Ensembl_gene_identifier"]:
            print(database)

if __name__ == '__main__':
    main()
