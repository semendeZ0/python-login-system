from time import sleep
import random
# usar para config de redefinição de usuário:
n = 0
tentativa = 3
usuario = []
nome = []
sexo = []
senha = []

def redefinir():
    print('Opa! Você quer redefinir o que exatamente?')
    print('[ 1 ] Redefinir nome\n[ 2 ] Redefinir usuário\n[ 3 ] Redefinir senha')
    resposta3 = str(input('SUA RESPOSTA: '))
    if resposta3 == '1':
        resposta_nome2 = str(input('Para qual nome deseja redefinir?\nSua resposta: '))
        nome[0] = resposta_nome2
        print('PROCESSANDO...')
        carregamento()
        print('Prontinho, {} !'.format(*nome))
        print('\033[35mVoltando...\033[m')
        sleep(2)
    elif resposta3 == '2':
        resposta_usuario2 = str(input('Qual seu novo nome de usuário? @'))
        usuario[0] = resposta_usuario2
        print('PROCESSANDO...')
        carregamento()
        print('\033[32mProntinho! Seu novo nome de usuário é:\033[m {}'.format(*usuario))
        print('\033[35mVoltando...\033[m')
        sleep(2)
    elif resposta3 == '3':
        print('Certo! Vamos trocar sua senha.')
        antiga_senha = ''
        global tentativa
        while True:
            antiga_senha = str(input('Digite sua antiga senha: '))
            if antiga_senha == senha[0]:
                break
            tentativa -= 1
            print('\033[31mParece que você digitou algo errado...\033[m\nTente novamente: ')
            print('Você tem mais {} tentativas.'.format(tentativa))
            if tentativa == 0:
                print('Infelizmente não poderemos trocar a sua senha...')
                print('Retornando...')
                sleep(2)
                return 
        nova_senha = str(input('Digite a nova senha: '))
        senha[0] = nova_senha
        print('PROCESSANDO...')
        carregamento()
        print('\033[32mSENHA ALTERADA COM SUCESSO! [✓]\033[m')
        print('\033[35mVoltando...\033[m')
        sleep(2)
# usar para carregar algo: 
def carregamento():
    etapas = ['⬜⬜⬜⬜', '🟦⬜⬜⬜', '🟦🟦⬜⬜', '🟦🟦🟦⬜', '🟦🟦🟦🟦']
    for status in etapas:
        print(f'\r{status}', end='', flush=True)
        sleep(1)

