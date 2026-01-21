# Deteccion-de-lineas-de-carretera en procesamiento-de-imagenes

Proyecto de Procesamiento Digital de Imágenes aplicado a video, cuyo objetivo es el realce y segmentación de las líneas de la carretera para apoyar sistemas de conducción autónoma. El sistema procesa un video fotograma por fotograma y aplica una cadena de operadores punto y regionales diseñados e implementados por el estudiante, con el fin de mejorar el contraste y resaltar las marcas viales bajo diferentes condiciones de iluminación, color y textura del asfalto.

El método incluye transformaciones de espacio de color, ecualización de histograma, corrección gamma, suavizado espacial mediante kernels definidos manualmente, selección de región de interés (ROI) y binarización, sin hacer uso de operadores de alto nivel predefinidos en OpenCV. Como resultado, el sistema genera un video de salida en el que las líneas de la carretera se encuentran claramente destacadas en color blanco, mientras que el resto de la escena permanece en negro.

Este proyecto fue desarrollado en Python utilizando OpenCV, NumPy y Matplotlib, cumpliendo con los criterios académicos del procesamiento digital de imágenes y priorizando la claridad, modularidad y justificación teórica de cada etapa del proceso.
