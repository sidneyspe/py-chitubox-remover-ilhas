import pyautogui
import time

# Defina as posições (x, y) dos três botões

#notebook
btn_fatiar = (2226,19)
btn_fatiar_2 = (2453,969)

iniciar_deteccao = (1182, 81)  # Exemplo de coordenadas do botão 1
excluir_todas_as_ilhas = (2467, 193)  # Exemplo de coordenadas do botão 2
detectar_ilhas = (2523, 115)  # Exemplo de coordenadas do botão 3

#monitor extra
# iniciar_deteccao = (1833, -715)  # Exemplo de coordenadas do botão 1
# excluir_todas_as_ilhas = (1828, -641)  # Exemplo de coordenadas do botão 2
# detectar_ilhas = (1889, -686)  # Exemplo de coordenadas do botão 3

# Tempo entre cada rodada (em segundos)
intervalo = 5

# Número de repetições
repeticoes = 300

pyautogui.moveTo(btn_fatiar[0], btn_fatiar[1])
pyautogui.click()

pyautogui.moveTo(btn_fatiar_2[0], btn_fatiar_2[1])
pyautogui.click()
time.sleep(30)

# Iniciar Detecção
print("Iniciando Detecção de Ilhas...")
pyautogui.moveTo(iniciar_deteccao[0], iniciar_deteccao[1])
pyautogui.click()
time.sleep(intervalo)

for i in range(repeticoes):
    print(f"\nRodada {i+1}/{repeticoes}")

    # Clique no botão 1
    pyautogui.moveTo(excluir_todas_as_ilhas[0], excluir_todas_as_ilhas[1])
    pyautogui.click()
    print("Excluir Ilhas")

    # Pequeno intervalo entre cliques (opcional)
    # time.sleep(0.5)

    # Clique no botão 2
    pyautogui.moveTo(detectar_ilhas[0], detectar_ilhas[1])
    pyautogui.click()
    print("Detectando Ilhas...")

    # Espera até a próxima execução
    if i < repeticoes - 1:
        time.sleep(intervalo)
