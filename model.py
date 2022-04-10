from modules import * # TKINTER


# PARTE QUE ACESSA O ARQUIVO PARA REALIZAR DETERMINADA AÇÃO
class ModelParaCrud():
    def get_registros(self):
        self.registros = []
        try:
            self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
            for linha in self.arquivo:
                self.dados = linha.split(" | ")
                self.registros.append(self.dados)

            self.arquivo.close()
        except:
            self.arquivo = open("arquivo.txt", "a", encoding="utf-8")
            self.arquivo.close()

        return self.registros

    def combobox_list(self):
        self.lista_anos = []
        self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
        for e in self.arquivo:
            self.linha = e.split(" | ")
            if self.linha[1] not in self.lista_anos:
                self.lista_anos.append(self.linha[1])
        self.arquivo.close()

        return self.lista_anos

    def buscar_nome(self):
        try:
            self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
        except:
            messagebox.showerror(message="Não há álbuns cadastrados.")
        else:
            self.lista = []
            self.lista_exibir = []
            for e in self.arquivo:
                self.linha = e.split(" | ")
                self.lista = [self.linha[2], self.linha[0], self.linha[1]]
                self.nm_artista = self.entrada1.get().lower()
                if self.nm_artista in self.linha[2].lower() and self.nm_artista != "" and not self.nm_artista.isspace():
                    self.lista_exibir.append(self.lista)

            self.arquivo.close()

            return self.lista_exibir   

    def buscar(self):
        self.l_busca = []
        try:
            self.arquivo = open("arquivo.txt", "r", encoding='utf-8')
        except:
            messagebox.showerror(message="Não há álbuns cadastrados")
        else:
            for e in self.arquivo:
                self.linha = e.split(" | ")
                self.lista_n = [self.linha[1], self.linha[0], self.linha[2]]  # SERVE PARA DEIXAR NA ORDEM CERTA, PARA, NA LINHA 29, CONSEGUIR ORDENAR OS ANOS EM ORDEM CRESCENTE
                if self.v_radio_p == 1 and self.linha[1] <= self.ano:
                    self.l_busca.append(self.lista_n)
                elif self.v_radio_p == 2 and self.linha[1] == self.ano:
                    self.l_busca.append(self.lista_n)
                elif self.v_radio_p == 3 and self.linha[1] >= self.ano:
                    self.l_busca.append(self.lista_n)
            self.arquivo.close()

            return self.l_busca

    def store(self):
            self.valid = True
            for e in self.dados:
                if e == "" or e.isspace():  # VALIDAÇÃO DOS DADOS
                    self.valid = False
                    break

            if self.valid == True:
                self.albuns_salvos = []

                try:
                    self.arquivo = open("arquivo.txt", "r", encoding="utf-8")
                    for e in self.arquivo:
                        e = e.split(" | ")
                        self.albuns_salvos.append(e[0].lower())

                    self.arquivo.close()
                except:
                    if self.dados[1].isnumeric():
                        self.dados_p_salvar = " | ".join(self.dados)

                        self.dados_para_salvar = self.dados_p_salvar + '\n'

                        self.arquivo = open("arquivo.txt", "a", encoding="utf-8")
                        self.arquivo.write(self.dados_para_salvar)

                        self.arquivo.close()
                        messagebox.showinfo(message="Dados cadastrados com sucesso !")
                    else:
                        messagebox.showerror(message="Você não preencheu os dados corretamente.")

                else:
                    if self.dados[0].lower() not in self.albuns_salvos and self.dados[1].isnumeric():
                        self.dados_p_salvar = " | ".join(self.dados)

                        self.dados_para_salvar = self.dados_p_salvar + "\n"

                        self.arquivo = open("arquivo.txt", "a", encoding="utf-8")
                        self.arquivo.write(self.dados_para_salvar)

                        self.arquivo.close()
                        messagebox.showinfo(message="Dados cadastrados com sucesso !")
                    else:
                        messagebox.showerror(message="Esse álbum já existe, ou você não preencheu os dados corretamente.")
            else:
                messagebox.showerror(message="Preencha todos os campos.")