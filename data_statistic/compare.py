''' these modules were used.'''
import os
import argparse
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from matplotlib_venn import venn2


def _argparse():
    parser = argparse.ArgumentParser(description="A Python-Venn")
    parser.add_argument('-a', '--afile', action='store', dest='file1', required=True, help='first file')
    parser.add_argument('-al', action='store', default=1, dest='file1_colum', type=int, help='Set a colum to use, default [first column].')
    parser.add_argument('-sa', '--separatora', action='store', dest='separatora', default='tab', help='separator of first file. choose: tab or space, default [ tab ].')
    parser.add_argument('-header', action='store_true', dest='header', default=False, help='file with or without header, the first line is header or not.')

    parser.add_argument('-b', '--bfile', action='store', dest='file2', required=True, help='second file')
    parser.add_argument('-bl', action='store', default=1, dest='file2_colum', type=int, help='Set a colum to use, default [first column].')
    parser.add_argument('-sb', '--separatorb', action='store', dest='separatorb', default='tab', help='separator of second file. choose: tab or space, default [ tab ].')

    parser.add_argument('-c', '--common', action='store_true', dest='common', default=False, help='show common or not. Default [ False ]. show this common result.')
    parser.add_argument('-cname', '--cfilename', action='store', dest='common_op_file', help='You must give a file name when you use this parmarater. must use "-c" simultaneously. will write common result to the file which you give.')
    parser.add_argument('-u', '--union',  action='store_true', dest='union', default=False, help='show union or not. Default [ False ]. will not print this union result.')
    parser.add_argument('-uname', '--ufilename', action='store', dest='union_op_file',  help='You must give a file name when you use this parmarater. must use "-u" simultaneously. will write union result to the file which you give.')
    parser.add_argument('-l', '--leftside', action='store_true', dest='leftside', default=False, help='show rest of A file. Default: False. will not print this leftside result.')
    parser.add_argument('-lname', '--lfilename', action='store', dest='leftside_op_file', help='You must give a file name when you use this parmarater. must use "-l" simultaneously. will write leftside result to the file which you give.')
    parser.add_argument('-r', '--rightside', action='store_true', dest='rightside', default=False, help='Show rest of B file. Default [ False ]. Will not print this rightside result.')
    parser.add_argument('-rname', '--rfilename', action='store', dest='rightside_op_file', help='You must give a file name when you use this parmarater. must use "-r" simultaneously. will write rightside result to the file which you give.')
    parser.add_argument('-g', '--graph', action='store_true', dest='graph', default=False, help='Draw a venn graph. Default [ False ]. will not print venn graph.')
    parser.add_argument('-gname', '--graphname', action='store', dest='graph_name', help='Out put venn graph name.')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def write_to_file(a, b):
    with open(a, "w") as f:
        for line in b:
            f.write("%s\n" % line)


def print_to_screen(a):
    for line in a:
        print("%s" % line)


def main():
    """docstring for main"""
    parser = _argparse()

    # check arguments dependency.
    if parser.common_op_file and not parser.common:
        parser.error("The -cname argument requires the -c")
    if parser.union_op_file and not parser.union:
        parser.error("The -uname argument requires the -u")
    if parser.leftside_op_file and not parser.leftside:
        parser.error("The -lname argument requires the -l")
    if parser.rightside_op_file and not parser.rightside:
        parser.error("The -rname argument requires the -r")
    # deal input file A and B.
    with open(parser.file1, "r") as f1, open(parser.file2, "r") as f2:
        if parser.separatora == 'tab':
            file_list_a = [line.rstrip("\n").split("\t")[parser.file1_colum - 1] for line in f1]
        else:
            file_list_a = [line.rstrip("\n").replace("\t", " ").split()[parser.file1_colum - 1] for line in f1]
        if parser.separatorb == 'tab':
            file_list_b = [line.rstrip("\n").split("\t")[parser.file2_colum - 1] for line in f2]
        else:
            file_list_b = [line.rstrip("\n").replace("\t", " ").split()[parser.file2_colum - 1] for line in f2]

    number_of_elements_a = len(file_list_a)
    number_of_elements_b = len(file_list_b)
    # get a unique list
    file_list_a = list(set(file_list_a))
    file_list_b = list(set(file_list_b))
    number_of_uniq_element_a = len(file_list_a)
    number_of_uniq_element_b = len(file_list_b)

    # get intersection, union, and difference of two files.
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
    print("%s\t%s\t%s" % (len(left_diff), len(intersection), len(right_diff)))
    print("%.2f\t\t%.2f\n" % (float(len(intersection))/(len(intersection)+len(left_diff)), float(len(intersection))/(len(intersection)+len(right_diff))))

    # print additional info.
    if parser.common:
        if parser.common_op_file:
            write_to_file(parser.common_op_file, intersection)
        else:
            print("intersection list :")
            print_to_screen(intersection)
    if parser.leftside:
        if parser.leftside_op_file:
            write_to_file(parser.leftside_op_file, left_diff)
        else:
            print("File A list:")
            print_to_screen(left_diff)
    if parser.rightside:
        if parser.rightside_op_file:
            write_to_file(parser.rightside_op_file, right_diff)
        else:
            print("File B list:")
            print_to_screen(right_diff)
    if parser.union:
        if parser.union_op_file:
            write_to_file(parser.union_op_file, union)
        else:
            print("File A+B union list:")
            print_to_screen(union)
    if parser.graph:
        name1 = os.path.basename(parser.file1).split(".")[0]
        name2 = os.path.basename(parser.file2).split(".")[0]
        subsets = (len(left_diff), len(right_diff), len(intersection))
        pic = venn2(subsets, set_labels=(name1, name2), set_colors=('r','g'),alpha=0.4)
        #pic.get_patch_by_id('10').set_edgecolor('#FF0000') #左圆形边框颜色
        #pic.get_patch_by_id('10').set_linestyle('-.') #左圆形边框样式
        #pic.get_patch_by_id('10').set_linewidth(2) #左圆形边框大小
        #pic.get_patch_by_id('01').set_linestyle(':') #右圆形边框样式
        #pic.get_patch_by_id('11').set_edgecolor('#0F60A9') #中间边框颜色
        #pic.get_patch_by_id('11').set_linewidth(3) #中间边框大小 
        # https://dyfocus.com/zh-cn/news-philosophy/1d0511.html

        if parser.graph_name:
            plt.savefig(parser.graph_name)
        else:
            plt.savefig("venn.jpg")

if __name__ == '__main__':
    main()
