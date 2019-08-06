ls ./*/*.txt |while read line;do name=`ls $line|awk -F '/' '{print$2}'`;echo "cd $name && md5sum -c MD5* && cd ..";done |sh
