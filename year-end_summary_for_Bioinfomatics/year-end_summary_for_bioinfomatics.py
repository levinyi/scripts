# python 3.5 +
# coding:UTF-8
import os
import sys
import time
import numpy as np


def TimeStampToTime(timestamp):
    """docstring for TimeStampToTime"""
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_scripts(currentPath):
    """docstring for get_scripts"""
    dirlist = []
    for dirpath, dirname, filename in os.walk(currentPath):
        for i in filename:
            if i.endswith(".py"):
                dirlist.append(os.path.join(dirpath, i))
    return dirlist


def get_Total_script_number(alist):
    """docstring for print_summary"""
    number_list = []
    for each_file in alist:
        file_number = os.popen("wc -l {}".format(each_file)).read().split()[0]
        number_list.append(int(file_number))

    list_a = np.array(number_list).tolist()
    max_index = list_a.index(max(list_a))
    total_number = np.sum(list_a)
    return total_number, max(list_a), max_index


def FileCreateTime(filePath):
    """docstring for FileCreateTime"""
    # filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    """docstring for get_FileModifyTime"""
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)


def get_FileAccessTime(filePath):
    """docstring for get_FileAccessTime"""
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def main():
    """docstring for main"""
    input_dir = sys.argv[1:]

    # initial a script class
    scripts_list = []

    for each in input_dir:
        # print("your input_dir is {}".format(os.path.abspath(each)))
        each_scripts_list = get_scripts(each)
        scripts_list.extend(each_scripts_list)

    # ## Answer First Question:
    total_file = len(scripts_list)
    print("1.这一年你写了{}个脚本".format(total_file))
    # Answer Question 2:
    total_number, max_number, max_index = get_Total_script_number(scripts_list)
    print("2.总代码量为{} 行，简直是一部天书".format(total_number))
    print("3.您写过最长的脚本是{} 共{}行，相当于一部长篇小说".format(os.path.basename(scripts_list[max_index]),max_number))
    print("4.time")
    for each in scripts_list:
        print(each, FileCreateTime(each), get_FileModifyTime(each), get_FileAccessTime(each))
        print(FileCreateTime(each), get_FileModifyTime(each), get_FileAccessTime(each))


if __name__ == '__main__':
    main()
