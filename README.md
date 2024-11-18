# OpenAI-Whisper-Video_Transcription
Using Python and OpenAI Whisper to transcribe videos.

# Requirements
    - OpenAI Whisper
        - pip install -U openai-whisper
    - FFMPEG (with PATH configured)
        - https://www.ffmpeg.org/download.html
            - Choose "release full builds"
        - "Edit the system environment variables" -> "Environment Variables..." -> "System variables" -> "Path" -> "New" -> Add location of FFmpeg -> Save
            - Verify by running "ffmpeg.exe -version"
    - python-ffmpeg
        - pip install -U python-ffmpeg