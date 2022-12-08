import logging
import os
import sys


def two_dim_value_list(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].setdefault(key_b, []).append(val)
    else:
        thedict.update({key_a: {key_b: [val]}})
    return thedict


def find_dup_file(file_list):
    adict = {}
    flag = False
    for each_file in file_list:
        each_basename = os.path.basename(each_file)
        if "-1" in each_basename or "-2" in each_basename or '-3' in each_basename or '-4' in each_basename:
            """10x data"""
            flag = True
            f_name = "-".join(each_basename.split("-")[1:]).split("_")[0]
        else:
            """other data"""
            # f_name = os.path.basename(each_file).split("-")[1].split("_")[0] 
            f_name = os.path.basename(each_file).split("_")[0]

        # R220325P01-G0474E1L1-1_L3_1.fq.gz
        # R220620P02-G0484E8L1_L2_2.fq.gz # bug
        read = each_basename.split(".")[0].split("_")[-1]
        # print(f_name)

        if int(read) == 1:
            # "1" represents read 1. "2" is read 2.
            two_dim_value_list(adict, f_name, "1", each_file)
        elif int(read) == 2:
            two_dim_value_list(adict, f_name, "2", each_file)
        else:
            logging.error("Error file name {}".format(f_name))
    return adict, flag


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", datefmt = '%Y-%m-%d %H:%M:%S')

    input_dir_list = []
    all_fastq_list = []
    for each_dir in sys.argv[1:]:
        input_dir_list.append(each_dir)
        for f in os.listdir(each_dir):
            all_fastq_list.append(os.path.join(each_dir, f))

    fastq_dict, flag = find_dup_file(all_fastq_list)
    import json

    # print(json.dumps(fastq_dict,indent=2)) # for debug


    """ merge dict_data into a dir"""
    merged_sample = 0
    linked_sample = 0
    with open("merge.sh","w") as f:
        for each_sample in fastq_dict:
            for R in fastq_dict[each_sample]:
                fq_list = fastq_dict[each_sample][R]
                if len(fq_list) >1:
                    merged_sample +=1
                    if flag:
                        f.write("cat {} >{}_S1_L001_R{}_001.fastq.gz\n".format(" ".join(fq_list), each_sample, R))
                    else:
                        f.write("cat {} >{}_L1_{}.fq.gz\n".format(" ".join(fq_list), each_sample, R))
                else:
                    linked_sample +=1
                    if flag:
                        f.write("ln -s {} {}_S1_L001_R{}_001.fastq.gz\n".format(" ".join(fq_list), each_sample, R))
                    else:
                        f.write("ln -s {} {}_L1_{}.fq.gz\n".format(" ".join(fq_list), each_sample, R))
    sample_number =len(fastq_dict.keys())
    fq_number = len(fastq_dict.values())

    logging.info("Detected total :{} samples with {} unique fastqs. But find total {} fastqs.".format(sample_number, merged_sample, len(all_fastq_list)))
    logging.info("So, {} fastq files are duplicated out of {} files.".format(merged_sample, merged_sample*2))
    logging.info("linked sample:{}".format(linked_sample))
    logging.info("Total sample : {} unique fastq files. ".format(merged_sample+linked_sample))
    logging.info("please run : `sh merge.sh` to merge data")

if __name__ == '__main__':
    main()
