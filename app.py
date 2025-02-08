import streamlit as st
import time



def main():
    st.set_page_config("Information Retrieval System")
    st.header("Information Retrieval System ")

    with st.sidebar:
        st.title("Menu:")
        pdf_file = st.file_uploader("Upload your PDF file and click on submit", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit"):
            with st.spinner("Processing..."):
                time.sleep(2)
            
                st.success("PDF file uploaded successfully")
            


if __name__ == "__main__":
    main()