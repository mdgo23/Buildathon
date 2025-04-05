import streamlit as st

st.header("Website Name!!")
st.write("Welcome back user")

st.write("Maybe a graph of some sort for demo, we can use data from kaggle")

side_select = st.sidebar.selectbox(
                "What would you like to do?", ("Select Option", "Tax Advice", "Bookkeeping")
                )

if side_select == "Tax Advice":
    st.header("Tax Advice")

if side_select == "Bookkeeping":
    st.header("Bookkeeping")

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