task copy {
  input {
    File input_file
    String destination
  }
  command {
    cp ${input_file} ${destination}
  }
  output {
    File output_file = "${destination}/${input_file.name}"
  }
}

workflow parallel_copy {
  Array[File] input_files
  String destination

  scatter (input_file in input_files) {
    call copy {
      input: input_file = input_file, destination = destination
    }
  }
}

