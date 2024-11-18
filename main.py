# This is the main Python script executing Function(s)/Module(s) as required for the Application to run

# Main function
def main():
    import Modules.directory_services
    import Modules.openai_whisper
    import Modules.ffmpeg_operations
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

    # Process filtered files
    for file in filteredFiles:
        # Extract .mp3
        inputFile = directory + "/" + file
        print (inputFile)        
        extractAudioOutputFile = mp3Directory + file.replace(".mp4", ".mp3")
        print (extractAudioOutputFile)

        Modules.ffmpeg_operations.extract_audio(inputFile, extractAudioOutputFile)

        # Generate .srt files using OpenAi Whisper
        transcribeAudioOutputFileName = transcriptionDirectory + file.replace(".mp4", ".srt")

        Modules.openai_whisper.transcribe_audio(extractAudioOutputFile, transcriptionDirectory, transcribeAudioOutputFileName)

        # Generate subtitled video file
        finalOutputFileName = finalDirectory + file.replace(".mp4", "-Processed.mp4")

        Modules.ffmpeg_operations.transcribe_subtitles(inputFile, finalOutputFileName, transcribeAudioOutputFileName)

# Main execution
if __name__ == "__main__":
    main()