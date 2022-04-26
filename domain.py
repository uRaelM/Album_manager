from modules import * # TKINTER
from model import *   # IMPORTANDO TUDO DA model.py


# LÓGICA DA APLICAÇÃO
# PARA MUDAR DE TELA
class GetTelas():
    def get_tela2(self):
        self.window.destroy()
        self.tela2()
    
    def get_tela3(self):
        self.window.destroy()
        self.tela3()

    def get_tela4(self):
        self.window.destroy()
        self.tela4()

    def get_tela5(self):
        self.window.destroy()
        self.tela5()


# LÓGICA DA APLICAÇÃO
class Crud(ModelParaCrud):
    def iniciar(self):
        try:
            self.criar_arquivo()
        except:
            messagebox.showerror(message="Não foi possível iniciar o programa corretamente")

    def salvar(self):
        self.status = messagebox.askyesno(message="Tem certeza que deseja cadastrar ?")
        if self.status != False:
            self.dados = []

            self.ialbum = self.entrada_album.get()
            self.dados.append(self.ialbum)

            self.ilancamento = self.entrada_ano_lancamento.get()
            self.dados.append(self.ilancamento)

            self.ibanda_artista = self.entrada_banda_artista.get()
            self.dados.append(self.ibanda_artista)

            self.isim_nao = self.var.get()
            if self.isim_nao == 1:
                self.dados.append("Sim")
            else:
                self.dados.append("Não")

            # LIMPA OS ENTRYS
            self.entrada_album.delete("0", "end")
            self.entrada_banda_artista.delete("0", "end")
            self.entrada_ano_lancamento.delete("0", "end")

            # VALIDAÇÃO DE DADOS
            self.valid = True
            for e in self.dados:
                if e == "" or e.isspace():  # VALIDAÇÃO DOS DADOS
                    self.valid = False
                    break
            if self.valid == True:
                try:
                    self.albuns_salvos = self.pegar_albuns() # VERIFICANDO QUAIS ÁLBUNS ESTÃO SALVOS
                except:
                    if self.dados[1].isnumeric():
                        #self.dados_p_salvar = " | ".join(self.dados)

                        #self.dados_para_salvar = self.dados_p_salvar + "\n"

                        self.store() # ARMAZENA OS DADOS NO arquivo.json
                        messagebox.showinfo(message="Dados cadastrados com sucesso !")
                    else:
                        messagebox.showinfo(message="Preencha os campos corretamente")
                else:                    
                    if self.dados[0].lower() not in self.albuns_salvos:
                        if self.dados[1].isnumeric():
                            #self.dados_p_salvar = " | ".join(self.dados)

                            #self.dados_para_salvar = self.dados_p_salvar + "\n"

                            self.store() # ARMAZENA OS DADOS NO arquivo.json
                            messagebox.showinfo(message="Dados cadastrados com sucesso !")
                        else:
                            messagebox.showinfo(message="Preencha os campos corretamente")
                    else:
                        messagebox.showinfo(message="Esse álbum já está cadastrado")
            else:
                messagebox.showinfo(message="Preencha os campos corretamente")
    
    def pesquisar(self):
        for e in self.treeview.get_children():
            self.treeview.delete(e)

        self.ano = self.ano_busca.get()
        self.v_radio_p = self.var.get()
        if self.ano.isnumeric():
            try:
                self.l_busca = self.buscar()
            except:
                messagebox.showerror(message="Não há álbuns cadastrados")
            else:
                if len(self.l_busca) == 0:
                    messagebox.showinfo(message="Nenhum resultado encontrado")
                else:
                    self.l_busca.sort()  # ORDENA DE ACORDO COM ELEMENTO DA POSIÇÃO 0 DE CADA ELEMENTO DE l_busca
                    for e in self.l_busca:
                        self.treeview.insert("", "end", values=[f"{e[1]}", f"{e[2]}", f"{e[0]}"])
        else:
            messagebox.showerror(message="Preencha os dados corretamente")
    
    def pesquisar_nome(self):
        for e in self.treeview.get_children():
            self.treeview.delete(e)
        
        self.nm_artista = self.entrada1.get()

        if self.nm_artista != "" and not self.nm_artista.isspace():

            try:
                self.lista_exibir = self.buscar_nome()
            except:
                messagebox.showerror(message="Não há álbuns cadastrados.")
            else:

                if len(self.lista_exibir) == 0:
                    messagebox.showinfo(message="Nenhum resultado encontrado.")
                else:
                    self.lista_exibir.sort()
                    for e in self.lista_exibir:
                        self.treeview.insert("", "end", values=[f"{e[1]}", f"{e[0]}", f"{e[2]}"])
        else:
            messagebox.showerror(message="Preencha o campo corretamente") 
    
    def lista_combobox(self):
        try:
            self.lista_anos = self.combobox_list()
        except:
            self.lista_anos = []
            messagebox.showinfo(message="Não há dados cadastrados")
        else:
            if len(self.lista_anos) != 0:
                self.lista_anos.sort()

        return self.lista_anos
    
    def obter_registros(self):
        try:
            self.registros = self.get_registros()
        except:
            self.registros = []
            messagebox.showinfo(message="Não há dados cadastrados")
        else:
            if len(self.registros) != 0:
                self.registros.sort()

        return self.registros
    
    def exibir_registros(self):
        for e in self.registros:
            self.treeview.insert("", "end", values=[f"{e[0]}", f"{e[2]}", f"{e[1]}"])
