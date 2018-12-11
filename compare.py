import sys
import os
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="A Python-Venn")
    parser.add_argument('-a', '--afile', action='store', dest='file1', required=True, help='first file')
    parser.add_argument('-al', action='store', default=1, dest='file1_colum', type=int, help='Set a colum to use, default first line.')
    parser.add_argument('-b', '--bfile', action='store', dest='file2', required=True, help='second file')
    parser.add_argument('-bl', action='store', default=1, dest='file2_colum', type=int, help='Set a colum to use, default first line.')

    parser.add_argument('-c', '--common', action='store_true', dest='common', default=False, help='show common or not. Default [ False ]. show this common result.')
    parser.add_argument('-u', '--union',  action='store_true', dest='union', default=False, help='show union or not. Default [ False ]. will not print this union result.')
    parser.add_argument('-l', '--leftside', action='store_true', dest='leftside', default=False, help='show rest of A file. Default: False. will not print this leftside result.')
    parser.add_argument('-r', '--rightside', action='store_true', dest='rightside', default=False, help='Show rest of B file. Default [ False ]. Will not print this rightside result.')
    parser.add_argument('-cname', '--cfilename', action='store', dest='common_op_file', help='write common result to output file. Default: print this common result to screen.')
    parser.add_argument('-uname', '--ufilename', action='store', dest='union_op_file',  help='write  union result to output file. Default: print this union result to screen.')
    parser.add_argument('-lname', '--lfilename', action='store', dest='leftside_op_file', help='write leftside result to output file. Default: print this leftside result to screen.')
    parser.add_argument('-rname', '--rfilename', action='store', dest='rightside_op_file', help='write rightside result to ouput file. Default: print this rightside result to screen.')
    
    parser.add_argument('-g', '--graph', action='store_true', dest='graph', default=False, help='Draw a venn graph. Default [ False ]. will not print venn graph.')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def main():
    """docstring for main"""
    parser = _argparse()

    with open(parser.file1, "r") as f1, open(parser.file2, "r") as f2:
        file_list_a = [line.split()[parser.file1_colum - 1] for line in f1]
        file_list_b = [line.split()[parser.file2_colum - 1] for line in f2]

    number_of_elements_a = len(file_list_a)
    number_of_elements_b = len(file_list_b)
    # unique
    file_list_a = list(set(file_list_a))
    file_list_b = list(set(file_list_b))
    number_of_uniq_element_a = len(file_list_a)
    number_of_uniq_element_b = len(file_list_b)

    intersection = list(set(file_list_a).intersection(set(file_list_b)))
    union = list(set(file_list_a).union(set(file_list_b)))
    left_diff = list(set(file_list_a).difference(set(file_list_b)))
    right_diff = list(set(file_list_b).difference(set(file_list_a)))

    # print basic information.

    print("\t Number of elements \t number of unique elements")
    print("File A:\t %s\t%s" % (number_of_elements_a, number_of_uniq_element_a))
    print("File B:\t %s\t%s" % (number_of_elements_b, number_of_uniq_element_b))
    print("Overall number of unique elements: %s" % (len(union)))
    print("\n-----------------------------------------------------\n")
    print("left\tmiddle\tright")
    print("%s\t%s\t%s\n" % (len(left_diff), len(intersection), len(right_diff)))
    # print additional info.
    if parser.common:
        print("intersection list :")
        for line in intersection:
            print line
    if parser.leftside:
        print("File A list:")
        for line in left_diff:
            print line
        # print len(left_diff)
    if parser.rightside:
        print("File B list:")
        for line in right_diff:
            print line
        # print len(right_diff)
    if parser.union:
        print("File A+B union list:")
        for line in union:
            print line
        # print len(union)
    if parser.graph:
        with open("file_a", "w") as f1, open("file_b", "w") as f2:
            for each in file_list_a:
                f1.write("%s\n" % each)
            for each in file_list_b:
                f2.write("%s\n" % each)
        try:
            print("Rscript venn.R file_a file_b")
            os.system("Rscript venn.R file_a file_b")
        except:
            sys.exit(1)
        finally:
            pass
            # os.system("rm file_a file_b")
if __name__ == '__main__':
    main()
