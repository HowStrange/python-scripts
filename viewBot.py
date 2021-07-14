import webbrowser, time

url = input("Coloque a Url: ")
timeSet = input("Quanto tempo para abrir janelas: ")
quantidadeJanelas = input("Número de Janelas")

for i in range(int(quantidadeJanelas)): ## Quantas janelas
    webbrowser.open_new(url) ## Function para abrir janelas
    time.sleep(int(timeSet)) ## Tempo de janelas