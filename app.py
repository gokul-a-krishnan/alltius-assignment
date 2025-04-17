import uuid

import gradio as gr
from rag_agent import chat


def initiate_chat():
    session_id = str(uuid.uuid4())
    return session_id


def chat_with_agent(message, state_data):
    session_id, history = state_data
    response = chat(message, session_id)
    updated_history = history + [(message, response)]
    return "", (session_id, updated_history)


def clear_session():
    new_session_id = initiate_chat()
    return new_session_id, []


# Launch Gradio app
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="Chat History")
    msg = gr.Textbox(label="User Input",
                     placeholder="Type your message here...")
    state = gr.State(())  # (session_id, history)
    clear_button = gr.Button("Clear Chat")

    # On chat message
    msg.submit(chat_with_agent, [msg, state], [msg, state]).then(
        lambda s: s[1], state, chatbot
    )

    # On clear
    clear_button.click(clear_session, None, state, queue=False).then(
        lambda s: s[1], state, chatbot
    )

    # On load
    demo.load(lambda: (initiate_chat(), []), None, state)

demo.launch(server_name="0.0.0.0", server_port=7860)
