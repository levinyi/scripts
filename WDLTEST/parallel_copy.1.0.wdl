version 1.0

task copy {
		File source
		String dest_filename

    command <<<
        cp ${source.path} ${dest_filename}
    >>>

    output {
        File copied_file = dest_filename
    }
}

workflow parallel_copy {
    Array[File] files_to_copy
    String dest_dir = "/tmp/parallel_copy_test/"

    scatter (file in files_to_copy) {
        call copy {
            input:
                source = file,
                dest_filename = "${dest_dir}/${file.name}"
        }
    }
}

