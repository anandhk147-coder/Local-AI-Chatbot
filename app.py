import streamlit as st
from ollama import chat

st.set_page_config(
    page_title="Local AI Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Local AI Chatbot")
st.caption("Powered by Ollama + Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = chat(
                model="qwen2.5:1.5b",
                messages=st.session_state.messages,
            )

            answer = response["message"]["content"]

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# Sidebar
st.sidebar.title("Options")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.info(
    """
    **Model:** qwen2.5:1.5b

    Running locally using Ollama.
    """
)