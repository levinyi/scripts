import sys
import os

# files should less than 1000 per time.
output_file = sys.argv[1]
input_files = sys.argv[2:]

index = 0
tmp_file_list = []
cmd = []
while len(input_files) > 0:
    a = input_files[:1000]
    del input_files[:1000]
    index += 1
    tmp_file = 'tmp_' + str(index) + '.bam'
    tmp_file_list.append(tmp_file)
    tmp_cmd = ['samtools', 'merge', '-f', '-@ 20', tmp_file, ' '.join(a)]
    cmd.append(tmp_cmd)
last_cmd = ['samtools', 'merge', '-f', '-@ 20', output_file, ' '.join(tmp_file_list)]
cmd.append(last_cmd)
for each in cmd:
    # print type(each)
    print " ".join(each)
