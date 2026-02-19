# Deteccion-de-lineas-de-carretera en procesamiento-de-imagenes

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de Procesamiento Digital de Imágenes aplicado a video, cuyo objetivo es el realce y segmentación de las líneas de la carretera como etapa de apoyo para sistemas de conducción autónoma, el sistema procesa un video fotograma por fotograma, aplicando una cadena de operadores punto y operadores regionales diseñados e implementados manualmente por el estudiante, con el propósito de mejorar el contraste y resaltar las marcas viales bajo diferentes condiciones de:

- Iluminación variable

- Cambios de color

- Texturas del asfalto

- Sombras y variaciones ambientales

## Metodología Implementada

El método desarrollado incluye las siguientes etapas fundamentales del Procesamiento Digital de Imágenes:

- Transformación de espacio de color (RGB → HSV)

- Ecualización de histograma sobre el canal de intensidad (V)

- Corrección gamma para ajuste de contraste

- Suavizado espacial mediante kernel definido manualmente

- Definición de Región de Interés (ROI)

- Segmentación por umbral (binarización)

Es importante destacar que no se utilizaron operadores de alto nivel predefinidos de OpenCV para segmentación automática.
Cada etapa fue implementada de manera controlada y justificada teóricamente conforme a los fundamentos académicos del procesamiento digital de imágenes.

## Resultado:

- El sistema genera un video de salida donde:

- Las líneas de la carretera aparecen claramente destacadas en color blanco.

- El resto de la escena permanece en negro.

- Se conserva únicamente la región de interés relevante para análisis vial.

Esto permite obtener una representación limpia y procesada, útil como etapa previa para algoritmos de detección de carriles o visión autónoma.

## Tecnologías Utilizadas

- Python 3

- OpenCV

- NumPy

- Matplotlib

. tqdm (barra de progreso)


Para correr el archivo o el programa se debe hacer a través de la terminal en este caso proporcionando el camino al archivo de video usando el parámetro --video_path. 

Por lo que primero debe poner el python, después incluir la ruta donde esta el archivo .py y seguidamente -v para el llamado del video y después va la ruta del video, para que así pueda también entrar el video y comenzar el progreso, en este caso quedaría la forma quedaría algo así.

PS C:\Users\> python “Ruta del archivo .py” -v “Ruta del video”

Nota: Para que sea mas eficiente ambos archivos deben estar en una misma carpeta. 
