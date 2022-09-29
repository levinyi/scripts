"""  smart git tools """
# Info
__author__ = 'Shiyi Du'

# Imports
import sys
import os

def git_push(ajob):
    """docstring for push_git"""
    os.system("git add %s" % ajob)
    os.system("git commit -m 'some changes' ")
    os.system("git push origin master")

def main():
    JOBs = sys.argv[1:]
    for each_job in JOBs:
        if not os.path.exists(each_job):
            sys.exit("No such file!")
        else:
            git_push(each_job)

if __name__ == '__main__':
    main()
