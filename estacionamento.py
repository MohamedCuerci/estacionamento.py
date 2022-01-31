from datetime import datetime
import csv

#problemas no codigo
#ainda preciso ajeitar as funções do subsistema
#ler o arquivo estacionamento_em_aberto.txt qaundo inicar o programa para reconhecer os dados.
#ainda da pra enxugar bastante as linhas desse programa

def menu_inicial():
    print()
    print('============================ Gerenciamento ============================') 
    print()
    print('1 - Configurações do Sistema')
    print('2 - Vagas Disponiveis')
    print('3 - Vagas Ocupadas')
    print('4 - Entrada de Veiculos')
    print('5 - Saida de Veiculos')
    print('6 - Sair')
    print()
    
    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao > 0 and opcao <= 6:
                return opcao
            else:
                print('numero invalido, por favor digite novamente!')
        except ValueError:
            print('numero invalido, por favor digite novamente!')

#1
def menu_sistema():
    print()
    print('============================ Gerenciamento do Sistema ============================') 
    print()
    print('1 - Alterar a quantidade de vagas')
    print('2 - Alterar o valor da hora')
    print('3 - Voltar')

    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao > 0 and opcao <= 3:
                return opcao
            else:
                print('numero invalido, por favor digite novamente!')
        except ValueError:
            print('numero invalido, por favor digite novamente!')

#funções menu inicial
#2
def vagas_disponiveis(estacionamento, cont_vagas_vazias):
    '''verifica a disponibilidade das vagas'''
    #vaga = []
    #print(estacionamento)
    lista_temp = []
    cont = 1
    for vaga in estacionamento:
        if not vaga:
            cont_vagas_vazias += 1
            lista_temp.append(cont)
        cont += 1
    print(f'Qtde de vagas disponiveis: {cont_vagas_vazias}')
    print(f'Vagas Disponíveis: ', end='')
    for item in lista_temp:
        print(f'V{item}', end=' ')
    #print(lista_temp)
    print()

#3
def vagas_ocupadas(estacionamento, cont_vagas_ocupadas):
    '''verifica as vagas que estão ocupadas'''
    lista_temp = []
    cont = 1
    for vaga in estacionamento:
        if vaga:
            cont_vagas_ocupadas += 1
            lista_temp.append(cont)
        cont += 1

    print(f'QTDE Vagas ocupadas: {cont_vagas_ocupadas}')
    print(f'Vagas Ocupadas: ', end='')
    for item in lista_temp:
        print(f'V{item}', end=' ')
    print()

#4
def entrada_veiculo(estacionamento):
    '''cadastra geral dos veiculo'''
    #criando uma lista que posteriormente será adicionada na lista estacionamento
    vaga_temporaria = []

    #validação para as horas
    decisao_hora =  input('Defina a hora que sera utilizada: sistema ou manual: ').lower().strip()
    if decisao_hora == 'manual':
        print(f'hora do sistema: {hora}:{minuto}')
        while True:
            try:
                hora_chegada, min_chegada = input('digite a hora e minuto da entrada [hh:mm]: ').split(':')

                if int(hora_chegada) == hora and int(min_chegada) == minuto:
                    break
                else:
                    print('Ta sem relógio, camarada ? Digita essa merda denovo, sem trapacear')
            except:
                print('[ERRO] Por favor, digite novamente.')
        motivo = input('Em poucas palavras, explique pq escolheu colocar hora no manual: ')
        #ainda preciso adicionar o motivo num arquivo txt para salvar as ocorrencias
    else:
        hora_chegada = hora
        min_chegada = minuto
    

    
    #verificando disponibilidadde da vaga
    while True:
        try:
            vaga = int(input('Escolha uma vaga para estacionar: '))
            x = verifica_vaga_vaga(estacionamento, vaga)
            if x:
                break
            else:
                print('vaga ocupada, tente outra.')
        except:
            print(msg_erro)
        

    #verificando placa
    placa_veiculo = verifica_placa()
        

    #caracteristicas adicionais
    cor = input('Digite a cor do veiculo: ')
    marca = input('Digite a marca do veiculo: ')
    nome_proprietario = recebe_nome()
    while True:
        try:
            telefone = int(input('digite numero de telefone do proprietario: '))
            break
        except:
            print(msg_erro)


    #adicionando as informações na lista temporaria
    vaga_temporaria.append(str(hora_chegada)+':'+str(min_chegada))
    vaga_temporaria.append(placa_veiculo)
    vaga_temporaria.append(cor)
    vaga_temporaria.append(marca)
    vaga_temporaria.append(nome_proprietario)
    vaga_temporaria.append(telefone)

    #adicionando lista temporaria ao estacionamento
    estacionamento[vaga-1] = vaga_temporaria
    #preciso tirar esses print depois
    print()
    print(vaga_temporaria)
    print()
    #print(estacionamento)
    return estacionamento

