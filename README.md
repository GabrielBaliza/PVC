>>O programa foi feito em ambiente Linux Ubuntu 16.04, 64 bits,
utilizando a biblioteca OpenCV 3.4.2 e Python 2.7.12
Também é utilizada a biblioteca NumPy, que é necessária para a execução do programa
Cada requisito do projeto foi separado em um codigo fonte diferente.
Para executa-los basta utilizar o seguinte comando no terminal, na pasta
do arquivo:
Requisito 1: Identificar cor e posição do pixel selecionado
Requisito 2: "Pintar" de vermelho todos os pixels de uma cor próxima ao selecionado de vermelho, em uma imagem
Requisito 3: Mesmo do requisito 2 em um vídeo salvo no computador
Requisito 4: Mesmo do requisito 2 para vídeo da webcam

>>Para os Requisitos 1 e 2:

python Requisito1 --image [Path to image]

e

python Requisito2 --image [Path to image]

Por exemplo:

python Requisito2.py --image ~/Documents/Trabalho1/Gabriel/data/image.jpg

>>Para o Requisito 3:

python Requisito2.py --video [path tp video]

python Requisito3.py --video ~/Documents/Trabalho1/Gabriel/data/video.avi

>>Para o Requisito 4:

python Requisito4.py

Para fechar o programa aperte a tecla ESC
Fechar de outras maneiras pode resultar em erros. Os únicos formatos testados foram .jpg para imagem e .avi para video.

Feito para a matéria Princípios de visão computacional, primeiro semestre de 2019
