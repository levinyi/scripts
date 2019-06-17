from pyquery import PyQuery as pq
import sys

d = pq(sys.argv[1])
print d('body').html()
