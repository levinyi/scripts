import sys


def addtwodimdict(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict '''
    if key_a in thedict:
        thedict[key_a].setdefault(key_b,[]).append(val)
    else:
        thedict.update({key_a:{key_b:[val]}})
    return thedict

a_dict = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip("\n")
        sample_name, insert_size_length, count, flag = line.split()
        if flag == '0':
            flag = 'Health'
        else:
            flag = 'IS'
        addtwodimdict(a_dict,flag,insert_size_length,int(count))

for flag,y in a_dict.items():
    for k,v in y.items():
        mean = float(sum(v))/len(v)
        print "%s\t%s\t%s" %(k,mean,flag)