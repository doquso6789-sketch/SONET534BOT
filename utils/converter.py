import ffmpeg


def convert_to_mp3(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file)
        .run(overwrite_output=True)
    )
