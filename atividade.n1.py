from random import randint
movimentos= 0
casa = 1
venceu = 0
jogada= 0

while venceu == 0:
	if movimentos >= 6:
		print("Você atingiu o limite de movimentos!")
		break;
	else:
		while casa == 1 and movimentos <7:
			print("Você esta na casa: ",casa)
			print("Você ainda tem", 7-movimentos,"movimentos")
			print("Escolha seu caminho:")
			print("[1]- Caminho vermelho")
			print("[2]- Caminho preto")
			jogada = int(input(""))
			print("")
			if jogada == 1:
				casa = 2
				movimentos = movimentos+1
				break;
