import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversation_chain

def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("Reply: ", message.content)

def main():
    st.set_page_config("Information Retrieval System")
    st.header("Information Retrieval System ")

    user_question= st.text_input("Enter your question here:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_file = st.file_uploader("Upload your PDF file and click on submit", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_file)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversation_chain(vector_store)

                
            
                st.success("PDF file uploaded successfully")
            


if __name__ == "__main__":
    main()