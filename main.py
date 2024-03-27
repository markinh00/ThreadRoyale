# THREAD ROYALE

import random
from personagem import Personagem

# Criando os personagens
personagens = []
nomes = ["Siegfried", "Merlin", "Thor", "Aragorn"]
habilidades = ["vampirismo", "comum", "encegamento", "ladino", "veloz", "tanque", "forte"]
for nome in nomes:
    vida = random.randint(80, 125)
    dano = random.randint(10, 20)
    velocidade = random.randint(1, 2) if vida > 100 else random.randint(2, 3)
    precisao_max = min(90, 100 - dano)
    precisao = random.randint(70, precisao_max)

    # Criando e retornando o personagem
    personagem = Personagem(nome=nome,
                            vida=vida,
                            dano=dano,
                            velocidade=velocidade,
                            accuracy=precisao,
                            habilidade=random.choice(habilidades))
    personagens.append(personagem)

Personagem.lista_personagens = personagens

for personagem in personagens:
    personagem.imprimir_status()

# Iniciando a batalha
for personagem in personagens:
    personagem.start()

# Esperando até que todos os personagens terminem a batalha
for personagem in personagens:
    personagem.join()

print("Battle Royale encerrado.")
