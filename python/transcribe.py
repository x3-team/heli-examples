"""Расшифровка аудио (Whisper) через Heli: POST /v1/audio/transcriptions.

    export HELI_API_KEY=sk-heli-...
    python transcribe.py meeting.mp3
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

path = sys.argv[1] if len(sys.argv) > 1 else "audio.mp3"

with open(path, "rb") as audio:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",  # алиас; канонический id в каталоге: openai/whisper-1
        file=audio,
    )

print(transcript.text)
