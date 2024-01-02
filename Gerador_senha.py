import secrets
import string
from time import sleep

def validar_senha_gerada(tamanho_senha, senha, elementos_senha):
    verifica_senha = []

    for letra in senha:
        for opc in elementos_senha:
            if opc == 'maiuscula':
                if letra in string.ascii_uppercase:
                    verifica_senha.append('maiuscula')
            elif opc == 'minuscula':
                if letra in string.ascii_lowercase:
                    verifica_senha.append('minuscula')
            elif opc == 'numero':
                if letra in string.digits:
                    verifica_senha.append('numero')
            else:
                if letra in string.punctuation:
                    verifica_senha.append('simbolo')

    if set(elementos_senha) == set(verifica_senha):
        print("Senha criada: ", senha)
    else:
        gerar_senha(tamanho_senha, elementos_senha)

def gerar_senha(tamanho_senha, elementos_senha):
    caracteres_concatenados = ''

    for opcao in elementos_senha:
        if opcao == 'maiuscula':
            caracteres_concatenados += string.ascii_uppercase
        elif opcao == 'minuscula':
            caracteres_concatenados += string.ascii_lowercase
        elif opcao == 'numero':
            caracteres_concatenados += string.digits
        else:
            caracteres_concatenados += string.punctuation

    senha = ''.join(secrets.choice(caracteres_concatenados) for i in range(tamanho_senha))
    validar_senha_gerada(tamanho_senha, senha, elementos_senha)

def personalizar_senha():
    opcao_escolhida = [] # captura todas as escolhas do usuario
    elementos_senha = [] # armazena apenas os elementos que irão compor a senha

    tamanho_senha = int(input("Tamanho da senha? [Mínimo: 4]. Sua resposta: "))

    if tamanho_senha < 4:
        print("O tamanho da sua senha é inferior a 4. \nPor padrão iremos alterar o tamanho da sua senha.")
        tamanho_senha = 4

    sleep(1)
    print("Atenção, usuário! \nIremos considerar como 'Sim' se você apertar 'S' ou qualquer letra (exceto 'N'). \
          \nIremos considerar como 'Não' somente se você apertar 'N'.")

    sleep(2)
    while(True): 
        conter_letra_maiuscula = input("Conter letra maiúscula? Sua resposta: ").upper()
        conter_letra_minuscula = input("Conter letra minúscula? Sua resposta: ").upper()
        conter_numero = input("Conter número? Sua resposta: ").upper()
        conter_simbolo = input("Conter símbolo? Sua resposta: ").upper()

        opcao_escolhida = [conter_letra_maiuscula, conter_letra_minuscula, conter_numero, conter_simbolo]

        if conter_letra_maiuscula == 'N' and conter_letra_minuscula == 'N' and conter_numero == 'N' and conter_simbolo == 'N' :
            print("Você precisa escolher ao menos um item para que possamos gerar sua senha.")
        else:
            for pos, opcao in enumerate(opcao_escolhida):
                if opcao != 'N':
                    if pos == 0:    
                        elementos_senha.append("maiuscula")
                    elif pos == 1:
                        elementos_senha.append("minuscula")
                    elif pos == 2:
                        elementos_senha.append("numero")
                    else:
                        elementos_senha.append("simbolo")
            break                         

    gerar_senha(tamanho_senha, elementos_senha)

if __name__ == "__main__":
    personalizar_senha()

        

