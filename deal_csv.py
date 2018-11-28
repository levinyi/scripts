import sys
import csv
with open(sys.argv[1],"rb") as csvfile:
	# spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	print spamreader
	for row in spamreader:
		print row
		# print ','.join(row)
