import sys
import os 
import pandas as pd
import argparse
import json

def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('-f', '--geneid', action='store', dest='geneid_file', default='geneid_file.txt', help="this is gene id file(table format)")
    parser.add_argument('-s', '--species', action='store', dest="tax_id", default='9606', help="tax id")
    parser.add_argument('-a', '--fromType', action='store', dest="fromType", default="Ensembl", help="ENSEMBL,ENSEMBLTRANS,SYMBOL, ENTREZID,")
    parser.add_argument('-t', '--toType', action='store', dest="toType", default="Ensembl_gene_identifier",help="tax_id;GeneID;Ensembl_gene_identifier;RNA_nucleotide_accession.version;Ensembl_rna_identifier;protein_accession.version;Ensembl_protein_identifier")
    return parser.parse_args()

def main():
    parser = _argparse()
    species = parser.tax_id
    fromType = parser.fromType
    toType = parser.toType
    
    #database = pd.read_table("/cygene/database/gene2ensembl/gene2ensembl.9606.txt", sep="\t")
    database = "/cygene/database/gene2ensembl/gene2ensembl.9606.txt"
    db_dict = {}
    with open(database, "r") as db:
        for line in db:
            line = line.rstrip("\n")
            tax_id, GeneID, Ensembl_gene_identifier, RNA_nucleotide_accession, Ensembl_rna_identifier, protein_accession, Ensembl_protein_identifier = line.split()
            if species == tax_id:
                '''
                if fromType == "ENSEMBL":
                    if Ensembl_gene_identifier in db_dict:
                        if GeneID not in db_dict[Ensembl_gene_identifier]:
                            db_dict.setdefault(Ensembl_gene_identifier,[]).append(GeneID)
                    else:
                        db_dict.setdefault(Ensembl_gene_identifier, []).append(GeneID)
                '''
                if fromType == "ENSEMBLTRANS":
                    if Ensembl_rna_identifier == "-":
                        continue
                    db_dict[Ensembl_rna_identifier] = GeneID
    #for each in db_dict:
        # print(each, db_dict[each])
    id2symbol_dict = {}
    with open("/cygene/database/gene2ensembl/test.9606.gene_info.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            c = line.split()
            if c[0] == species:
                id2symbol_dict[c[1]] = c[2]
    
    input_file = parser.geneid_file
    geneid_dict = {}
    with open(input_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            c = line.split()
            # geneid = c[0].split(".")[0]
            geneid = c[0]
            if geneid in db_dict:
                print("{}\t{}\t{}".format(geneid, id2symbol_dict.get(db_dict[geneid], "NA"),c[1] ))
            else:
                print("{}\t{}\t{}".format(geneid, "NA", c[1]))

    

if __name__ == '__main__':
    main()
