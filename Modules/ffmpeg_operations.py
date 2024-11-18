# Date last updated: 2024/11/17

# This script is intended to: Extract Audio from the Video file
def extract_audio(inputFile, outputFile):
    from __future__ import annotations

    from ffmpeg import FFmpeg, Progress

    ffmpeg = (
        FFmpeg()
        .input(inputFile)
        .output(outputFile)
    )

    @ffmpeg.on("start")
    def on_start(arguments: list[str]):
        print("arguments:", arguments)

    @ffmpeg.on("stderr")
    def on_stderr(line):
        print("stderr:", line)

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    @ffmpeg.on("completed")
    def on_completed():
        print("completed")

    @ffmpeg.on("terminated")
    def on_terminated():
        print("terminated")

    ffmpeg.execute()

# This script is intended to: Add subtitles to the Video file
def transcribe_subtitles(inputFile, outputFile, srtFile):
    from __future__ import annotations

    from ffmpeg import FFmpeg, Progress

    subtitles = "subtitles='" + srtFile.replace(":/", "\\:/") + "'"

    ffmpeg = (
        FFmpeg()
        .input(inputFile)
        .output(
            outputFile,
            vf=subtitles
        )
    )

    @ffmpeg.on("start")
    def on_start(arguments: list[str]):
        print("arguments:", arguments)

    @ffmpeg.on("stderr")
    def on_stderr(line):
        print("stderr:", line)

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    @ffmpeg.on("completed")
    def on_completed():
        print("completed")

    @ffmpeg.on("terminated")
    def on_terminated():
        print("terminated")

    ffmpeg.execute()