""" Deal igblast result """
import sys
import os

# Check requirements
if sys.version_info < (2, 7, 0):
    sys.exit('At least Python 3.4.0 is required.\n')


# Get version, author and license information
info_file = os.path.join('/cygene/script', 'Version.py')
__version__, __author__, __license__ = None, None, None
try:
    exec(open(info_file).read())
except:
    sys.exit('Failed to load package information from %s.\n' % info_file)

if __version__ is None:
    sys.exit('Missing version information in %s\n.' % info_file)
if __author__ is None:
    sys.exit('Missing author information in %s\n.' % info_file)
if __license__ is None:
    sys.exit('Missing license information in %s\n.' % info_file)


igblast_out = sys.argv[1:-1]
result_dict = {}
for each_file in igblast_out:
    with open(each_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("V") or line.startswith("J") or line.startswith("D"):
                read_id = line.split()[1]
                gene = line.split()[2]
                identity = line.split()[3]
                length = line.split()[4]
                if read_id.startswith("reversed"):
                    # this is a reversed read_id
                    read_id = read_id.replace("reversed|", "")
                    result_dict.setdefault(read_id, []).append(gene)
                else:
                    # this is a forword read_id
                    result_dict.setdefault(read_id, []).append(gene)


with open(sys.argv[-1], "w") as output:
    for k, v in result_dict.items():
        output.write("%s\t%s\t%s\n" % (k, len(v), v))
