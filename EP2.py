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

frota = {}
nome_navios = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
for nome in frota.keys():
    n=0
    if nome =='porta=aviões':
        i=1
    elif nome == 'navio-tanque':
        i=2
    elif nome == 'contratorpedo':
        i=3
    elif nome == 'submarino':
        i=4
    while n<1:
        print(f'Insira as informacoes referentes ao navio {nome} que possui tamanho {tamanho[nome]}')
        linha=int(input('Qual linha?'))
        coluna=int(input('Qual coluna?'))
        if nome!= 'submarino':
            direcao=input('[1] vertical [2] horizontal')
        if nome== 'submarino':
            orientacao='vertical'
        if direcao== '1':
            orientacao='vertical'
        elif direcao== '2':
            orientacao='horizontal'
        if posicao_valida(frota, linha,coluna, orientacao,tamanho[nome])== False:
            print('Esta posicao nao esta valida!')
        else:
            preenche_frota(frota,linha,coluna,orientacao,tamanho[nome])
            n+=1
print (frota)