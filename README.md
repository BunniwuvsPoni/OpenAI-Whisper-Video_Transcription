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

# Description
This application is intended to process a directory of video files, generate the necessary transcription using OpenAI Whisper, and finally transcode the subtitles into the original video file.

Note: This application is built from within a Windows environment and has not been tested elsewhere.

# Steps
1. User selects a directory containing the video file(s)
2. Application searches for all .mp4 file(s) in the directory, sub-directories not included. To change the file type, update the record in main.py
    - filteredFiles = Modules.directory_services.filter_directory(directory, '.mp4')
3. Processes each video file found:
4. Extracts .mp3 from the video file using FFmpeg
5. Generates transcription using OpenAI Whisper
6. Transcode transcription back into the video file using FFmpeg