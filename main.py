import json
import csv
import timeit

def ler_json(arquivo):
    with open(arquivo) as file:
        return json.load(file)

def ler_csv(arquivo):
    strings_entrada = []
    with open(arquivo) as file:
        entradas = csv.reader(file)
        for linha in entradas:
            strings_entrada.append(linha[0])
    return strings_entrada

def percorrer_automato(estado_inicial, estados_finais, transicoes, entrada):
    estado_atual = estado_inicial
    for caractere in entrada:
        if caractere == ";" or estado_atual == "-1":
            break
        estado_atual = proximo_estado(estado_atual, caractere, transicoes)
    return int(estado_atual) in estados_finais

def proximo_estado(estado_atual, caractere, transicoes):
    if str(caractere) in transicoes[str(estado_atual)]:
        estado_atual = transicoes[str(estado_atual)][str(caractere)]
    else:
        estado_atual = "-1"
    return estado_atual

def main():
    automato = ler_json(r'C:/Users/nicol/OneDrive/Ambiente de Trabalho/trabalho della/ex1.json')
    entradas = ler_csv(r'C:/Users/nicol/OneDrive/Ambiente de Trabalho/trabalho della/testes.csv')

    estado_inicial = automato['initial']
    estados_finais = automato['final']
    transicoes = {}
    for transicao in automato["transitions"]:
        if transicao["from"] not in transicoes:
            transicoes[transicao["from"]] = {transicao["read"]: transicao["to"]}
        else:
            transicoes[transicao["from"]].update({transicao["read"]: transicao["to"]})

    resultados = []
    for entrada in entradas:
        start_time = timeit.default_timer()
        resultado = percorrer_automato(estado_inicial, estados_finais, transicoes, entrada)
        elapsed_time = timeit.default_timer() - start_time
        resultado = 1 if resultado else 0
        resultados.append((entrada, resultado, f"{elapsed_time:.8f}"))

    with open('resultados.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
        for resultado in resultados:
            resultado_final = f"{resultado[0]};{resultado[1]};{resultado[2]}"
            writer.writerow([resultado_final])

if __name__ == "__main__":
    main()