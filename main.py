# This is the main Python script executing Function(s)/Module(s) as required for the Application to run

# Main function
def main():
    import Modules.directory_services
    import Modules.openai_whisper
    import Modules.ffmpeg_operations
    import Modules.logging
    import os

    # Get directory of video(s)
    directory = Modules.directory_services.select_directory()

    # Get all .mp4 files
    filteredFiles = Modules.directory_services.filter_directory(directory, '.mp4')

    # Creates subdirectories as needed
    mp3Directory = directory + "/mp3/"
    os.makedirs(mp3Directory, exist_ok=True)
    transcriptionDirectory = directory + "/transcription/"
    os.makedirs(transcriptionDirectory, exist_ok=True)
    finalDirectory = directory + "/output/"
    os.makedirs(finalDirectory, exist_ok=True)

    # Log file path
    log = finalDirectory + "Log.txt"

    # Logging start
    timeStart = Modules.logging.time()
    Modules.logging.log(log, timeStart + ": Start processing files in: " + directory)

    # Process filtered files
    for file in filteredFiles:
        # Extract .mp3
        inputFile = directory + "/" + file     
        extractAudioOutputFile = mp3Directory + file.replace(".mp4", ".mp3")

        # Logging .mp3 extraction
        timeStartmp3 = Modules.logging.time()
        Modules.logging.log(log, timeStartmp3 + ": Extracting .mp3 from: " + file)

        # Extraction of .mp3
        Modules.ffmpeg_operations.extract_audio(inputFile, extractAudioOutputFile)

        # Logging .mp3 extraction
        timeEndmp3 = Modules.logging.time()
        Modules.logging.log(log, timeEndmp3 + ": Extracted .mp3 from: " + file)
        Modules.logging.log(log, "Total extraction time of: " + (timeEndmp3 - timeStartmp3) + " for: " + file)

        # Generate .srt files using OpenAi Whisper
        transcribeAudioOutputFileName = transcriptionDirectory + file.replace(".mp4", ".srt")

        # Logging transcription
        timeStartTranscription = Modules.logging.time()
        Modules.logging.log(log, timeStartTranscription + ": Transcribing .mp3 from: " + file)

        # Transcription of audio file
        Modules.openai_whisper.transcribe_audio(extractAudioOutputFile, transcriptionDirectory, transcribeAudioOutputFileName)

        # Logging transcription
        timeEndTranscription = Modules.logging.time()
        Modules.logging.log(log, timeEndTranscription + ": Transcribed .mp3 from: " + file)
        Modules.logging.log(log, "Total transcription time of: " + (timeEndTranscription - timeStartTranscription) + " for: " + file)

        # Generate subtitled video file
        finalOutputFileName = finalDirectory + file.replace(".mp4", "-Processed.mp4")

        # Logging transcoding
        timeStartTranscoding = Modules.logging.time()
        Modules.logging.log(log, timeStartTranscoding + ": Transcoding subtitles from: " + file)

        # Transcode video with subtitles
        Modules.ffmpeg_operations.transcribe_subtitles(inputFile, finalOutputFileName, transcribeAudioOutputFileName)

        # Logging transcoding
        timeEndTranscoding = Modules.logging.time()
        Modules.logging.log(log, timeEndTranscoding + ": Transcoded subtitles from: " + file)
        Modules.logging.log(log, "Total transcoding time of: " + (timeEndTranscoding - timeStartTranscoding) + " for: " + file)

    # Logging end
    timeEnd = Modules.logging.time()
    Modules.logging.log(log, timeEnd + ": End of processing files in: " + directory)
    Modules.logging.log(log, "Total processing time: " + (timeEnd - timeStart))

# Main execution
if __name__ == "__main__":
    main()