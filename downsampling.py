import sys
import os
import gzip
from Bio import SeqIO
import random
import datetime
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('-r1', '--rd1', action='store', dest='read1', required=True, help="input read1 file")
    parser.add_argument('-r2', '--rd2', action='store', dest='read2', help="input read2 file")
    parser.add_argument('-p',  '--prefix', action='store', dest='prefix', required=True, help="this is the output file prefix that you had to give.")
    parser.add_argument('-s',  '--special', action='store', dest='spec_value', type=int, help="Specialized a int number to present the percentage you want, like [10] or [46] etc. which means 10% or 46%.")

    parser.add_argument('-v',  '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def print_current_time():
    time_stamp = datetime.datetime.now()
    return time_stamp.strftime('%Y.%m.%d-%H:%M:%S')


def addtwodimdict(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict '''
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a: {key_b: val}})
    return thedict


def main():
    '''docstring for main '''
    parser = _argparse()

    file1 = gzip.open(parser.read1, "r")
    prefix = parser.prefix

    print("%s Reading R1" % print_current_time())

    adict = {}
    read_list = []
    for record in SeqIO.parse(file1, "fastq"):
        adict[record.id] = record
        read_list.append(record.id)
    file1.close()

    if parser.read2:
        # print_current_time()
        print("%s Reading R2\n" % print_current_time())

        bdict = {}
        file2 = gzip.open(parser.read2, "r")
        for record in SeqIO.parse(file2, "fastq"):
            bdict[record.id] = record
        file2.close()

    total_reads_number = len(read_list)

    if parser.spec_value:
        number_spec_pct = int(total_reads_number * float(parser.spec_value) / 100)
        if parser.read2:
            with gzip.open(prefix + "_" + parser.spec_value + "pct_R1.fq.gz", "aw") as f1, gzip.open(prefix + '_' + parser.spec_value + "pct_R2.fq.gz", "aw") as f2:
                for index, each in enumerate(read_list, 1):
                    if index <= number_spec_pct:
                        SeqIO.write(adict[each], f1, "fastq")
                        SeqIO.write(bdict[each], f2, "fastq")
        else:
            with gzip.open(prefix + "_" + parser.spec_value + "pct_R1.fq.gz", "aw") as f1:
                for index, each in enumerate(read_list, 1):
                    if index <= number_spec_pct:
                        SeqIO.write(adict[each], f1, "fastq")
        print("%s all finished!\n" % print_current_time())
    else:
        number_05pct = int(total_reads_number * 0.05)
        number_10pct = int(total_reads_number * 0.1)
        number_20pct = int(total_reads_number * 0.2)
        number_40pct = int(total_reads_number * 0.4)
        number_60pct = int(total_reads_number * 0.6)
        number_80pct = int(total_reads_number * 0.8)

        print("%s shuffle random list\n" % print_current_time())
        random.shuffle(read_list)

        print("%s writing to fastq...\n" % print_current_time())
        if parser.read2:
            with gzip.open(prefix + "_05pct_R1.fq.gz", "aw") as f1,  gzip.open(prefix + "_05pct_R2.fq.gz", "aw") as f2,  gzip.open(prefix + "_10pct_R1.fq.gz", "aw") as f3, \
                    gzip.open(prefix + "_10pct_R2.fq.gz", "aw") as f4,  gzip.open(prefix + "_20pct_R1.fq.gz", "aw") as f5,  gzip.open(prefix + "_20pct_R2.fq.gz", "aw") as f6, \
                    gzip.open(prefix + "_40pct_R1.fq.gz", "aw") as f7,  gzip.open(prefix + "_40pct_R2.fq.gz", "aw") as f8,  gzip.open(prefix + "_60pct_R1.fq.gz", "aw") as f9, \
                    gzip.open(prefix + "_60pct_R2.fq.gz", "aw") as f10, gzip.open(prefix + "_80pct_R1.fq.gz", "aw") as f11, gzip.open(prefix + "_80pct_R2.fq.gz", "aw") as f12:
                for index, each in enumerate(read_list, 1):
                    if index <= number_05pct:
                        SeqIO.write(adict[each], f1, "fastq")
                        SeqIO.write(bdict[each], f2, "fastq")
                    if index <= number_10pct:
                        SeqIO.write(adict[each], f3, "fastq")
                        SeqIO.write(bdict[each], f4, "fastq")
                    if index <= number_20pct:
                        SeqIO.write(adict[each], f5, "fastq")
                        SeqIO.write(bdict[each], f6, "fastq")
                    if index <= number_40pct:
                        SeqIO.write(adict[each], f7, "fastq")
                        SeqIO.write(bdict[each], f8, "fastq")
                    if index <= number_60pct:
                        SeqIO.write(adict[each], f9, "fastq")
                        SeqIO.write(bdict[each], f10, "fastq")
                    if index <= number_80pct:
                        SeqIO.write(adict[each], f11, "fastq")
                        SeqIO.write(bdict[each], f12, "fastq")
        else:
            with gzip.open(prefix + "_05pct_R1.fq.gz", "aw") as f1,  gzip.open(prefix + "_10pct_R1.fq.gz", "aw") as f3, gzip.open(prefix + "_20pct_R1.fq.gz", "aw") as f5, \
                    gzip.open(prefix + "_40pct_R1.fq.gz", "aw") as f7,  gzip.open(prefix + "_60pct_R1.fq.gz", "aw") as f9, gzip.open(prefix + "_80pct_R1.fq.gz", "aw") as f11:
                for index, each in enumerate(read_list, 1):
                    if index <= number_05pct:
                        SeqIO.write(adict[each], f1, "fastq")
                    if index <= number_10pct:
                        SeqIO.write(adict[each], f3, "fastq")
                    if index <= number_20pct:
                        SeqIO.write(adict[each], f5, "fastq")
                    if index <= number_40pct:
                        SeqIO.write(adict[each], f7, "fastq")
                    if index <= number_60pct:
                        SeqIO.write(adict[each], f9, "fastq")
                    if index <= number_80pct:
                        SeqIO.write(adict[each], f11, "fastq")
        print("%s all finished!\n" % print_current_time())

if __name__ == '__main__':
    main()
