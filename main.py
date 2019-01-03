import sys
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="this is description")
    # parser.add_argument('-c', action='store', dest='config', help="config file")
    parser.add_argument('-fq1', action='store', dest='fastq1', help="fastq 1 file, read 1 file.")
    # parser.add_argument('-fq2', action='store', dest='fastq2', help="fastq 2 file, read 2 file.")
    parser.add_argument('-p', action='store', dest='prefix', help='prefix of out put name.')
    return parser.parse_args()


def do_step4():
    print("step4:statistic")
    print("/cygene/software/annocoda3/bin/Rscript heatmap.R")
    print("venn plot")


def main():
    """docstring for main"""
    parser = _argparse()
    # configfile = parser.config
    raw_fastq = parser.fastq1
    # fastq2 = parser.fastq2
    prefix = parser.prefix
    # print prefix,raw_fastq
    argument_dict = {'prefix': prefix, "raw_fastq": raw_fastq}
    print("# step1:cutadapt")
    print("cutadapt -g adapter=ATATCCAGAACCCTGACCCTGCGTACCAGCACAAGTTTGTACAAAAAAGCAGGCTACC -O 10 -o %(prefix)s.p1.fq -r %(prefix)s.p2.fq --info-file=%(prefix)s.cutadapt.log %(raw_fastq)s " % {'raw_fastq': raw_fastq, 'prefix': prefix})
    print("perl /home/xiaofan/separate_fq.pl %(prefix)s.cutadapt.log %(prefix)s" % argument_dict)
    # get b0005_1.p1.fq b0005_1.p2.fq

    print("# step2:igblastn")
    print("# fastq 2 fasta")
    print("seqkit fq2fa %(prefix)s.p1.fq >%(prefix)s.p1.fa" % argument_dict)
    print("seqkit fq2fa %(prefix)s.p2.fq >%(prefix)s.p2.fa" % argument_dict)
    print("igblastn -query %(prefix)s.p1.fa -out output.m19.out -outfmt 19 -germline_db_V ./database/human_TR_V -germline_db_J ./database/human_TR_J -germline_db_D ./database/human_TR_D -auxiliary_data ./optional_file/human_gl.aux -organism human -ig_seqtype TCR -show_translation -evalue 1e-10 -num_threads 20" % argument_dict)
    print("igblastn -query %(prefix)s.p1.fa -out output.m19.out -outfmt 19 -germline_db_V ./database/human_TR_V -germline_db_J ./database/human_TR_J -germline_db_D ./database/human_TR_D -auxiliary_data ./optional_file/human_gl.aux -organism human -ig_seqtype TCR -show_translation -evalue 1e-10 -num_threads 20" % argument_dict)

    print("# step3:mixcr")
    print("mixcr analyze shotgun --align \"-OsaveOriginalReads=true\" --species hs --starting-material rna --receptor-type tcr -r %(prefix)s.p1.report %(prefix)s.p1.fq %(prefix)s.p1.mixcr.out" % argument_dict)
    print("mixcr analyze shotgun --align \"-OsaveOriginalReads=true\" --species hs --starting-material rna --receptor-type tcr -r %(prefix)s.p2.report %(prefix)s.p2.fq %(prefix)s.p2.mixcr.out" % argument_dict)
    # return : .report .clna .txt
    print("mixcr exportReadsForClones -s %(prefix)s.p1.mixcr.out.clna %(prefix)s.p1." % argument_dict)
    print("mixcr exportReadsForClones -s %(prefix)s.p2.mixcr.out.clna %(prefix)s.p2." % argument_dict)
    print("mkdir -p %(prefix)s && mv %(prefix)s.*.fastq.gz %(prefix)s"% argument_dict)
    print("perl /home/xiaofan/tcr_pairing.pl %(prefix)s.p1 %(prefix)s.p2 %(prefix)s.pairing.info %(prefix)s.pairing.freq" % argument_dict)


if __name__ == '__main__':
    main()
