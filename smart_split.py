""" this module docstring"""
import argparse


def main():
    """docstring for main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--total_nu", type=int, help="files total numbe")
    parser.add_argument("-b", "--line", type=int, help="how many lines in one")
    args = parser.parse_args()

    for i in range(1, args.total_nu):
        if args.total_nu % (args.line*i) == 0:
            print(args.line*i, args.total_nu/(args.line*i))


if __name__ == '__main__':
    main()
