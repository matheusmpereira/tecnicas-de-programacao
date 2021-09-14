from random import randint
movimentos= 0
casa = 1
venceu = 0
jogada= 0
while venceu == 0:
	while jogadas< 7:
		print("Voce esta na sala:",sala)
		print("jogadas restantes:",7-jogadas)
		print("Escolha seu caminho:")
		print("[1] - Caminho vermelho")
		print("[2] - Caminho preto")
		escolha = int(input(""))
		break;
