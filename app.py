import streamlit as st
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from gtts import gTTS
import os

# Configuración de la página
st.set_page_config(
    page_title="Clasificación de Imágenes",
    page_icon="🤖",  # Emoji de robot
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar el modelo preentrenado
model = MobileNetV2(weights='imagenet')

# Función para predecir
def predict_image(img):
    if img.mode != "RGB":  # Asegurarse de que la imagen esté en RGB
        img = img.convert("RGB")
    img = img.resize((224, 224))  # Redimensionar la imagen
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Predicción
    preds = model.predict(img_array)
    return decode_predictions(preds, top=3)[0]

# Función para convertir texto a audio y reproducirlo
def play_audio(text, filename="prediction.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"afplay {filename}")  # Comando para reproducir audio en macOS

# Sidebar con menú de información
st.sidebar.title("Información del Proyecto")

st.sidebar.markdown("### Sobre el modelo")
st.sidebar.markdown("""
Este proyecto utiliza **MobileNetV2** para la clasificación de imágenes.
El modelo fue preentrenado con el conjunto de datos **ImageNet**, que contiene más de 1 millón de imágenes y 1,000 categorías diferentes.
""")

# Mostrar precisión del modelo
st.sidebar.markdown("### Precisión del modelo")
st.sidebar.markdown("**Precisión top-1:** 71.8%\n\n**Precisión top-5:** 91.0%")

# Categorías del modelo
st.sidebar.markdown("### Categorías del modelo")
st.sidebar.markdown("""
El modelo puede clasificar imágenes en las siguientes categorías:
- Animales (perros, gatos, leones, etc.)
- Vehículos (coches, camiones, bicicletas)
- Objetos cotidianos (relojes, computadoras, teclados)
- Electrodomésticos y más...
""")

# Interfaz de usuario
st.title('Clasificación de Imágenes con MobileNetV2')
st.write("Sube una imagen y el modelo predecirá la categoría.")

# Objetivo de la aplicación
st.markdown("""
### Objetivo de la Aplicación:
El objetivo principal de esta aplicación es **identificar objetos, animales, personas, y otros elementos visuales** a través de imágenes, proporcionando una respuesta tanto visual como auditiva. 
Esta funcionalidad está diseñada para **contribuir al desarrollo del lenguaje de los estudiantes**, permitiéndoles interactuar con el mundo visual mientras reciben una **retroalimentación auditiva** que refuerza el aprendizaje de nuevos términos y conceptos.
""")

# Cargar imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    
    # Mostrar imagen y predicciones
    st.image(img, caption='Imagen subida', use_column_width=True)
    st.write("Realizando predicción...")
    predicciones = predict_image(img)
    
    # Mostrar resultados
    st.write("Predicciones:")
    for pred in predicciones:
        pred_text = f"{pred[1]} con {round(pred[2] * 100, 2)}% de probabilidad"
        st.markdown(f"<h4 style='color: green;'>{pred_text}</h4>", unsafe_allow_html=True)
        
        # Añadir botón para reproducir audio
        if st.button(f"Reproducir audio para {pred[1]}"):
            play_audio(pred_text)

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Esta aplicación usa el modelo MobileNetV2 preentrenado para clasificar imágenes en más de 1000 categorías.</p>", unsafe_allow_html=True)
