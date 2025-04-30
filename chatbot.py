import os
from time import sleep
def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep} {nome}, vale muito a pena aprender python, pois é uma das melhores linguagens de programação atualmente e, também é a que mais cresce do mundo.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} A média salarial de um programador Python pode variar entre R$ 150.000,00 até mais de R$ 300.000,00.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} pra se tornar um analista de dados você precisa estudar alguns temas que são muito relevantes para a profissão.{os.linesep}É preciso se dedicar e estar sempre praticando Python, pois programação envolve estudar mas, tambem praticar muito.{os.linesep}')
    elif resposta == '4':
        print("-------------------------------------------")
        print("Saindo do sistema... Obrigado volte sempre!")
        print("-------------------------------------------")
        return True
    else:
        print("[ERRO!]: Digite uma opção válida!")
    sleep(0.5)
    return False


def start():
    print(f'Olá, seja Bem vindo (a), ao ChatBot do Ryan')

    nome = input('Digite o seu nome: ')

    while True:
        resposta = input(
            f'O que você gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Qual a média salarial de um profissional que trabalha com Python?{os.linesep}[3] - Qual o caminho para se tornar um analista de dados?{os.linesep}[4] - Sair do sistema! {os.linesep}')
        if processar_resposta(resposta, nome):
            break
if __name__ == '__main__':
    start()

