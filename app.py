import streamlit as st
import os

# Nombre del archivo interno donde se guardará todo
ARCHIVO_DATOS = "registro_pedidos.txt"

# Función para guardar los datos en el archivo
def guardar_datos(tipo, nombre, contenido):
with open(ARCHIVO_DATOS, "a", encoding="utf-8") as f:
f.write(f"[{tipo}] | Nombre: {nombre} | Detalle: {contenido}\n")

st.title("Reservar Mesa o Pedido")

# Menú para los clientes
opcion = st.radio("Menú de opciones:", ["📅 Apartados", "⭐ Calificar", "📋 Sugerencias"])

if opcion == "📅 Apartados":
    nombre = st.text_input("Tu Nombre:")
    detalles = st.text_area("¿Qué deseas apartar?")

if st.button("Enviar Apartado"):
if nombre and detalles:
    guardar_datos("APARTADO", nombre, detalles)
    st.success(f"¡Gracias {nombre}! Apartado registrado en la app con éxito.")
else:
    st.error("Por favor, llena todos los campos.")

elif opcion == "⭐ Calificar":
nombre_calif = st.text_input("Tu Nombre:")
estrellas = st.slider("Calificación:", 1, 5, 5)
comentario = st.text_area("Comentario adicional:")

if st.button("Enviar Calificación"):
if nombre_calif:
guardar_datos("CALIFICACIÓN", nombre_calif, f"{'⭐' * estrellas} - {comentario}")
st.success("¡Gracias por tu calificación!")
else:
st.error("Por favor, pon tu nombre.")

elif opcion == "📋 Sugerencias":
sugerencia = st.text_area("Escribe tu sugerencia:")

if st.button("Enviar Sugerencia"):
if sugerencia:
guardar_datos("SUGERENCIA", "Anónimo", sugerencia)
st.success("¡Gracias por ayudarnos a mejorar!")
else:
st.error("El campo de sugerencia no puede estar vacío.")

# --- SECCIÓN SECRETA SOLO PARA TI ---
st.markdown("---")
with st.expander("🔑 Modo Administrador (Ver pedidos guardados)"):
contrasena = st.text_input("Introduce la contraseña para ver los datos:", type="password")

# Puedes cambiar "1234" por la contraseña que tú quieras
if contrasena == "1234":
st.subheader("📋 Lista de Pedidos y Mensajes Recibidos:")

if os.path.exists(ARCHIVO_DATOS):
with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
lineas = f.readlines()

if lineas:
for linea in reversed(lineas): # Muestra los más nuevos primero
st.text(linea.strip())
else:
st.info("Aún no hay mensajes registrados.")
else:
st.info("Aún no hay mensajes registrados.")
elif contrasena != "":
st.error("Contraseña incorrecta")

