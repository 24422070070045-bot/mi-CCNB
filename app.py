import streamlit as st

st.set_page_config(page_title="Café Central", page_icon="☕")

st.markdown("<h1 style='text-align: center; color: #6f4e37;'>☕ Café Central</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8d6e63;'>¡Bienvenidos! Elige una opción.</p>", unsafe_allow_html=True)

opcion = st.radio("Menú de opciones:", ["🗓️ Apartados", "⭐ Calificar", "📋 Sugerencias"])

if opcion == "🗓️ Apartados":
    st.subheader("Reservar Mesa o Pedido")
    nombre = st.text_input("Tu Nombre:")
    detalles = st.text_area("¿Qué deseas apartar?")
if st.button("Enviar Apartado"):
    st.success(f"¡Gracias {nombre}! Apartado registrado.")

elif opcion == "⭐ Calificar":
    st.subheader("Califica nuestra atención")
    estrellas = st.slider("Estrellas", 1, 5, 5)
if st.button("Enviar Calificación"):
    st.success("¡Gracias por calificar!")

elif opcion == "📋 Sugerencias":
    st.subheader("¿Qué te gustaría en el Menú?")
    antojo = st.text_area("Escribe aquí:")
if st.button("Enviar Sugerencia"):
    st.success("¡Idea recibida!")

