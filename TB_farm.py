import sys
import argparse

def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('-v1',  action='store', dest='v1', type=int, help="")
    parser.add_argument('-v2',  action='store', dest='v2', type=int, help="")
    parser.add_argument('-dis1',  action='store', dest='dis1', type=float, help="")
    parser.add_argument('-dis2',  action='store', dest='dis2', type=float, help="")
    return parser.parse_args()

def main():
    parser = _argparse()

    v1 = parser.v1
    v2 = parser.v2
    dis1 = 10000 * parser.dis1
    dis2 = 100000000 * parser.dis2
    s = dis1/v1 + dis2/v2
    print("{}s".format(s))
    print("{}m".format(s/60))
    print("{}h".format(s/3600))
    print("{}d".format(s/3600/24))
    

if __name__ == '__main__':
    main()
