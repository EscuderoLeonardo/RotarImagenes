from datetime import datetime
import cv2
import numpy as np

def rotar(img,angulo): # angulo = 90,180,-90
        
    filas, columnas, canales = img.shape
    
    if angulo == 90:
        aux = np.zeros((columnas,filas,canales), dtype=np.uint8)
        
        # Las filas (comenzando desde la ultima y con todas las columnas) de la imagen original pasan a ser la columna i (comenzando desde 0) de la nueva imagen
        # Ej: [0,1,2]               [6,3,0]
        #     [3,4,5]   ------->>   [7,4,1]
        #     [6,7,8]               [8,5,2]
        
        for i in range(filas):
            aux[:,i] = img[filas-1-i,:]

        # Slicing: [inicio:fin:paso]

    elif angulo == 180:
         
        # La fila i (comenzando desde la primera y con todas las columnas) de la imagen original pasan a ser la fila "filas-1-i" de la nueva imagen con las columnas completadas al revez.
        # filas-1-i comenzaria desde la ultima fila hasta la primera
        
        # Ej: [0,1,2]               [8,7,6]
        #     [3,4,5]   ------->>   [5,4,3]
        #     [6,7,8]               [2,1,0]
        
        aux = np.zeros((filas,columnas,canales), dtype=np.uint8)
        for i in range(filas):
            aux[filas-1-i,::-1] = img[i,:]        
                
    elif angulo == -90:
        
        aux = np.zeros((columnas,filas,canales), dtype=np.uint8)
        
        # la columna n (comenzando desde la ultima y con todas las filas) de la imagen original pasa a ser la fila "fil" de la nueva imagen
        # En este caso el for comienza desde la ultima columna, y el indice n se reduce en 1 por cada ciclo, hasta llegar al inicio, es decir 0.

        # Ej: [0,1,2]               [2,5,8]
        #     [3,4,5]   ------->>   [1,4,7]
        #     [6,7,8]               [0,3,6]
        
        fil = 0
        for n in range(columnas-1,-1,-1):
            aux[fil,:] = img[:,n]
            fil +=1
    else:
        return img
    return aux

def mostrar(txt,img,t):
    cv2.namedWindow(txt,cv2.WINDOW_NORMAL)
    cv2.imshow(txt,img)
    cv2.moveWindow(txt,400,100)
    t = cv2.waitKeyEx(0)
    while t not in Lista_teclas:
        if t == 115: # tecla 's'
            now = datetime.now()
            fecha = now.strftime("%Y-%m-%d_%H-%M-%S")
            cv2.imwrite(f'Imagen{fecha}.jpg',img)
        t = cv2.waitKeyEx(0)
    cv2.destroyAllWindows()
    return t

imagen_inicial = cv2.imread('cameraman.jpg')

Lista_teclas = [2424832,2555904,2490368,2621440,113]
#2424832 = flecha izquierda
#2555904 = flecha derecha
#2490368 = flecha arriba
#2621440 = flecha abajo
#113 = q
#115 = s

tecla = mostrar('Imagen original',imagen_inicial,0)

imagen_actual = np.copy(imagen_inicial)

while True:
        
    if tecla == 2555904:  #tecla flecha derecha
        imagen_actual = rotar(imagen_actual,90)
        tecla = mostrar('Imagen',imagen_actual,tecla)
    
    elif tecla == 2424832: # tecla flecha izquierda
        imagen_actual = rotar(imagen_actual,-90)
        tecla = mostrar('Imagen',imagen_actual,tecla)
        
    elif tecla == 2621440 or tecla == 2490368: #flecha arriba o flecha abajo
        imagen_actual = rotar(imagen_actual, 180)
        tecla = mostrar('Imagen',imagen_actual,tecla)

    elif tecla == 113:
        break