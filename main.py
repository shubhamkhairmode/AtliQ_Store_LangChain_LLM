import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Set Streamlit title and developer details
st.set_page_config(
    page_title="AtliQ Brand Store: Database Q&A 👕",
    page_icon=":Tshirt:",
    layout="wide",
)

# Header
st.title("AtliQ Brand Store: Database Q&A 👕")
st.write("Welcome to the AtliQ Clothing Database Q&A tool.")
st.write("Developed by Shubham Khairmode")
st.write("Contact: shubhambkhairmode@gmail.com")

# User input
question = st.text_input("Ask a Question:")
st.write("Ask any question about the AtliQ Cloathing database.")

if st.button("Get Answer"):
    if question:
        chain = get_few_shot_db_chain()
        response = chain.run(question)

        # Display answer
        st.subheader("Answer:")
        st.write(response)

# Footer
st.write("Thank you for using the AtliQ Brand Store Clothing Database Q&A tool.")
