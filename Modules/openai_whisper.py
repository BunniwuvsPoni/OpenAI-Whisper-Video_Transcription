# Date last updated: 2024/11/17

# This script is intended to: Transcribe using OpenAI's Whisper
def transcribe_audio(inputFile, outputDirectory, outputFileName):
    import whisper
    import whisper.utils

    model = whisper.load_model("turbo")
    result = model.transcribe(inputFile, verbose=True, fp16=False)
    print(result["text"])

    writer = whisper.utils.get_writer("srt",outputDirectory)
    writer(result,outputFileName,{})