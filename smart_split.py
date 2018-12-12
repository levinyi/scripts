import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a","--total_number",type=int,help="total_number of the file")
parser.add_argument("-b","--line",type=int,help="how many lines in one.")
args = parser.parse_args()

for i in range(1,args.total_number):
    if args.total_number%(args.line*i) == 0:
        print args.line*i,args.total_number/(args.line*i)
