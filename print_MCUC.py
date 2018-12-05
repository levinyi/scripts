""" print Most commonly used commands in Linux """
import os
from collections import Counter
c = Counter()

with open(os.path.expanduser('~/.bash_history'),"r") as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] +=1
print c.most_common(20)
