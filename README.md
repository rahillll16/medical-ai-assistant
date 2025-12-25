# 🏥 Medical AI Assistant

A **multimodal AI-powered medical assistant** that helps users find the **best hospitals** based on **city, medical department, rating, and budget**, using **LLMs, tool calling, streaming responses, and audio input/output**.

This project is built with **Python, OpenAI APIs, and Gradio**, and uses **mock hospital data** for safe experimentation.

---

## ✨ Features

- 💬 Text-based chat interface  
- 🎙️ Voice input (Speech-to-Text)  
- 🔊 Voice output (Text-to-Speech)  
- ⚡ Streaming responses (token-by-token)  
- 🛠️ LLM tool calling for hospital search  
- 💰 Budget-aware recommendations (e.g. “this is expensive”)  
- 🧠 Symptom → department mapping  
- 🧱 Modular and scalable architecture  
- 🔐 Uses mock data only (no real medical advice)

---

## 🚨 Disclaimer

> This assistant **does NOT provide medical advice, diagnosis, or treatment**.  
> It only recommends hospitals based on the provided dataset.

---

## 🧑‍⚕️ Supported Medical Departments

The assistant can recommend hospitals for:

- 🫀 Cardiology  
- 🧠 Neurology  
- 🦴 Orthopedics  
- 🧬 Oncology 
- 🧃 Gastroenterology  

If you mention **symptoms** (e.g. *headache*, *chest pain*, *fever*), the assistant automatically maps them to the appropriate department.

---

## 📁 Project Structure & Setup Instructions

### 📁 Project Structure

medical-ai-assistant/
│
├── app/                  # Application entry point & UI
│   ├── main.py           # Launches the Gradio app
│   └── ui.py             # Gradio UI + event wiring
│
├── agent/                # AI agent logic
│   ├── system_prompt.py  # System prompt & rules
│   ├── agent_runner.py   # Tool calling + streaming logic
│   └── state.py          # Conversation & budget state
│
├── tools/                # Tool implementations
│   ├── hospital_finder.py # Hospital search logic
│   ├── tool_schema.py     # Tool JSON schema
│   └── tool_handler.py    # Tool execution handler
│
├── audio/                # Audio processing
│   ├── speech_to_text.py  # Audio → text
│   └── text_to_speech.py  # Text → audio
│
├── data/
│   └── MOCK_DATA.json    # Mock hospital dataset
│
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md


---

### ⚙️ Setup Instructions

Follow the steps below to run the project locally.

---

#### 1️⃣ Clone the Repository

git clone https://github.com/rahillll16/medical-ai-assistant.git  
cd medical-ai-assistant

---

#### 2️⃣ Create a Virtual Environment (Recommended)

python -m venv .venv

Activate it:

Windows  
.venv\Scripts\activate

macOS / Linux  
source .venv/bin/activate

---

#### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

#### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add:

OPENAI_API_KEY=your_openai_api_key_here

(You can copy from `.env.example`)

---

#### 5️⃣ Run the Application

python app/main.py

The Gradio interface will automatically open in your browser.

---

### 📝 Notes

- This project uses **mock hospital data** (`MOCK_DATA.json`)
- No real medical diagnosis or treatment is provided
- Audio input/output requires a working microphone
- Streaming responses may take a few seconds depending on network speed
- Designed for **educational and experimental purposes**

---


