import streamlit as st
from pandas_ai import AI
import pandas as pd

# Function to create a chatbot and get response
def get_chatbot_response(chatbot, message):
    response = chatbot.ask(message)
    return response

def main():
    st.title("CSV Chatbot with PandasAI")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)

        # Create a chatbot
        chatbot = AI(data)

        # Chat interface
        user_input = st.text_input("Ask a question about the data:")

        if user_input:
            # Get the response from the chatbot
            response = get_chatbot_response(chatbot, user_input)
            st.text(f"Response: {response}")

if __name__ == "__main__":
    main()
