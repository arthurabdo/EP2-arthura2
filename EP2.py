import random

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    return posicoes


def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frota:
        frota[nome] = []
    frota[nome].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)]
    
    for tipo, l_posicoes in frota.items():
        for posicoes in l_posicoes:
            for linha, coluna in posicoes:
                grid[linha][coluna] = 1
    return grid
def afundados(frota, tabuleiro):
    navios_afundados = 0
    
    for navio,  posicoes in frota.items():
        for posicoes in posicoes:
            afundado = True
            for posicao in posicoes:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1
                
    return navios_afundados

def posicao_valida(dicio_navios, linha, coluna, orientacao, tamanho):
    navio=define_posicoes(linha, coluna,orientacao,tamanho)
    for n in navio:
        if n[0]<0 or n[1]<0 or n[0]>9 or n[1]>9:
            return False
        for i in dicio_navios.values():
            for j in range(len(i)):
                if n in i[j]:
                    return False
    if dicio_navios=={}:
        return True
    return True

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicionario_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

print(frota)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)

def monta_tabuleiros(tabuleiro_jogador,  tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        info_jogador = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        info_oponente = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {info_jogador}|     {linha}| {info_oponente}|\n'
    return texto
grade_frota = posiciona_frota(frota)
grade_oponente = posiciona_frota(frota_oponente)
primeiro_ataque_jogador = []
primeiro_ataque_oponente = []
jogando = True
while jogando == True:
    grade = monta_tabuleiros(grade_frota, grade_oponente)
    print(grade)
    repete = True
    while repete == True:
        linha = True
        coluna = True
        while linha == True:
            linha_do_ataque = int(input('Jogador, qual linha deseja atacar?'))
            if linha_do_ataque < 0 or linha_do_ataque > 9:
                print('Linha inválida')
            else:
                linha = False
        while coluna == True:
            coluna_do_ataque = int(input('Jogador, qual coluna deseja atacar?'))
            if coluna_do_ataque < 0 or coluna_do_ataque > 9:
                print('Coluna inválida!')
            else:
                coluna = False
        novo_ataque = [linha_do_ataque, coluna_do_ataque]
        if novo_ataque in primeiro_ataque_jogador:
            print(f'A posição linha {linha_do_ataque} e coluna {coluna_do_ataque} já foi informada anteriormente')
        else:
            repete = False
    primeiro_ataque_jogador.append(novo_ataque)
    grade_oponente = faz_jogada(grade_oponente, linha_do_ataque, coluna_do_ataque)
    barcos_afundados = afundados(frota_oponente, grade_oponente)
    if barcos_afundados == 10:
        jogando = False
        print('Parabéns! Você derrubou todos os navios do seu oponente! ;)')
    else:
            segunda_jogada = True
            while segunda_jogada:
                linha1 = random.randint(0, 9)
                coluna2 = random.randint(0, 9)
                ataque_oponente = [linha1, coluna2]
                if ataque_oponente not in primeiro_ataque_oponente:
                    print(f'Seu oponente está atacando na linha {linha1} e coluna {coluna2}')
                    primeiro_ataque_oponente.append(ataque_oponente)
                    grade_frota = faz_jogada(grade_frota, linha1, coluna2)
                    segunda_jogada = False
            if afundados(frota, grade_frota) == 10:
                jogando = False
                print('Opa! O oponente derrubou toda a sua frota! :( ')