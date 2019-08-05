from pyquery import PyQuery as pq
import sys
import re


def usage():
    """
    docstring for usage

    Statistic content:
        # Filename,
        # Total Sequences
        # Filtered Sequences
        # Sequences length
        # % GC
        # % Q20
        # % Q30
    Usage:
        python fastqc_html_parser.py /path/to/html/ 
    
    Description:
        will parser all the htmls in the dirs.

    Change Log:
        20190801:Creat this script.

    """
    

p = re.compile(r'')
d = pq(sys.argv[1])
print d('body').html()

def main():
    """docstring for main"""
    html_files = [item for item in  os.listdir('.') if item.endswith('.html')]
    for html_file in html_files:
        with open(html_file, "r") as f:

    

if __name__ == '__main__':
    main()
