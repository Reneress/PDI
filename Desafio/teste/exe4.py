import cv2

# Crie um objeto VideoCapture para ler o vídeo.
cap = cv2.VideoCapture('surveillance.mpg')

# Verifique se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")

# Defina o codec de vídeo e crie um objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Nota: para mp4, você pode usar 'mp4v'
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640,480)) # Nota: a extensão do arquivo é .mp4

while cap.isOpened():
    # Leia o próximo frame do vídeo
    ret, frame = cap.read()
    if ret:
        # Adicione um quadrado preto ao frame
        start_point = (50, 50)
        end_point = (100, 100)
        color = (0, 0, 0)
        thickness = -1
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

        # Escreva o frame no arquivo de saída
        out.write(frame)

        # Exiba o frame na janela
        cv2.imshow('Frame', frame)

        # Saia se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libere os recursos e feche as janelas
cap.release()
out.release()
cv2.destroyAllWindows()