while n == 0:
    print("Seja bem-vindo!")
    print('-' * 10)
    resposta = str(input(('Sua primeira vez aqui[S/N]? '))).strip().upper()[0]
    if resposta == 'S':
        print('Ficamos lisonjeados em ter você aqui!\nPermita-me explicar:\nEste programa está em fase beta. Caso encontre algum bug, relate ao Dev!\nSem mais enrolações, vamos começar! :D')
        resposta_nome = str(input('Antes de tudo, me diga... qual é o seu nome? ')).capitalize().strip()
        print('...')
        nome.append(resposta_nome)
        sleep(2)
        print('Muito prazer, \033[34m{}\033[m !'.format(*nome))
        resposta_sexo = str(input('Qual seu sexo[M/F]? ')).upper().strip()
        while resposta_sexo != 'M' and resposta_sexo != 'F':
            resposta_sexo = str(input('\033[31mParece que você digitou algo errado... acontece haha!\033[m\nVamos tentar de novo:\nQual seu sexo[M/F]? ')).upper().strip()
        sexo.append(resposta_sexo)
        print('Show!\nAgora me diz... Quer criar um nome de usuário próprio\nou quer prosseguir com seu nome mesmo? :)')        
        resposta_pergunta = ''
        while resposta_pergunta != 'NOME' and resposta_pergunta != 'CRIAR':
            resposta_pergunta = str(input('responda aqui\033[33m[CRIAR/NOME]\033[m: ')).upper().strip()
            if resposta_pergunta != 'NOME' and resposta_pergunta != 'CRIAR':
                print('\033[31mParece que você digitou algo errado...\033[m\nPor favor:')
        if resposta_pergunta == 'CRIAR':
            print('Tudo certo!')
            resposta_usuario = str(input('Como deverá ser seu usuário? @'))
            usuario.append(resposta_usuario)
        elif resposta_pergunta == 'NOME':
            usuario.append(nome[0])
        else:
            print('Ih, deu erro... parece que você digitou algo errado.')
        print("Perfeito, @{} !".format(*usuario))
        print('Vamos definir a sua senha agora, tá bom?\nPode pôr qualquer coisa!')
        resposta_senha = str(input('Crie a senha: '))        
        senha.append(resposta_senha)
        print('-' * 10)
        carregamento()
        print('\033[32mCadastro concluído!\033[m')
        print('-=-' * 10)
        print('Antes de voltar, por favor, confira suas informações:')
        print('-' * 10)
        print('NOME: {}\nUSUÁRIO: {}\nSEXO: {}'.format(*nome, *usuario, *sexo))
        print('-' * 10)
        sleep(3)
        resposta2 = str(input('Elas estão corretas[S/N]? ')).upper().strip()[0]
        sleep(1)
        if resposta2 == 'S':
            print('Ótimo! vou te levar para o inicio novamente.\nAgora você pode fazer login e aproveitar o que tem aqui! :)\nÉ pouca coisa, mas é uma forma de agradecer a paciência de nos ajudar a testar o programa! Divirta-se :)')
            sleep(2)
        else: 
            print('Eita... o que está errado?\nselecione uma das opções por favor:')
            print('[ 1 ] Redefinir nome\n[ 2 ] Redefinir usuário\n[ 3 ] Redefinir senha')
            resposta3 = str(input('SUA RESPOSTA: '))
            if resposta3 == '1':
                resposta_nome2 = str(input('Para qual nome deseja redefinir?\nSua resposta: '))
                nome[0] = resposta_nome2
                print('PROCESSANDO...')
                carregamento()
                print('Prontinho, {} !'.format(*nome))
                print('\033[35mVoltando...\033[m')
                sleep(2)
            elif resposta3 == '2':
                resposta_usuario2 = str(input('Qual seu novo nome de usuário? @'))
                usuario[0] = resposta_usuario2
                print('PROCESSANDO...')
                carregamento()
                print('\033[32mProntinho! Seu novo nome de usuário é:\033[m {}'.format(*usuario))
                print('\033[35mVoltando...\033[m')
                sleep(2)
            elif resposta3 == '3':
                redefinir()
                print('PROCESSANDO...')
                carregamento()
                print('\033[32mSENHA ALTERADA COM SUCESSO! [✓]\033[m')
                print('\033[35mVoltando...\033[m')
                sleep(2)
    elif resposta == 'N':
        print('Olá! é muito bom te ver aqui de novo! :D')
        print('Comece informando seu login, por favor:')
        login_usuario = str(input('USUÁRIO: @'))
        login_senha = str(input('SENHA: '))
        print('PROCESSANDO...')
        sleep(2)
        print('\033[53m-\033[m' * 10)    
        if login_usuario == usuario[0] and login_senha == senha[0]:
            while True:        
                print('Seja bem-vindo de volta \033[36m@{}\033[m !'.format(usuario[0]))
                print('Preparei alguns joguinhos para você se divertir aqui! Confira:')
                print('\033[33m[ 1 ] Jogo da adivinhação\n[ 2 ] Pedra, papel e tesoura\n[ 3 ] Jogo da forca\n[ 4 ] adivinhe o planeta\n[ 5 ] jogo secreto...\n[ 7 ] REDEFINIÇÃO DE CONTA\n[ 0 ] LOGGOUT\033[m')
                resposta4 = str(input('SUA RESPOSTA: '))
                if resposta4 == '1':
                    while True:
                        print('Iniciando jogo...')
                        sleep(2)
                        print('-' * 10)
                        print('========\033[35mJOGO DA ADIVINHAÇÃO\033[m========')
                        print('\033[35m-=-\033[m' * 20)
                        print('Opa, @{} ! Seja muito bem-vindo(a)!'.format(*usuario))
                        sleep(3)
                        print('\033[1;34mpermita-me explicar como funciona:\nNesse jogo, eu penso em um número aleatório de 0 até 10!\nSerá que você consegue adivinhar em qual estou pensando? rs.\033[m')
                        sleep(5)
                        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                        pc = random.choice(numeros)
                        tentativas = 1
                        print('-' * 10)
                        print('Tá pronto?')
                        sleep(2)
                        print('Já pensei no número!')
                        jogador = str(input('Eai... qual será que escolhi?\nSUA RESPOSTA: '))
                        while jogador != pc:
                            print('Você errou! Haha!')
                            print('Tenta novamente aí!')
                            jogador = str(input('SEU CHUTE: '))
                            tentativas += 1
                            print('-' * 10)
                        if tentativas == '1':
                            print('Ca-ram-ba. Eu não esperava que fosse ser tão óbvio...\nBom, parece que você me venceu haha! Parabéns!')
                        else:
                            print('Parabéns, você acertou! :D\nFoi necessário {} tentativas para me vencer!'.format(tentativas))
                        print('Você quer continuar jogando[S/N]? ')
                        resposta = str(input('SUA RESPOSTA: ')).upper().strip()
                        if resposta == 'N':
                            print('VOLTANDO AO INICIO...')
                            sleep(2)
                            break
                # tem mais coisa para adicionar, para voltar ao menu principal
                if resposta4 == '2':
                    print('Iniciando o jogo...')
                    sleep(2)
                    print('-=-' * 10)
                    print('{:^40}'.format('PEDRA, PAPEL E TESOURA'))
                    print('-' * 10)
                    print('\033[1;34mPermita-me explicar como funciona:\nO famoso JOKENPÔ consiste em ambos os jogadores escolherem entre PEDRA, PAPEL ou TESOURA.\nPAPEL → Ganha de pedra, perde para tesoura\nPEDRA → Ganha da tesoura, mas perde para papel\nTESOURA → Ganha de papel, mas perde para pedra.\nEai! Simples, não é?\033[m')
                    sleep(5)
                    print('VAMOS AO DESAFIO!')
                    print('NO 3 VOCÊ ESCOLHE! FECHOU?')
                    print('-' * 20)
                    sleep(1)
                    print('...')
                    sleep(1)
                    print('1')
                    sleep(1)
                    print('2')
                    sleep(1)
                    print('3')
                    escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
                    pc = random.choice(escolhas)
                    jogador = str(input('SUA ESCOLHA: ')).upper()
                    print('...')
                    sleep(1)
                    print('JO')
                    sleep(1)
                    print('KEN...')
                    sleep(1)
                    print('PO!')
                    print('-' * 10)
                    print('JOGADOR: {}\nCOMPUTADOR: {}'.format(jogador, pc))
                    if jogador == 'PEDRA' and pc == 'TESOURA' or jogador == 'PAPEL' and pc == 'PEDRA' or jogador == 'TESOURA' and pc == 'PAPEL':
                        print('\033[32mVOCÊ VENCEU!\033[m')
                        print('Essa foi uma bela jogada, ein? Haha!')
                    elif jogador == pc:
                        print('\033[33mEITA! parece que empatamos...\033[m')
                        print('Bora desempatar!')
                        print('-' * 20)
                        while jogador == pc:
                            jogador = str(input('SUA ESCOLHA: ')).upper().strip()
                            pc = random.choice(escolhas)
                            print('JOGADOR: {}\nCOMPUTADOR: {}'.format(jogador, pc))
                            if jogador == 'PEDRA' and pc == 'TESOURA' or jogador == 'PAPEL' and pc == 'PEDRA' or jogador == 'TESOURA' and pc == 'PAPEL':
                                print('Caramba, \033[32mvocê me venceu!\033[m\nPARABÉNS! Essa foi acirrada, ein? hehe.')
                            elif jogador == pc:
                                print('EI, de novo!? Sinto que Você tá roubando ein... hahah!\nBrincadeiras a parte, BORA DESEMPATAR!') 
                            else:    
                                print('EU VENCI! Nossa, essa foi realmente acirrada, ein? hehe.')
                    else:
                        print('EU VENCI! Haha! Quer jogar de novo?')
                    print('-' * 20)

                if resposta4 == '3':
                    print('Iniciando o jogo...')
                    sleep(2)
                    print('-=-' * 20)
                    print('======\033[36mJOGO DA FORCA\033[m======')
                    print('\033[32EM DESENVOLVIMENTO.\033[m')
                
                if resposta4 == '4':
                    print('JOGO EM DESENVOLVIMENTO...')
                    print('retornando...')
                    sleep(2)
                
                if resposta4 == '5':
                    print('JOGO EM DESENVOLVIMENTO...')
                    print('retornando...')
                    sleep(2)

                if resposta4 == '7':
                    redefinir()

                if resposta4 == '0':
                    print('\033[31mSaindo...\033[m')
                    sleep(3)
                    break
        else:
            while tentativa != 0:
                print('Parece que há algo errado... por favor, tente novamente:')
                print('Você tem mais {} tentativas.'.format(tentativa))
                login_usuario = str(input('USUÁRIO: @'))
                login_senha = str(input('SENHA: '))
                tentativa -= 1
            print('\033[31mParece que você não conseguiu fazer login.\033[m')
            sleep(2)
            print('Caso não tenha um ainda, retorne e crie um usuário antes de prosseguir.')
            sleep(4)
            print('Voltando...')
            sleep(2)
print('ENCERRANDO O PROGRAMA...')
sleep(2)












