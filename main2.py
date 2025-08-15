import pyautogui
import time

# Defina as posições (x, y) dos três botões

#notebook
iniciar_deteccao_1 = (1819, 370)  # Exemplo de coordenadas do botão 1
excluir_todas_as_ilhas_1 = (1804, 437)  # Exemplo de coordenadas do botão 2
detectar_ilhas_1 = (1892, 393)  # Exemplo de coordenadas do botão 3

#monitor extra
iniciar_deteccao_2 = (1833, -715)  # Exemplo de coordenadas do botão 1
excluir_todas_as_ilhas_2 = (1828, -641)  # Exemplo de coordenadas do botão 2
detectar_ilhas_2 = (1889, -686)  # Exemplo de coordenadas do botão 3

# Tempo entre cada rodada (em segundos)
intervalo = 30

# Número de repetições
repeticoes = 200

# Iniciar Detecção
print("Iniciando Detecção de Ilhas...")
pyautogui.moveTo(iniciar_deteccao_1[0], iniciar_deteccao_1[1])
pyautogui.click()
pyautogui.moveTo(iniciar_deteccao_2[0], iniciar_deteccao_2[1])
pyautogui.click()
time.sleep(intervalo)

for i in range(repeticoes):
    print(f"Rodada {i+1}/{repeticoes}")

    # Clique no botão 1
    pyautogui.moveTo(excluir_todas_as_ilhas_1[0], excluir_todas_as_ilhas_1[1])
    pyautogui.click()
    # Pequeno intervalo entre cliques (opcional)
    time.sleep(0.5)

    pyautogui.moveTo(excluir_todas_as_ilhas_2[0], excluir_todas_as_ilhas_2[1])
    pyautogui.click()

    print("Excluir Ilhas")

    # Pequeno intervalo entre cliques (opcional)
    time.sleep(0.5)

    # Clique no botão 2
    pyautogui.moveTo(detectar_ilhas_1[0], detectar_ilhas_1[1])
    pyautogui.click()
    # Pequeno intervalo entre cliques (opcional)
    time.sleep(0.5)

    pyautogui.moveTo(detectar_ilhas_2[0], detectar_ilhas_2[1])
    pyautogui.click()
    print("Detectando Ilhas...")

    # Espera até a próxima execução
    if i < repeticoes - 1:
        time.sleep(intervalo)
