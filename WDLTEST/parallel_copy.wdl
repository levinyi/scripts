task copy {
    File input_file
    String destination
  command {
    cp ${input_file} ${destination}
    echo "finished copy ${input_file} to ${destination}"
  }
  output {
    String output_file = "${destination}/${input_file}"
  }
}

workflow parallel_copy {
  Array[File] input_files
  String destination

  scatter (input_file in input_files) {
    call copy {
      input: 
        input_file = input_file, destination = destination
    }
  }
}

