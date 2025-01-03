import streamlit as st

st.title("Application Streamlit Bac 3 EMI !")
st.write("Ceci est une application Streamlit exécutée sur Windows.")
ab = st.number_input("Entrez un nombre :")
al =st.button("Cliquez ici")

if al:
    st.write('Je suis etudiant et la valeur saisi estp')
    st.write("J'ai", ab)
