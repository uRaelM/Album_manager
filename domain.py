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
    def salvar(self):
        self.status = messagebox.askyesno(message="Tem certeza que deseja cadastrar ?")
        if self.status != False:
            self.dados = []

            self.ialbum = str(self.entrada_album.get())
            self.dados.append(self.ialbum)

            self.ilancamento = str(self.entrada_ano_lancamento.get())
            self.dados.append(self.ilancamento)

            self.ibanda_artista = str(self.entrada_banda_artista.get())
            self.dados.append(self.ibanda_artista)

            self.isim_nao = self.var.get()
            if self.isim_nao == 1:
                self.dados.append("sim")
            else:
                self.dados.append("não")

            # LIMPA OS ENTRYS
            self.entrada_album.delete("0", "end")
            self.entrada_banda_artista.delete("0", "end")
            self.entrada_ano_lancamento.delete("0", "end")

            self.store()
    
    def pesquisar(self):
        for e in self.treeview.get_children():
            self.treeview.delete(e)

        self.ano = self.ano_busca.get()
        self.v_radio_p = self.var.get()
        if self.ano.isnumeric():
            self.l_busca = self.buscar()

            self.l_busca.sort()  # ORDENA DE ACORDO COM ELEMENTO DA POSIÇÃO 0 DE CADA ELEMENTO DE l_busca

            for e in self.l_busca:
                self.treeview.insert("", "end", values=[f"{e[1]}", f"{e[2]}", f"{e[0]}"])
    
    def pesquisar_nome(self):
        for e in self.treeview.get_children():
            self.treeview.delete(e)
        
        self.lista_exibir = self.buscar_nome()

        self.lista_exibir.sort()

        if len(self.lista_exibir) == 0:
            messagebox.showinfo(message="Nenhum resultado encontrado.")
        else:
            for e in self.lista_exibir:
                self.treeview.insert("", "end", values=[f"{e[1]}", f"{e[0]}", f"{e[2]}"]) 
    
    def lista_combobox(self):
        self.lista_anos = self.combobox_list()
        self.lista_anos.sort()

        return self.lista_anos
    
    def obter_registros(self):
        self.registros = self.get_registros()
        self.registros.sort()

        return self.registros