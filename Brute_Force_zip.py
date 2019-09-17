# coding=UTF-8
"""
用字典暴力破解zip压缩文件密码
ZIP压缩文件破解程序加强版， 用户可以自己制定想要破解的文件和破解字典，多线程破解
"""

import zipfile
import optparse

"""
f = zipfile.ZipFile(sys.argv[1])
f.extractall(pwd='error')
with open('passwords.txt', "r") as pf:
    for line in pf:
        try:
            f.extractall(pwd=line.strip())
            print("password is {0}".format(line.strip()))
        except:
            pass

"""
import threading

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd : ", password)
        return password
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')

    options, args = parser.parse_args()
    if options.zname == None or options.dname== None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    dFile = open(dname, 'r')
    for line in dFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractFile, args=(zFile, password))
        t.start()
        """
        guess = extractFile(zFile, password)
        if guess:
            print('Password = ', password)
            return
        else:
            print("can't find password")
            return
        """
if __name__ == '__main__':
    main()
