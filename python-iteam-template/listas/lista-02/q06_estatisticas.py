# =========================
# Arquivo: q06_estatisticas.py
# =========================

import math


def media(dados):
    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia.")

    resultado = sum(dados) / len(dados)
    return round(resultado, 2)


def mediana(dados):
    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia.")

    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    if n % 2 == 0:
        meio1 = dados_ordenados[n // 2 - 1]
        meio2 = dados_ordenados[n // 2]
        resultado = (meio1 + meio2) / 2
    else:
        resultado = dados_ordenados[n // 2]

    return round(resultado, 2)


def moda(dados):
    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia.")

    frequencias = {}

    for numero in dados:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1

    maior_frequencia = max(frequencias.values())

    for numero, freq in frequencias.items():
        if freq == maior_frequencia:
            return round(numero, 2)


def desvio_padrao(dados):
    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia.")

    m = media(dados)

    soma = 0
    for numero in dados:
        soma += (numero - m) ** 2

    variancia = soma / len(dados)
    resultado = math.sqrt(variancia)

    return round(resultado, 2)