import sys
import pandas as pd


def _argparse():
    parser = argparse.ArgumentParser(description="A Python-spread script")
    parser.add_argument('-a', '--inputifle', action='store', dest='inputfile', required=True, help='input file')
    parser.add_argument('-o', '--outputfile',action='store', dest='outputfile', required=True, help='output file.')
    parser.add_argument('--index', action='store', dest='index_column', default=0)
    parser.add_argument('--columns',)
    parser.add_argument('--value',)
    parser.add_argument('-sa', '--separatora', action='store', dest='separatora', default='tab', help='separae. choose: tab or space, d')
    parser.add_argument('-header', action='store_true', dest='header', default=False, help='file with or without header, th')


def main():
    """docstring for main"""
    input_file = sys.argv[1]
    names = ('Clone', 'counts', 'well')
    # data = pd.read_table(input_file, sep="\t", header=None)
    # data = pd.read_table(input_file, sep="\t", names=names)
    data = pd.read_table(input_file, names=["Clone", "Count","Well"])
    # df = pd.DataFrame(data=data, index=columns).T  # .transpose()
    df = pd.DataFrame(data=data)  # .transpose()
    print(df.head(10))

    df1 = df.pivot_table(
        index = ["Clone"],
        columns = ["Well"],
        values = ["Count"],
        fill_value=0,
        )
########### method 1
    df1.columns = df1.columns.droplevel(0)
    df1.columns.name = None

########### method 2
# df1 = df1.rename_axis(None, axis=1).reset_index()

    print(df1.head(2))
    output_file = sys.argv[2]
    df1.to_csv(output_file)


if __name__ == '__main__':
    main()
