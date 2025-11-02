iimport streamlit as st
import google.generativeai as genai
import os

# Show title and description.
st.title("💬 Chatbot (Gemini)")
st.write(
    "This is a simple chatbot that uses Google's Gemini Pro model to generate responses. "
    "To use this app, you need to provide a Gemini API key, which you can get [here](https://aistudio.google.com/app/apikey). "
)

# Ask user for their Gemini API key via `st.text_input`.
gemini_api_key = st.text_input("Gemini API Key", type="password")
if not gemini_api_key:
    st.info("Please add your Gemini API key to continue.", icon="🗝️")
else:
    # Set API key for Gemini SDK
    genai.configure(api_key=gemini_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message.
    if prompt := st.chat_input("What is up?"):
        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call Gemini API
        # Convert chat history for Gemini format
        history = []
        for m in st.session_state.messages[:-1]:
            if m["role"] == "user":
                history.append({"role": "user", "parts": [m["content"]]})
            elif m["role"] == "assistant":
                history.append({"role": "model", "parts": [m["content"]]})

        # Create Gemini chat model
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=history)

        # Generate response
        response = chat.send_message(prompt)
        gemini_response = response.text

        # Streamlit表示と履歴保存
        with st.chat_message("assistant"):
            st.markdown(gemini_response)
        st.session_state.messages.append({"role": "assistant", "content": gemini_response})
