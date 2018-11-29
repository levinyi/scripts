import sys
import os 

def git_push(a):
    """docstring for push_git"""
    os.system("git add %s"%a)
    os.system("git commit -m 'some changes' ")
    os.system("git push origin master")
    #print "git add ",a
    #print "git commit -m \"some changes\" "
    #print "git push origin master"

if __name__ == '__main__':
    job = sys.argv[1]
    git_push(job)
