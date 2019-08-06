"""  smart git tools """
import sys
import os
# Info
__author__ = 'Shiyi Du'

# Imports


def git_push(ajob):
    """docstring for push_git"""
    os.system("git add %s" % ajob)
    os.system("git commit -m 'some changes' ")
    os.system("git push origin master")

if __name__ == '__main__':
    JOB = sys.argv[1]
    if not os.path.exists(JOB):
        sys.exit("No such file!")
    else:
        git_push(JOB)
