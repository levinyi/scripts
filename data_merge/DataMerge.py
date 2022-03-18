import sys
import os
sys.path.append("/cygene/script/python_packages/")
import MultiDict


input_dir_list = []
all_fastq_list = []
for each_dir in sys.argv[1:]:
    input_dir_list.append(each_dir)
    for f in os.listdir(each_dir):
        # print(f)
        all_fastq_list.append(os.path.join(each_dir, f))

print(len(input_dir_list), input_dir_list)
print(len(all_fastq_list), all_fastq_list[:5])



def find_dup_file(file_list):
    adict = {}
    for each_file in file_list:
        f_name = os.path.basename(each_file).split("-")[1].split("_")[0]
        read = os.path.basename(each_file).split(".")[0].split("_")[-1]
        # print(f_name)

        if int(read) == 1:
            # "1" represent read 1. "2" is read 2.
            MultiDict.two_dim_value_list(adict,f_name,"1",each_file)
        else:
            MultiDict.two_dim_value_list(adict,f_name,"2",each_file)
    return adict

fastq_dict = find_dup_file(all_fastq_list)
import json
print(json.dumps(fastq_dict,indent=2))
'''
{
  "G470E6L1": {
    "R1": [
      "/cygene2/data/2022/20220304_HCY3MDSX3-1-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L1_1.fq.gz",
      "/cygene2/data/2022/20220307_HF73KDSX3-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L2_1.fq.gz",
      "/cygene2/data/2022/20220309_HF57KDSX3-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L1_1.fq.gz"
    ],
    "R2": [
      "/cygene2/data/2022/20220304_HCY3MDSX3-1-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L1_2.fq.gz",
      "/cygene2/data/2022/20220307_HF73KDSX3-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L2_2.fq.gz",
      "/cygene2/data/2022/20220309_HF57KDSX3-X101SC20031639-Z03_Result/Rawdata/R220228P01-G470E6L1_L1_2.fq.gz"
    ]
  },
'''

# merge dict_data into a dir
with open("merge.txt","w") as f:
    for each_sample in fastq_dict:
        for R in fastq_dict[each_sample]:
            fq_list = fastq_dict[each_sample][R]
            f.write("cat {} >{}_L1_{}.fq.gz\n".format(" ".join(fq_list), each_sample,R))
print("run : sh merge.txt to merge data")