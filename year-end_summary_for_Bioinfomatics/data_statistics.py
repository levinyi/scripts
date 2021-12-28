import os
import sys
import time
import datetime


def get_FileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fileSize = os.path.getsize(filePath)
    fileSize = fileSize/float(1024*1024)
    return round(fileSize, 2)

def get_FileCreateTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

def get_FileModifyTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)

def write_2_txt(fileInfo, output_file):
    filename,size,year, =fileInfo.split(":")
    with open(output_file) as f:
        f.write(filename, size year)

def main():
    filePath = './'
    for path, dir_list, file_list  in os.walk(filePath):
        for file_name in file_list:
            print(os.path.join(path, file_name))
        
if __name__ == '__main__':
    main()