#5
def saida_veiculo(estacionamento, hora, minuto, contador=0):
    '''atraves da placa do veiculo, essa função tenta encontrar o veiculo'''
    #primeiro passo - encontrar o carro
    while True:
        try:
            #verifica se o estacionamento esta vazio
            for vaga in estacionamento:
                if vaga:
                    contador +=1
            if contador <= 0:
                print('Nenhum veiculo encontrado.')
                break
            placa = input('Digite a placa do veiculo: ')
            #adicionar os dados no return da função pois preciso gravar essa informação depois
            valida, x, y = procura_vaga(estacionamento, placa)
            if valida:
                break
            else:
                decisao = input('placa nao encontrada, deseja tentar novamente ? [S/N] ').upper().strip()[0]
                if decisao == 'N':
                    break
        except:
            print(msg_erro)

    #função para calcular qaunto devera ser pago
    #obs: de brinde ainda mostra quanto tempo o carro ficou
    if contador >= 1:
        calculo_tempo_hora(x, y, hora, minuto)



#funçoes do Subsistema
def Alterar_qtde_vagas():
    '''altera qauntidade de vagas'''
    while True:
        try:
            qtde_vagas = int(input('Digite a quantidade de vagas: '))
            if qtde_vagas > 0 and qtde_vagas <= 100:
                return qtde_vagas
            else:
                print(msg_erro)
        except ValueError:
            print(msg_erro)

def Alterar_valor_hora(valor_hora):
    '''altera valor/hora do estacionamento'''
    while True:
        try:
            valor_hora = float(input('Digite o valor/hora: '))
            return valor_hora
        except:
            print(msg_erro)


#funções para ajudar 
def total_vagas(estacionamento, qtde_vagas):
    '''cria o estacionamento, baseado na qtde de vagas'''
    vagas = []
    lista_vagas = []
    for i in range(qtde_vagas):
        lista_vagas.append(vagas)
        estacionamento = lista_vagas
    return estacionamento

def verifica_placa():
    '''verifica se a placa possui letras e numeros'''
    while True:
        try:
            placa = input('Digite a placa do veiculo: ')
            if placa.isalnum():
                return placa
            else:
                print('[ERRO] placa invalida. Tente novamente')
        except:
            print('[ERRO] Por Favor, digite novamente.')
            

def verifica_vaga_vaga(estacionamento, vaga):
    '''percorrendo a lista e devolvendo vagas vagas kkkk'''
    contador = 0
    lista_de_vagas = []
    lista_de_vagas_ocupada = []
    for espaço in estacionamento:
        contador += 1
        if not espaço:
            lista_de_vagas.append(contador)
        else:
            lista_de_vagas_ocupada.append(contador)
    if vaga in lista_de_vagas:
        return True
    else:
        return False

