import sys
import zipfile

f = zipfile.ZipFile(sys.argv[1])
f.extractall(pwd='error')
with open('passwords.txt', "r") as pf:
    for line in pf:
        try:
            f.extractall(pwd=line.strip())
            print("password is {0}".format(line.strip()))
        except:
            pass
