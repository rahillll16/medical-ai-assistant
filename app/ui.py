from agent.agent_runner import run_agent
from audio.speech_to_text import speech_to_text
from audio.text_to_speech import text_to_speech

def put_message_in_chatbot(message, history):
    if history is None:
        history = []

    # 🔥 If text exists, use it
    if message.strip():
        history.append({"role": "user", "content": message})

    return "", history

def chat(history, audio_path):
    if history is None:
        history = []

    # 🛑 Ignore empty audio-trigger calls
    if audio_path is None and (not history or history[-1]["role"] != "user"):
        return

    # 🎙️ AUDIO PATH EXISTS → handle audio
    if audio_path:
        user_text = speech_to_text(audio_path)
        history.append({"role": "user", "content": user_text})

    # ⌨️ TEXT PATH → user message already exists
    user_text = history[-1]["content"]

    # Add empty assistant message
    history.append({"role": "assistant", "content": ""})

    assistant_text = ""

    for token in run_agent(user_text, history[:-1]):
        assistant_text += token
        history[-1]["content"] = assistant_text
        yield history, None, None

    audio_reply = text_to_speech(assistant_text)
    yield history, audio_reply, None


