import cv2
import numpy as np 
import argparse

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

#Funcao que escreve no terminal as coordenadas e o nivel de cinza do pixel selecionado por um clique do mouse
def position_Grayscale(event, y, x, flags, param):
	global blue, green, red
	if (event == cv2.EVENT_LBUTTONDOWN):
		gray = imagem[x][y][0] 
		print("(X = {}, Y = {}) => Grayscale = [{}]".format(x, y, gray))

#Define qual imagem sera carregada para o codigo
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

imagem = cv2.imread(args["image"])

ver = len(imagem.shape)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow("Image", imagem)

if ver == 2:
	cv2.setMouseCallback("Image", position_Grayscale)
else:
	if Tipo(imagem) == 1:
		cv2.setMouseCallback("Image", position_BGR)
	else:
		cv2.setMouseCallback("Image", position_Grayscale)


cv2.waitKey(0)
cv2.destroyAllWindows()