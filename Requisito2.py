import cv2
import numpy as np 
import argparse

#Funcao verifica quais pixels devem ser marcados de vermelho em uma imagem preto e branco
def Marcar_Grayscale():
	global marcada
	marcada = cv2.imread(args["image"])
	for add in range(0, 13):
		if (gray + add <= 255):
			marcada[np.where((marcada == [gray + add, gray + add, gray + add]).all(axis = 2))] = [0, 0, 255]
		if (gray - add >= 0):
			marcada[np.where((marcada == [gray - add, gray - add, gray - add]).all(axis = 2))] = [0, 0, 255]

#Funcao verifica quais pixels devem ser marcados de vermelho em uma imagem colorida
def Marcar_colorida():
	global imagem
	BlueSp, GreenSp, RedSp = cv2.split(imagem)

	BlueSp = BlueSp.astype(np.int)
	GreenSp = GreenSp.astype(np.int)
	RedSp = RedSp.astype(np.int)

	width = imagem.shape[1]
	height = imagem.shape[0]

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
	marcada = cv2.subtract(imagem, Remover)
	marcada = cv2.add(marcada, Euclidiana3)
	

#Funcao verifica se a imagem carregada e colorida ou preta e branco. 
def Tipo(original):
	grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
	grayBGR = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)

	difference = cv2.subtract(original, grayBGR)

	BlueDiff, GreenDiff, RedDiff = cv2.split(difference)

	CountB = cv2.countNonZero(BlueDiff)
	CountG = cv2.countNonZero(GreenDiff)
	CountR = cv2.countNonZero(RedDiff)

	if (CountB == 0 and CountG == 0 and CountR == 0):
		verificar = 0	#retorna 0 se for preta e branco
	else:
		verificar = 1	#retorna 1 se for colorida

	return verificar

#Funcao que escreve no terminal as coordenadas e os niveis das cores em RGB do pixel selecionado por um clique do mouse
def position_BGR(event, y, x, flags, param):
	global blue, green, red
	if (event == cv2.EVENT_LBUTTONDOWN):
		blue = imagem[x][y][0]
		green = imagem[x][y][1]
		red = imagem[x][y][2] 
		print("(X = {}, Y = {}) => RGB = [{}  {}  {}]".format(x, y, red, green, blue))
		Marcar_colorida()
		cv2.imshow("Image", marcada)

#Funcao que escreve no terminal as coordenadas e o nivel de cinza do pixel selecionado por um clique do mouse
def position_Grayscale(event, y, x, flags, param):
	global gray
	if (event == cv2.EVENT_LBUTTONDOWN):
		gray = imagem[x][y][0] 
		print("(X = {}, Y = {}) => Grayscale = [{}]".format(x, y, gray))
		Marcar_Grayscale()
		cv2.imshow("Image", marcada)

#Define qual imagem sera carregada para o codigo
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

imagem = cv2.imread(args["image"])

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow("Image", imagem)

if len(imagem.shape) == 2:
	cv2.setMouseCallback("Image", position_Grayscale)
else:
	if Tipo(imagem) == 1:
		cv2.setMouseCallback("Image", position_BGR)
	else:
		cv2.setMouseCallback("Image", position_Grayscale)

key = 0

while key != 27:
	
	key = cv2.waitKey(1)


cv2.destroyAllWindows()