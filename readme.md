# Clasificación de Imágenes con MobileNetV2

## Descripción

Esta aplicación utiliza **MobileNetV2**, un modelo de deep learning preentrenado en el dataset **ImageNet**, para clasificar imágenes en más de 1,000 categorías diferentes. Se trata de una herramienta educativa diseñada para ayudar a los estudiantes a desarrollar su vocabulario a través de la interacción visual y auditiva con imágenes.

https://eduimageclassifier-testing.streamlit.app/

## Características

- **Clasificación de imágenes**: Permite subir imágenes y predice las categorías más probables.
- **Retroalimentación auditiva**: El modelo no solo muestra las predicciones, sino que también proporciona una opción para escuchar las predicciones.
- **Interfaz amigable**: Desarrollada con Streamlit para ofrecer una experiencia de usuario sencilla y directa.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone github.com/cagmspain/EduImageClassifier
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## Requisitos

- Python 3.0
- TensorFlow 2.0
- Streamlit
- Pillow
- gTTS (opcional, para la retroalimentación auditiva)

## Uso

1. Ejecuta la aplicación y carga una imagen.
2. El modelo clasificará la imagen en una o más categorías.
3. Opcional: Reproduce el audio con las predicciones.

## Futuras mejoras

- Ajustar el modelo para casos de uso específicos.
- Implementar una interfaz más interactiva.
- Añadir soporte para otros idiomas en la retroalimentación auditiva.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un _issue_ o envía un _pull request_ con tus sugerencias.
