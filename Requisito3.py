import cv2
import numpy as np 
import argparse

#Funcao verifica quais pixels devem ser marcados de vermelho em um frame
def Marcar_colorida():
	
	BlueSp, GreenSp, RedSp = cv2.split(frame)

	BlueSp = BlueSp.astype(np.int)
	GreenSp = GreenSp.astype(np.int)
	RedSp = RedSp.astype(np.int)

	width = frame.shape[1]
	height = frame.shape[0]

	SolidBlue = np.zeros((height, width), np.uint8)
	SolidBlue[:] = blue
	SolidBlue = SolidBlue.astype(np.int)

	SolidGreen = np.zeros((height, width), np.uint8)
	SolidGreen[:] = green
	SolidGreen = SolidGreen.astype(np.int)

	SolidRed = np.zeros((height, width), np.uint8)
	SolidRed[:] = red
	SolidRed = SolidRed.astype(np.int)

	BlueSub = np.subtract(SolidBlue, BlueSp)
	GreenSub = np.subtract(SolidGreen, GreenSp)
	RedSub = np.subtract(SolidRed, RedSp)
	
	Euclidiana = np.sqrt(np.add(np.add(np.square(BlueSub), np.square(GreenSub)), np.square(RedSub))) #Distancia euclidiana
	Euclidiana = np.where(Euclidiana < 13, 255, 0)

	Euclidiana = Euclidiana.astype(np.uint8)
	Zeros = np.zeros((height, width), np.uint8)

	Euclidiana3 = cv2.merge((Zeros, Zeros, Euclidiana))
	Remover = cv2.merge((Euclidiana, Euclidiana, Zeros))

	global marcada
	marcada = cv2.subtract(frame, Remover)
	marcada = cv2.add(marcada, Euclidiana3)
	
#Funcao que escreve no terminal as coordenadas e os niveis das cores em RGB do pixel selecionado por um clique do mouse
def position_BGR(event, y, x, flags, param):
	global blue, green, red, click
	if (event == cv2.EVENT_LBUTTONDOWN):
		blue = frame[x][y][0]
		green = frame[x][y][1]
		red = frame[x][y][2] 
		print("(X = {}, Y = {}) => RGB = [{}  {}  {}]".format(x, y, red, green, blue))
		Marcar_colorida()
		click = 1

#Define qual video sera carregado para o codigo
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required = True, help = "Path to the video")
args = vars(ap.parse_args())

video = cv2.VideoCapture(args['video'])

click = 0
key = 0
ret, frame = video.read()

while(video.isOpened()):

	ret, frame = video.read()
	if ret == True:
	
		cv2.imshow("Video", frame)
		cv2.setMouseCallback("Video", position_BGR)

		if click == 1:
			Marcar_colorida()
			cv2.imshow("Video", marcada)

		if cv2.waitKey(25) & 0xFF == 27:
			break

	else:
		break
	

cv2.destroyAllWindows()