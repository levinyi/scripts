#!/usr/bin/env python

import sys
import fastq
import time


def qual_stat(qstr):
    q20 = 0
    q30 = 0
    for q in qstr:
        qual = ord(q) - 33
        if qual >= 30:
            q30 += 1
            q20 += 1
        elif qual >= 20:
            q20 += 1
    return q20, q30


def stat(filename):
    reader = fastq.Reader(filename)
    total_count = 0
    q20_count = 0
    q30_count = 0
    while True:
        read = reader.nextRead()
        if not read:
            break
        total_count += len(read[3])
        q20, q30 = qual_stat(read[3])
        q20_count += q20
        q30_count += q30

    print("total bases:", total_count)
    print("q20 bases:", q20_count)
    print("q30 bases:", q30_count)
    print("q20 percents:", 100 * float(q20_count)/float(total_count))
    print("q30 percents:", 100 * float(q30_count)/float(total_count))


def main():
    if len(sys.argv) < 2:
        print("usage: python q30.py <fastq_file>")
        sys.exit(1)
    stat(sys.argv[1])

if __name__ == "__main__":
    time1 = time.time()
    main()
    time2 = time.time()
    print('Time used: ' + str(time2-time1))
