import tempfile
from openai import OpenAI

client = OpenAI()

def text_to_speech(text: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(tmp.name)

    return tmp.name
