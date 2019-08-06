# This is README. Welcome to read my code and join me review my code.

 if the scripts start with pytricks, it is from the book pytricks, it shows some python skills.

    pytricks_dict_if.py 

    pytricks_merge_dicts.py

if the scripts start with "smart", it is mostly a wraper of some tools, for example:

    smart_git.py : is a wraper for git, it will submit and push your code with one step.
    smart_split.py : split a file with a integer  number. quick split files.

each file ...

# Brute Force zip file:

Brute_Force_zip.py is a script that can brute force zip file while using the passwords.txt as a known passwords database.

* related refs: passwords.txt

example:
```
python Brute_Force_zip.py <your_file.zip>
```

# Compared two files:

With this tool you can calculate the intersection(s) of list of elements. It will generate a textual output indicating which elements are in each intersection or are unique to a certain list. Currently you are able to calculate the intersections of at maximum 30 lists.

The graphical output is produced in JPG format.
* related refs: compare.py compare.list_a.txt compare.list_b.txt 

example: 
```
python compare.py -a compare.list_a.txt -al 1 -b compare.list_b.txt -bl 1
```

# extract Fastq/Fasta information.
```
#support read id list file
python extract.FastX.py test.fq test.list
# support gzip file and specific read id
python extract.FastX.py test.fastq.gz M04261:27:000000000-C7J75:1:1101:11401:1775
# support specific region 
python extract.FastX.py test.fa chr1 2 5
# support specific chrome.
python extract.FastX.py test.fa chr1
```
more detail see: "https://www.jianshu.com/p/22051fc6e0a3"

# parse Fastqc's html
```
This script was used to parser html info that aimed for Fastqc result.
example: 
python fastqc_html_parser.py /path/to/html/
```

# print Most commonly used commands in Linux
```
# just type:
python print_MCUC.py
```

# deal Fastx file
all scripts are in Fastx dir.
1. complement and reverse a Fastq file:
python complement_reverse_Fastq_2_Fastq.py xxx.fq >xxx.complement.reverse.fq 

# md5sum check
```
normally, use md5sum -c MD5.txt
sh smart_md5sum_check.sh # this script is a tricks of use md5sum in patch way.
```

