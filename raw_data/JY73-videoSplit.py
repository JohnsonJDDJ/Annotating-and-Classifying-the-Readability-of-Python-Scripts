import numpy as np
import cv2

import base64

def video_split(contents):
    url = '../data/data.mp4'
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)

    fh = open(url, "wb")
    fh.write(decoded)
    fh.close()
    print("Data upload")

    print("Start process video")

    # Cargamos video
    video = cv2.VideoCapture(url)

    # Meta datos del video
    n_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fs_actual = int(video.get(cv2.CAP_PROP_FPS))

    # Tamaño de paso de la ventana para remuestreo 
    muestra = int(n_frame/37)

    # crear el objeto video
    #fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    #out = cv2.VideoWriter("./datos/1_nuevo_37fps.mp4", fourcc, 10, (192,192))

    # Nuevas dimenciones del video 
    nuevo_ancho = 192
    nuevo_alto = 192

    # Variables para la extracion de muestras
    contador = 0
    contador_muestras = 0
    i = int(np.random.randint(low=0, high=muestra))

    # Bucle principal
    images = []
    while True:
        ret, frame = video.read()
        if not ret:
            break

        if contador_muestras == 37:
            break
        else:
            ventana_muestra = (contador_muestras*muestra) + i
            if contador == ventana_muestra:
                # Nuevo frame seleccionado
                nuevo_cuadro = cv2.resize(frame, (nuevo_ancho, nuevo_alto))
                images.append(nuevo_cuadro)

                # Restablecemos los valores para una nueva muestra 
                i = int(np.random.randint(low=0, high=muestra))
                contador_muestras = contador_muestras+1
        
        contador = contador+1

    # liberamos recursos
    video.release()

    images = np.array(images)
    np.save("../data\data_array", images)
    print("end process video")