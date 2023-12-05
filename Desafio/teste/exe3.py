import cv2

# Crie um objeto VideoCapture para ler o vídeo.
cap = cv2.VideoCapture('surveillance.avi')

# Verifique se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = 30
# Perform background accumulation and subtraction


# background = background.astype(float)

# Defina o codec de vídeo e crie um objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output1.avi', fourcc, frame_rate, (frame_width, frame_height),0)

alpha = 0.95
theta = 0.1
ret, frame = cap.read()
background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
    # Leia o próximo frame do vídeo
    ret, frame = cap.read()
    if ret:
        # Converta o frame para escala de cinza
        imgcur = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Converta o frame para float
        #imgcur = imgcur.astype(float)
        # Atualize o background
        background = alpha * background + (1 - alpha) * imgcur
        # Calcule a diferença entre o frame atual e o background
        diffImg = abs(imgcur - background)
        # Aplique o limiar
        ret, threshImg = cv2.threshold(diffImg, theta, 255, cv2.THRESH_BINARY)
        # Escreva o frame no arquivo de saída
        
       

        # Exiba o frame na janela
        cv2.imshow('Frame', frame)
        cv2.imshow('Background', background.astype('uint8'))
        cv2.imshow('Difference', diffImg.astype('uint8'))
        cv2.imshow('Thresholded Difference', threshImg.astype('uint8'))
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(diffImg.astype('uint8'))
        # Saia se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libere os recursos e feche as janelas
cap.release()
out.release()
cv2.destroyAllWindows()
