''' these modules were used.'''
import os
import argparse
from itertools import islice


def _argparse():
    parser = argparse.ArgumentParser(description="More description see: https://www.jianshu.com/p/66c0448f44f3")
    parser.add_argument('-a', '--filea', action='store', dest='file1', help="this is config file")
    parser.add_argument('-ka', '--key_a', action='store', dest='key_a', default=1, help="this is the key of filea colume.")
    parser.add_argument('-va', '--value_a', action='store', dest='value_a', default=2, help="this is the value of file A's colume.")
    parser.add_argument('-sa', '--separatora', action='store', dest='separatora', default='tab', help='separator of first file. choose: [tab] or [space], default [ tab ].')
    parser.add_argument('-headera', action='store_true', dest='headera', default=False, help='file with or without header, the first line is header or not.')
    parser.add_argument('-headerb', action='store_true', dest='headerb', default=False, help='file with or without header, the first line is header or not.')

    parser.add_argument('-b', '--fileb', action='store', dest='file2', help="this is list file")
    parser.add_argument('-kb', '--key_b', action='store', dest='key_b', default=1, help="this is the key of file")
    parser.add_argument('-vb', '--value_b', action='store', dest='value_b', default=2, help="this is the value of file B's colume.")
    parser.add_argument('-sb', '--separatorb', action='store', dest='separatorb', default='tab', help='separator of first file. choose: [tab] or [space], default [ tab ].')
    
    parser.add_argument('-u', '--union', action='store_true', dest='union', default=False, help='show union list')
    parser.add_argument('-f', '--freq',  action='store_true', dest='freq', default= False, help='calculate frequency for each value.')

    return parser.parse_args()


def deal_file(f, k, v, s, header):
    ''' deal file to get a dict for key and value. and get a list for all keys'''
    a_dict = {}
    a_list = []
    with open(f, "r") as f1:
        if header:
            for line in islice(f1, 1, None):
                line = line.rstrip("\n")
                if s == 'tab':
                    c = line.split("\t")
                else:
                    c = line.split()
                a_dict[c[int(k) - 1]] = c[int(v) - 1]
                a_list.append(c[int(k) - 1])
        else:
            for line in f1:
                line = line.rstrip("\n")
                if s == 'tab':
                    c = line.split("\t")
                else:
                    c = line.split()
                a_dict[c[int(k) - 1]] = c[int(v) - 1]
                a_list.append(c[int(k) - 1])
    return a_dict, a_list

def dict_freqency(adict):
    total_sum = sum((int(k) for k in adict.values()))
    new_dict = {}
    for each in adict:
        new_dict[each] = float(adict[each])/total_sum
    return new_dict

def main():
    parser = _argparse()

    file1_name = os.path.basename(parser.file1).split(".")[0]
    file2_name = os.path.basename(parser.file2).split(".")[0]

    file1_dict, file1_list = deal_file(parser.file1, parser.key_a, parser.value_a, parser.separatora, parser.headera)
    file2_dict, file2_list = deal_file(parser.file2, parser.key_b, parser.value_b, parser.separatorb, parser.headerb)
    
    if parser.freq:
        file1_dict = dict_freqency(file1_dict)  # recover the fomer dict.
        file2_dict = dict_freqency(file2_dict)  # recover the fomer dict.

    print("names\t%s\t%s" % (file1_name, file2_name))

    if parser.union:
        union_set = list(set(file1_list).union(set(file2_list)))
        for index, each in enumerate(union_set, 1):
            # print("{0}\t{1}\t{2}".format(index, file1_dict.get(each, 0), file2_dict.get(each, 0)))
            print("{0}\t{1}\t{2}".format(each, file1_dict.get(each, 0), file2_dict.get(each, 0)))
    else:
        intersection = list(set(file1_list).intersection(set(file2_list)))
        for index, each in enumerate(intersection, 1):
            # print("%s\t%s\t%s" % (index, file1_dict[each], file2_dict[each]))
            print("%s\t%s\t%s" % (each, file1_dict[each], file2_dict[each]))

if __name__ == '__main__':
    main()
