from openai import OpenAI
from agent.system_prompt import system_message
from agent.state import ConversationState
from tools.tool_schema import best_hospital_finder
from tools.tool_handler import handling_tool_calls

openai = OpenAI()
MODEL = "gpt-4.1-mini"
state = ConversationState()

tools = [{"type": "function", "function": best_hospital_finder}]

def run_agent(user_message, history):
    """
    user_message : latest user input (string)
    history      : list of previous messages (role/content)
    """

    # Handle budget complaints
    if "expensive" in user_message.lower():
        state.mark_expensive()

    # Build full message list
    messages = [{"role": "system", "content": system_message}]

    for h in history:
        messages.append({
            "role": h["role"],
            "content": h["content"]
        })

    messages.append({"role": "user", "content": user_message})

    # First LLM call
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    # 🔁 Tool-calling loop
    if response.choices[0].finish_reason == "tool_calls":
        assistant_message = response.choices[0].message

        # Add assistant tool-call message
        messages.append(assistant_message)

        # Execute tools
        tool_responses = handling_tool_calls(assistant_message)

        # Add tool responses to conversation
        messages.extend(tool_responses)

        # Call LLM again with tool outputs
        

    stream = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools = [],
        tool_choice="none",
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta

        # ✅ Correct attribute access
        if delta.content:
            yield delta.content


def clear_chat():
    state.reset()
    return [], None, "",None

