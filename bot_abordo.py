# -*- coding: utf-8 -*-

"""
Bot - Automação de Votos
===================

Descrição:
-----------
Este programa realiza o voto automático na candidata selecionada do reality show "A Bordo". 

Autor:
-------
Ariel Reises @arielreises

Data de Criação:
----------------
19 de dezembro de 2023
"""

# Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

gecko_path = r"C:\Users\User\anaconda3\geckodriver.exe" # Caminho para utilizar o geckodriver
navegador = webdriver.Firefox()                         # Seleção do navegador Mozilla Firefox


# Determinação da Função
def realizar_tarefa(navegador):
    # Seleciona por XPath o elemento desejado
    elemento_opcao = navegador.find_element(By.XPATH, '//*[@id="PDI_answer********"]')
    elemento_opcao.click()                              # Realiza o click
    
    time.sleep(1)                                       # Aguarda 1 segundo após o clique
    
    # Seleciona por XPath o botão de "votar"
    elemento_botao_voto = navegador.find_element(By.XPATH, '//*[@id="pd-vote-button********"]')
    elemento_botao_voto.click()                         # Realiza o click

navegador.get("https://abordoreality.com.br/")          # Abre o site do Reality Show
time.sleep(3)                                           # Aguarda 3 segundos para carregar a página


# Variável de Repetição
num_repeticoes = 10000                                  # Dez mil repetições
for _ in range(num_repeticoes):
    realizar_tarefa(navegador)                          # Realiza a tarefa desejada
    time.sleep(3)                                       # Aguarda 3 segundos
    navegador.refresh()                                 # Atualiza o navegador e repete o processo

# navegador.quit()                                      # Fecha o navegador (mas não está habilitado)