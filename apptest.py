import streamlit as st

st.header("Website Name!!")

side_select = st.sidebar.selectbox("What would you like to do?", ("Tax Advice", "Bookkeeping"))

if side_select == "Tax Advice":
    st.header("Tax Advice")

# Initialize a list to store messages
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display existing messages
    for message in st.session_state["messages"]:
        with st.chat_message(message["name"]):
            st.write(message["content"])

    # Get user input
    prompt = st.chat_input("Enter your message")

    # Process user input
    if prompt:
        st.session_state["messages"].append({"name": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Add a placeholder for the AI response
        with st.chat_message("assistant"):
            st.write("...")

        #  Simulate a response (replace with your logic)
        st.session_state["messages"].append({"name": "assistant", "content": "This is a response."})
        with st.chat_message("assistant"):
            st.write("This is a response.")