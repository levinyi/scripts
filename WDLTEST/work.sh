
java -jar /usr/local/bin/womtool-85.jar validate parallel_copy.wdl

cromwell run parallel_copy.wdl  --inputs inputs.json
