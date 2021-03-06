import requests
from os import *

API_KEY = '410a78ed80f94de4aff6b31389899ac5'

class Converter:

    def __init__(
        self, value, fromMoney
    ):
        self.value = value
        self.fromMoney = fromMoney
    def fromNewCoin(
        self
    ):
        moedas = ['BRL', self.fromMoney]
        outMoney = '{},{}'.format(moedas[0], moedas[1])
        r = requests.get(
            'https://openexchangerates.org/api/latest.json',
            params = {
                'app_id':API_KEY,
                'symbols':outMoney,
                'show_alternative':'true',
                'base':'USD'
            }
        )

        rates  = r.json()['rates']
        out = self.value * 1/rates.get(moedas[0])*rates.get(moedas[1])
        return out
def limparTela():
    system('cls' if name == 'nt' else 'clear')

def main(cabecalho):
    limparTela()
    print(':::::::::::::|{}|:::::::::::::'.format(cabecalho))
    moeda = str(input('SIGLA da moeda [3 letras]: '))
    valor = input('Valor em Real: ')
    moeda = moeda.upper()
    c = Converter(float(valor), moeda.upper())
    saida = c.fromNewCoin()
    print(f'{valor} Reais em {moeda} = {saida}')
    input("Aperte ENTER p/ voltar ao Menu")
