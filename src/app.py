import streamlit as st 

st.title('Suma tres números')

st.write("## Usando `st.number_input`")

n1 = st.number_input("Primer sumando: ", step=1)
n2 = st.number_input("Segundo sumando: ", step=1)
n3 = st.number_input("Tercer sumando: ", step=1)

st.write(f"La suma de los tres números es: {n1 + n2 + n3} :sunglasses:")

st.divider()

st.write("## Usando `st.slider`")

s1 = st.slider("Primer sumando: ")
s2 = st.slider("Segundo sumando: ")
s3 = st.slider("Tercer sumando: ")

st.write(f"La suma de los tres números es: {s1 + s2 + s3} :ok_hand:")