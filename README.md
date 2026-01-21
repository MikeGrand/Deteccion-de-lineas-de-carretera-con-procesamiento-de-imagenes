# Deteccion-de-lineas-de-carretera en procesamiento-de-imagenes

Proyecto de Procesamiento Digital de Imágenes aplicado a video, cuyo objetivo es el realce y segmentación de las líneas de la carretera para apoyar sistemas de conducción autónoma. El sistema procesa un video fotograma por fotograma y aplica una cadena de operadores punto y regionales diseñados e implementados por el estudiante, con el fin de mejorar el contraste y resaltar las marcas viales bajo diferentes condiciones de iluminación, color y textura del asfalto.

El método incluye transformaciones de espacio de color, ecualización de histograma, corrección gamma, suavizado espacial mediante kernels definidos manualmente, selección de región de interés (ROI) y binarización, sin hacer uso de operadores de alto nivel predefinidos en OpenCV. Como resultado, el sistema genera un video de salida en el que las líneas de la carretera se encuentran claramente destacadas en color blanco, mientras que el resto de la escena permanece en negro.

Este proyecto fue desarrollado en Python utilizando OpenCV, NumPy y Matplotlib, cumpliendo con los criterios académicos del procesamiento digital de imágenes y priorizando la claridad, modularidad y justificación teórica de cada etapa del proceso.

Para correr el archivo o el programa se debe hacer a través de la terminal en este caso proporcionando el camino al archivo de video usando el parámetro --video_path. 

Por lo que primero debe poner el python, después incluir la ruta donde esta el archivo .py y seguidamente -v para el llamado del video y después va la ruta del video, para que así pueda también entrar el video y comenzar el progreso, en este caso quedaría la forma quedaría algo así.

PS C:\Users\> python “Ruta del archivo .py” -v “Ruta del video”

Nota: Para que sea mas eficiente ambos archivos deben estar en una misma carpeta. 
