#from modules import * # TKINTER
import json


# PARTE QUE ACESSA O ARQUIVO PARA REALIZAR DETERMINADA AÇÃO
class ModelParaCrud():
    def criar_arquivo(self):
        try:
            self.arquivo = open("arquivo.json", "r", encoding="utf-8")
        except:
            self.arquivo = open("arquivo.json", "w", encoding="utf-8")
            self.arquivo.write("[]")
            self.arquivo.close()
        else:
            self.arquivo.close()

    def get_registros(self):
        self.registros = []

        self.arquivo = open("arquivo.json", "r", encoding="utf-8")
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()

        for e in self.dados_py:
            #self.dados = linha.split(" | ")
            self.lista_temp = [e["album"], e["ano_lancamento"], e["banda_artista"]]
            self.registros.append(self.lista_temp)


        return self.registros

    def combobox_list(self):
        self.lista_anos = []

        self.arquivo = open("arquivo.json", "r", encoding="utf-8")
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()

        for e in self.dados_py:
            #self.linha = e.split(" | ")

            if int(e["ano_lancamento"]) not in self.lista_anos:
                self.lista_anos.append(int(e["ano_lancamento"]))

        return self.lista_anos

    def buscar_nome(self):
        self.lista_exibir = []

        self.arquivo = open("arquivo.json", "r", encoding="utf-8")
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()
    
        for e in self.dados_py:
            #self.linha = e.split(" | ")
            self.lista = [e["banda_artista"], e["album"], e["ano_lancamento"]]
            if self.nm_artista.lower() in e["banda_artista"].lower():
                self.lista_exibir.append(self.lista)


        return self.lista_exibir   

    def buscar(self):
        self.l_busca = []

        self.arquivo = open("arquivo.json", "r", encoding='utf-8')
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()

        for e in self.dados_py:
            #self.linha = e.split(" | ")
            self.lista_n = [e["ano_lancamento"], e["album"], e["banda_artista"]]  # SERVE PARA DEIXAR NA ORDEM CERTA, PARA, NA LINHA 29, CONSEGUIR ORDENAR OS ANOS EM ORDEM CRESCENTE
            if self.v_radio_p == 1 and int(e["ano_lancamento"]) <= int(self.ano):
                self.l_busca.append(self.lista_n)
            elif self.v_radio_p == 2 and int(e["ano_lancamento"]) == int(self.ano):
                self.l_busca.append(self.lista_n)
            elif self.v_radio_p == 3 and int(e["ano_lancamento"]) >= int(self.ano):
                self.l_busca.append(self.lista_n)

        return self.l_busca
    
    def pegar_albuns(self):
        self.albuns_salvos = []

        self.arquivo = open("arquivo.json", "r", encoding="utf-8")

        '''for e in self.arquivo:
            e = e.split(" | ")
            self.albuns_salvos.append(e[0].lower())'''
        
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()
        for e in self.dados_py:
            e = e["album"]
            self.albuns_salvos.append(e.lower())

        return self.albuns_salvos        

    def store(self):
        self.arquivo = open("arquivo.json", "r", encoding="utf-8")
        self.dados_py = json.load(self.arquivo)

        self.arquivo.close()

        self.dic_temp = {"album":self.dados[0], "ano_lancamento":self.dados[1], "banda_artista":self.dados[2], "ultimo":self.dados[3]}
        
        self.dados_py.append(self.dic_temp)

        self.dados_json = json.dumps(self.dados_py, indent=True)

        self.arquivo = open("arquivo.json", "w", encoding="utf-8")
        self.arquivo.write(self.dados_json)

        self.arquivo.close()
