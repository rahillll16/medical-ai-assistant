from openai import OpenAI

client = OpenAI()

def speech_to_text(audio_path: str) -> str:
    with open(audio_path, "rb") as audio:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio
        )
    return transcript.text
