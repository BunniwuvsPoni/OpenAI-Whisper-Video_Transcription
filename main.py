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
    logString = "Start processing files in: " + directory
    Modules.logging.log(log, logString)

    # Process filtered files
    for file in filteredFiles:
        # Extract .mp3
        inputFile = directory + "/" + file     
        extractAudioOutputFile = mp3Directory + file.replace(".mp4", ".mp3")

        # Logging .mp3 extraction
        timeStartmp3 = Modules.logging.time()
        logString = "Extracting .mp3 from: " + file
        Modules.logging.log(log, logString)

        # Extraction of .mp3
        Modules.ffmpeg_operations.extract_audio(inputFile, extractAudioOutputFile)

        # Logging .mp3 extraction
        timeEndmp3 = Modules.logging.time()
        logString = "Extracted .mp3 from: " + file
        Modules.logging.log(log, logString)
        timeDifferencemp3 = timeEndmp3 - timeStartmp3
        timeDifferencemp3String = str(timeDifferencemp3)
        logString = "Total extraction time of: " + timeDifferencemp3String + " for: " + file
        Modules.logging.log(log, logString)

        # Generate .srt files using OpenAi Whisper
        transcribeAudioOutputFileName = transcriptionDirectory + file.replace(".mp4", ".srt")

        # Logging transcription
        timeStartTranscription = Modules.logging.time()
        logString = "Transcribing .mp3 from: " + file
        Modules.logging.log(log, logString)

        # Transcription of audio file
        Modules.openai_whisper.transcribe_audio(extractAudioOutputFile, transcriptionDirectory, transcribeAudioOutputFileName)

        # Logging transcription
        timeEndTranscription = Modules.logging.time()
        logString = "Transcribed .mp3 from: " + file
        Modules.logging.log(log, logString)
        timeDifferenceTranscription = timeEndTranscription - timeStartTranscription
        timeDifferenceTranscriptionString = str(timeDifferenceTranscription)
        logString = "Total transcription time of: " + timeDifferenceTranscriptionString + " for: " + file
        Modules.logging.log(log, logString)

        # Generate subtitled video file
        finalOutputFileName = finalDirectory + file.replace(".mp4", "-Processed.mp4")

        # Logging transcoding
        timeStartTranscoding = Modules.logging.time()
        logString = "Transcoding subtitles from: " + file
        Modules.logging.log(log, logString)

        # Transcode video with subtitles
        Modules.ffmpeg_operations.transcribe_subtitles(inputFile, finalOutputFileName, transcribeAudioOutputFileName)

        # Logging transcoding
        timeEndTranscoding = Modules.logging.time()
        logString = "Transcoded subtitles from: " + file
        Modules.logging.log(log, logString)
        timeDifferenceTranscoding = timeEndTranscoding - timeStartTranscoding
        timeDifferenceTranscodingString = str(timeDifferenceTranscoding)
        logString = "Total transcoding time of: " + timeDifferenceTranscodingString + " for: " + file
        Modules.logging.log(log, logString)

    # Logging end
    timeEnd = Modules.logging.time()
    logString = "End of processing files in: " + directory
    Modules.logging.log(log, logString)
    timeDifferenceRun = timeEnd - timeStart
    timeDifferenceRunString = str(timeDifferenceRun)
    logString = "Total processing time: " + timeDifferenceRunString
    Modules.logging.log(log, logString)

# Main execution
if __name__ == "__main__":
    main()