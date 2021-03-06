import pandas as pd
import numpy as np
import modules.utils as utils


def menu(titulo):
    
    utils.limparTela()
    print("::::::::::::::: ANALISE FINANCEIRA ::::::::::::::::::")
    j = int(input('Periodo em anos >> '))
    rate = float(input('taxa >> '))
    vi = float(input('Investimento inicial >> '))
    v1 = float(input('valor do primeiro periodo[mes ou ano] >> '))

    total = 0            
    flx = list()
    ano = list()
    total_descontado = list()
    saldo = list()

                
    for i in range(j):
        if i == 0:
            flx.append( vi / (1 + rate) ** i)
            ano.append(i)
            total_descontado.append(-vi)
            saldo.append(round(-(vi) - (v1 / (1 + rate ) ** i), 2))
        elif i == 4:
            flx.append(round((v1 / (1 + rate ) ** i), 2))
            ano.append(i)
            total_descontado.append(v1)
        else:
            flx.append(round((v1 / (1 + rate ) ** i), 2))
            ano.append(i)
            total_descontado.append(v1)
            saldo.append(round(-(vi) - (v1 / (1 + rate ) ** i), 2))
            
    for r in flx:
        total += round(r, 2)
        
    saldo.append(round(total, 2))

    data = {
        'Ano': ano,
        'Total': total_descontado,
        'Descontado(R$)': flx,
        'Saldo':saldo
    }

    valores = pd.DataFrame(data)
    print(valores)
    input('Aperte [ENTER] para voltar ao Menu.')

