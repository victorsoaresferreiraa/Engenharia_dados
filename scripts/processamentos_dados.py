import json
import csv

class Dados:
    
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        
    def leitura_json(self):
            dados_json = []
            with open(self, 'r') as file:
                dados_json = json.load(file)
            return dados_json    

    def leitura_csv(self):
        dados_csv = []
        with open(self, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        dados = []
        
        if self.tipo_dados == 'csv':
            dados = self.leitura_csv(self)
            
        elif self.tipo_dados == 'json':
            dados = self.leitura_json(self)
            
        return dados
