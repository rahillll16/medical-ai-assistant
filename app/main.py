from app.ui import *
from agent.agent_runner import clear_chat
import gradio as gr

with gr.Blocks(
    title="Medical AI Assistant",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="cyan",
        neutral_hue="gray"
    ),
) as ui:

    # ---------------------------
    # HEADER
    # ---------------------------
    gr.Markdown(
        """
        # 🏥 Medical AI Assistant  

        A smart assistant to help you **find the best hospitals** based on  
        **city, medical department, rating, and budget**.
        """
    )

    # ---------------------------
    # HOW TO USE
    # ---------------------------
    with gr.Accordion("ℹ️ How to use this assistant", open=True):
        gr.Markdown(
            """
            **You can interact in two ways:**

            **⌨️ Text Input**
            - Type your query and press **Enter** or click **Send**
            - Example:  
              *"Best cardiology hospital in Chennai"*

            **🎙️ Voice Input**
            - Click the mic, speak clearly, and release
            - Your speech will be converted to text automatically

            **💰 Budget Handling**
            - If a hospital feels expensive, say:  
              *"This is expensive"*  
            - The assistant will suggest more affordable options
            """
        )

    # ---------------------------
    # SUPPORTED DEPARTMENTS
    # ---------------------------
    with gr.Accordion("🧑‍⚕️ Supported Medical Departments", open=False):
        gr.Markdown(
            """
            You can ask for cities:
            **Delhi**
            **Chennai**
            **Bengaluru**
            **Hyderabad**
            **Mumbai**
            
            You can ask for hospitals in the following departments:

            - 🫀 **Cardiology**
            - 🧠 **Neurology**
            - 🦴 **Orthopedics**
            - 🧬 **Oncology**
            - 🧃 **Gastroenterology**

            If you mention symptoms (like *headache*, *chest pain*, *fever*),
            the assistant will automatically map them to the correct department.
            """
        )

    # ---------------------------
    # CHAT WINDOW
    # ---------------------------
    chatbot = gr.Chatbot(
        height=480,
        type="messages",
        label="💬 Conversation",
        show_copy_button=True
    )

    # ---------------------------
    # INPUT AREA
    # ---------------------------
    with gr.Row():
        message = gr.Textbox(
            label="Type your message",
            placeholder="e.g. Best neurology hospital in Delhi",
            scale=4,
        )

        audio_input = gr.Audio(
            type="filepath",
            label="🎙️ Speak",
            scale=2,
        )

    with gr.Row():
        send_btn = gr.Button("📨 Send", variant="primary")
        clear_btn = gr.Button("🧹 Clear Chat", variant="secondary")

    # ---------------------------
    # AUDIO OUTPUT
    # ---------------------------
    audio_output = gr.Audio(
        autoplay=True,
        label="🔊 Assistant Voice Response"
    )

    # ---------------------------
    # TEXT FLOW
    # ---------------------------
    message.submit(
        put_message_in_chatbot,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    ).then(
        chat,
        inputs=[chatbot, audio_input],
        outputs=[chatbot, audio_output, audio_input]
    )

    send_btn.click(
        put_message_in_chatbot,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    ).then(
        chat,
        inputs=[chatbot, audio_input],
        outputs=[chatbot, audio_output, audio_input]
    )

    # ---------------------------
    # AUDIO FLOW
    # ---------------------------
    audio_input.stop_recording(
        chat,
        inputs=[chatbot, audio_input],
        outputs=[chatbot, audio_output, audio_input]
    )

    # ---------------------------
    # CLEAR
    # ---------------------------
    clear_btn.click(
        clear_chat,
        outputs=[chatbot, audio_output, message, audio_input]
    )

ui.launch(inbrowser=True)
