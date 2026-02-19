import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm 

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--video_path", required=True, help="path to video file")
args = vars(parser.parse_args())

capture = cv2.VideoCapture(args["video_path"])

if not capture.isOpened():
    print("Error del inicio del video")
    exit()

fps = int(capture.get(cv2.CAP_PROP_FPS)) 
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter("Salida.MP4", fourcc, fps, (width, height))

ret, frame = capture.read()

def crear_mascara_rectangular(frame, x1, y1, x2, y2):
    mask = np.zeros_like(frame) 
    cv2.rectangle(mask, (x1, y1), (x2, y2), (255, 255, 255), -1)
    return mask

x1, y1 = 310, 420
x2, y2 = 1280, 660
mascara_rectangular = crear_mascara_rectangular(frame, x1, y1, x2, y2)

def recorte(image, x1, y1, x2, y2):
    return image[y1:y2, x1:x2]

def eq(image):
    H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_RGB2HSV))
    eq_V = cv2.equalizeHist(V)
    image_eq = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2RGB)
    return image_eq    

def sat_gamma(image, gamma=0.9):
    image_RGB_gamma = np.array(255 * (image / 255) ** gamma, dtype='uint8')
    return image_RGB_gamma

def suav(image):
    kernel = np.array([
        [6, 12, 6],
        [12, 24, 12],
        [6, 12, 6]
    ], dtype=np.float32) * float(1 / 96)
    output = cv2.filter2D(image, -1, kernel)
    return output

def trasf1(frame):
    frame = eq(frame)
    frame = cv2.bitwise_and(frame, mascara_rectangular)
    frame = sat_gamma(frame)
    frame = suav(frame)
    return frame

def trasf2(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ath = 200 
    output = np.where(frame_gray >= ath, 255, 0).astype(np.uint8)
    return output

frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
progress_bar = tqdm(total=frame_count, desc="Procesando fotogramas", unit="fotograma", dynamic_ncols=True)

while capture.isOpened():
    ret, frame = capture.read()
    
    if not ret:
        print("\nVideo finalizado. Cerrando programa automáticamente...")
        break  
        
    cv2.imshow('Original Frame', frame) 
    frame_t1 = trasf1(frame) 
    cv2.imshow('Procesado', frame_t1)
    Eframe = trasf2(frame_t1) 
    Eframe_recortado = recorte(Eframe, x1, y1, x2, y2) 
    cv2.imshow('Resultado Final', Eframe_recortado)  
    out.write(Eframe_recortado) 
        
    out.write(Eframe_recortado)

    key = cv2.waitKey(1) & 0xFF
    print(f"\rTecla presionada: {chr(key) if 32 <= key <= 126 else key}  ", end="")  

    if key == ord("z"): 
        print("\nTecla 'z' detectada. Saliendo...")
        break

    progress_bar.update(1)

progress_bar.close()
capture.release()
out.release()
cv2.destroyAllWindows()

print(" Programa finalizado correctamente.")



