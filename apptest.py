import streamlit as st
import streamlit.components.v1 as components


language= st.selectbox(" Select your preffered language\n"+"Escoge tu lenguage de preferencia", ("English", "Español"))
if language=="English":

    side_select = st.sidebar.selectbox("What would you like to do?", ("Main Page","Tax Advice", "Book keeping"))
    if side_select=="Main Page":
        st.title("Helping Hand")
        st.markdown(" Need help managing your small buisness?\n"+"We can lend you a hand! ")
        
    if side_select=="Tax Advice":
        st.title("Tax Advice")
    if side_select=="Book keeping":
        st.title("Book keeping")
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
if language=="Español":

    side_select = st.sidebar.selectbox(" Que deseas hacer?", ("Pagina Principal","Asesoria de Taxas", "Contabilidad"))
    if side_select=="Pagina Principal":
        st.title("Helping Hand")
        st.markdown("Necesitas ayuda manejando tu nuevo negocio? \n"+" Nostros te podemos echar la mano!")
    if side_select=="Asesoria de Taxas":
        st.title("Asesoria de Taxas")
    if side_select=="Contabilidad":
        st.title("Cotabilidad de tu negocio")
# Initialize a list to store messages
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        # Display existing messages
        for message in st.session_state["messages"]:
            with st.chat_message(message["name"]):
                st.write(message["content"])

        # Get user input
        prompt = st.chat_input("Introduce tu pregunta")

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