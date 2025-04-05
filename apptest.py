import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Website Name", layout="wide")

st.header("Website Name!!")
st.write("Welcome back user")

st.write("Maybe a graph of some sort for demo, we can use data from kaggle")

side_select = st.sidebar.selectbox(
                "What would you like to do?", ("Select Option", "Tax Advice", "Bookkeeping")
                )

if side_select == "Tax Advice":
    st.header("Tax Advice")
    st.write("Use the chatbot in the corner to ask any tax related questions!")
    
""" # Initialize a list to store messages
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
            st.write("This is a response.") """

    # ---- Inject Zapier Chatbot ---- #
    components.html(
    """
    <script async type="module" src="https://interfaces.zapier.com/assets/web-components/zapier-interfaces/zapier-interfaces.esm.js"></script>
    <zapier-interfaces-chatbot-embed is-popup='true' chatbot-id='cm94g0tw4000bgpqe8cnlyjcq'></zapier-interfaces-chatbot-embed>
    """,
    height=0,
    )
