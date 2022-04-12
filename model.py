from modules import * # TKINTER


# PARTE QUE ACESSA O ARQUIVO PARA REALIZAR DETERMINADA AÇÃO
class ModelParaCrud():
    def criar_arquivo(self):
        self.arquivo = open("arquivo.txt", "a", encoding="utf-8")
        self.arquivo.close()

    def get_registros(self):
        self.registros = []

        self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
        for linha in self.arquivo:
            self.dados = linha.split(" | ")
            self.registros.append(self.dados)

        self.arquivo.close()

        return self.registros

    def combobox_list(self):
        self.lista_anos = []
        self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
        for e in self.arquivo:
            self.linha = e.split(" | ")
            if int(self.linha[1]) not in self.lista_anos:
                self.lista_anos.append(int(self.linha[1]))
        self.arquivo.close()

        return self.lista_anos

    def buscar_nome(self):
        self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
    
        self.lista = []
        self.lista_exibir = []
        for e in self.arquivo:
            self.linha = e.split(" | ")
            self.lista = [self.linha[2], self.linha[0], self.linha[1]]
            if self.nm_artista in self.linha[2].lower():
                self.lista_exibir.append(self.lista)

        self.arquivo.close()

        return self.lista_exibir   

    def buscar(self):
        self.l_busca = []

        self.arquivo = open("arquivo.txt", "r", encoding='utf-8')

        for e in self.arquivo:
            self.linha = e.split(" | ")
            self.lista_n = [self.linha[1], self.linha[0], self.linha[2]]  # SERVE PARA DEIXAR NA ORDEM CERTA, PARA, NA LINHA 29, CONSEGUIR ORDENAR OS ANOS EM ORDEM CRESCENTE
            if self.v_radio_p == 1 and int(self.linha[1]) <= int(self.ano):
                self.l_busca.append(self.lista_n)
            elif self.v_radio_p == 2 and int(self.linha[1]) == int(self.ano):
                self.l_busca.append(self.lista_n)
            elif self.v_radio_p == 3 and int(self.linha[1]) >= int(self.ano):
                self.l_busca.append(self.lista_n)
        self.arquivo.close()

        return self.l_busca
    
    def pegar_albuns(self):
        self.albuns_salvos = []

        self.arquivo = open("arquivo.txt", "r", encoding="utf-8")

        for e in self.arquivo:
            e = e.split(" | ")
            self.albuns_salvos.append(e[0].lower())

        self.arquivo.close()

        return self.albuns_salvos        

    def store(self):
        self.arquivo = open("arquivo.txt", "a", encoding="utf-8")
        self.arquivo.write(self.dados_para_salvar)

        self.arquivo.close()