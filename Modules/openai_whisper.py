# Date last updated: 2024/11/17

# This script is intended to: Transcribe using OpenAI's Whisper
def transcribe_audio(inputFile):
    import whisper

    model = whisper.load_model("turbo")
    result = model.transcribe(inputFile)
    print(result["text"])