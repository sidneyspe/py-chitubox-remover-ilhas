import pyautogui
import time

# Defina as posições (x, y) dos dois botões
#notebook
# excluir_todas_as_ilhas = (1804, 437)  # Exemplo de coordenadas do botão 1
# detectar_ilhas = (1892, 393)  # Exemplo de coordenadas do botão 2
#monitor extra
excluir_todas_as_ilhas = (1828, -641)  # Exemplo de coordenadas do botão 1
detectar_ilhas = (1889, -686)  # Exemplo de coordenadas do botão 2

# Tempo entre cada rodada (em segundos)
intervalo = 30

# Número de repetições
repeticoes = 120

for i in range(repeticoes):
    print(f"Rodada {i+1} de {repeticoes}")

    # Clique no botão 1
    pyautogui.moveTo(excluir_todas_as_ilhas[0], excluir_todas_as_ilhas[1])
    pyautogui.click()
    print("Excluir Ilhas")

    # Pequeno intervalo entre cliques (opcional)
    time.sleep(0.5)

    # Clique no botão 2
    pyautogui.moveTo(detectar_ilhas[0], detectar_ilhas[1])
    pyautogui.click()
    print("Detectando Ilhas...")

    # Espera até a próxima execução
    if i < repeticoes - 1:
        time.sleep(intervalo)
