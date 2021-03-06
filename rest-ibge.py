import requests
import csv


class ContadorRegioes:
    # Método construtor
    def __init__(self):
        try:
            self.url = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/")
            if self.url.status_code == 200:
                self.dados = self.url.json()
                self.Converter_para_CSV()
            else:
                print("Erro de Conexão: {} - Verifique se a sua conexão ou a URL estão de acordo".format(self.url))
        except Exception as erro:
            print("Erro: {}".format(erro))

    # Método que cria o CSV.
    def Converter_para_CSV(self):
        # Cria uma lista que armazena todas as regiões dentro do JSON.
        lista_regioes = []
        for regiao in self.dados:
            lista_regioes.append(regiao['regiao']['nome'])

        # Cria uma lista que armazena o nome das regiões encontradas sem repeti-las.
        regioes_encontradas = set(lista_regioes)

        # Cria um arquivo CSV.
        with open("estados.csv", "w") as f:
            columns = ['Regiao', 'Quantidade']
            escrever = csv.DictWriter(f, fieldnames=columns, delimiter='|', lineterminator='\n')
            escrever.writeheader()

            for regiao in sorted(regioes_encontradas):
                escrever.writerow({'Regiao': regiao, 'Quantidade': lista_regioes.count(regiao)})


usuario = ContadorRegioes()