def calculo_tempo_hora(hora_chegada, min_chegada, hora_partida, min_partida):
    '''faz o calculo do valor/hora'''
    # Define horario:
    if hora_chegada > hora_partida:
        hora_partida = hora_partida + 24
    if min_chegada > min_partida:
        min_partida = min_partida + 60
        hora_partida = hora_partida - 1

    min_final = min_partida - min_chegada     
    hora_final = hora_partida - hora_chegada

    if hora_final >= 1:
        if min_final > 1:
            print('-----------------------------------------------------------')
            print("O carro ficou estacionado durante %d horas e %d minutos." % (hora_final, min_final))
        else:
            print('-----------------------------------------------------------')
            print("O carro ficou estacionado durante %d horas." % (hora_final))
    else:
        print('-----------------------------------------------------------')
        print("O carro ficou estacionado durante %d minutos." % (min_final))

    tempo_minutos = hora_final * 60 + min_final

    if tempo_minutos <= 60:
        total_pagar = valor_hora
    else:
        total_pagar = ((tempo_minutos // 60)+1) * valor_hora 
    print(f"O valor a ser pago será de R$ {float(total_pagar):.2f}")
    print('-----------------------------------------------------------')
    print()
    
def procura_vaga(estacionamento, placa):
    '''encontra a vaga escolhida para realizar a saida do veiculo'''
    nova_vaga = []
    contador_vaga = -1
    for vaga in estacionamento:
        contador_vaga += 1
        for carro in vaga:
            if carro == placa:
                print()
                print(f'Vaga Nº{contador_vaga+1} agora esta disponivel')
                
                #aki eu pego hora e minuto de entrada do veiculo
                #print(vaga[0])
                x, y = vaga[0].split(':')
                hora_entrada = int(x)
                minuto_entrada = int(y)
                #adicionando o numero da vaga nos dados da vaga e salvando no arquivo escolhido
                vaga.append(contador_vaga + 1)
                grava_saida_dados(vaga, 'estacionamentos_encerrados.csv')
                
                estacionamento.remove(vaga)
                estacionamento.insert(contador_vaga, nova_vaga)
                return True, hora_entrada, minuto_entrada

    if contador_vaga >= len(estacionamento):
        print('Essa placa não foi encontrada tente novamente')
        return False, 0, 0
        #preciso mudar alguma coisa aki

def verifica_informacao(dado):
    while True:
        if not dado:
            print('[ERRO] Por Favor digite uma informação valida.')

def recebe_nome():
    while True:
        #print()
        try:
            nome = input('Insira o nome do proprietario: ')
            if nome.isidentifier():
                return nome
            else:
                print('[ERRO] Por Favor, tente novamente.')
        except:
            print('[ERRO] Por favor, digite novamente')

#funções para trablhar com arquivos .txt ou .csv
#função para gravar dados da entrada num determinado arquivo
def grava_dados(estacionamento, nome_arquivo):
    '''cria um arquivo.csv que contem uma linha para cada "vaga" no estacionamento'''
    with open(nome_arquivo, 'w', newline='') as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=',')

        for vaga in estacionamento:
            csv_writer.writerow(vaga)

#função para gravar dados de saida num determinado arquivo
def grava_saida_dados(vaga, nome_arquivo):
    '''essa função vai acrescentar dados no arquivo definido'''
    with open(nome_arquivo, 'a', newline='') as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=',')

        csv_writer.writerow(vaga)

#função para ler os dados salvos num determindado arquivo
def ler_dados(tabela, nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as csv_file:
        leitor = csv.reader(csv_file, delimiter=',')

        for linha in leitor:
            tabela.append(linha)

#função para gravar a qtde de vagas e valor/hora
def grava_config(qtde_vagas, valor_hora, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=',') 
        dados = [qtde_vagas, valor_hora]
    
        csv_writer.writerow(dados)



##############################################################################################################################3
#mensagem de erro padrão
msg_erro = '[ERRO] Por Favor, tente novamente.'


#definindo hora atual
now = datetime.now()
hora = now.hour
minuto = now.minute

#lista para representar estacionamento
estacionamento = []

#valor padrão de vagas e valor/hora
valor_hora = 1
qtde_vagas = 10

cont_vagas_ocupadas = 0
cont_vagas_vazias = 0

#criando estacionamento
estacionamento = total_vagas(estacionamento, qtde_vagas)
#print(estacionamento)

while True:
        #total_vagas(estacionamento, qtde_vagas)
        x = menu_inicial()
        if x == 1:
            y = menu_sistema()
            if y == 1:
                qtde_vagas = Alterar_qtde_vagas()
                estacionamento = total_vagas(estacionamento, qtde_vagas)
                grava_config(qtde_vagas, valor_hora, 'configuracoes.csv')
                print(estacionamento)
            elif y == 2:
                print(f'valor/hora atual: {valor_hora}')
                valor_hora = Alterar_valor_hora(valor_hora)
                grava_config(qtde_vagas, valor_hora, 'configuracoes.csv')
                print(valor_hora)
        elif x == 2:
            vagas_disponiveis(estacionamento, cont_vagas_vazias)
        elif x == 3:
            vagas_ocupadas(estacionamento, cont_vagas_ocupadas)
        elif x == 4:
            entrada_veiculo(estacionamento)
            grava_dados(estacionamento, 'estacionamentos_em_aberto.csv')
        elif x == 5:
            saida_veiculo(estacionamento, hora, minuto)
            grava_dados(estacionamento, 'estacionamentos_em_aberto.csv')
        elif x == 6:
            print()
            print('Programa encerrado!')
            print()
            exit()

#lembre de tirar os print() q foram usados para debbug