from modules import *  # TKINTER
from domain import *   # IMPORTANDO TUDO DO domain.py


# APLICAÇÃO
class App(GetTelas, Crud):
    def __init__(self):
        self.tela1()
    
    def tela1(self):
        self.window = Tk()
        self.window.title("Spotify List")
        self.window.geometry("500x250+700+300")
        self.window.resizable(False, False)
        self.window.configure(bg="#040404")
        self.window.focus_force()
        # O PARÂMETRO True DEFINE QUE ESSA logo_top.ico TAMBÉM SE APLICA PARA AS OUTRAS TELAS TOPLEVEL
        self.window.iconbitmap(True, "img/logo_top.ico")

        self.lb1 = Label(self.window, text="Spotify List", font="Arial 16 bold", fg="#24cb5b", bg="#040404")
        self.lb1.place(x=192, y=30)

        self.img = PhotoImage(file="img/spotify-logo.png")

        self.btn1 = Button(self.window, image=self.img, width=160, height=120, bd=2, bg="#040404", cursor="exchange", command=self.get_tela2)
        self.btn1.place(x=170, y=90)
        self.window.mainloop()
    
    def tela2(self):
        self.window = Tk()
        self.window.title("Spotify List")
        self.window.geometry("500x250+700+300")
        self.window.resizable(False, False)
        self.window.configure(bg="#040404")
        self.window.focus_force()

        # LABELS E ENTRY
        self.album = Label(self.window, text="Álbum:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
        self.album.pack()

        self.entrada_album = Entry(self.window, width=30)
        self.entrada_album.pack()

        self.ano_lancamento = Label(self.window, text="Ano de lançamento:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
        self.ano_lancamento.pack()

        self.entrada_ano_lancamento = Entry(self.window, width=30)
        self.entrada_ano_lancamento.pack()

        self.banda_artista = Label(self.window, text="Banda/Artista:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
        self.banda_artista.pack()

        self.entrada_banda_artista = Entry(self.window, width=30)
        self.entrada_banda_artista.pack()

        self.ultimo_album = Label(self.window, text="Ultimo album de lançamento(Sim/Não):", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
        self.ultimo_album.pack()

        self.var = IntVar()
        self.entrada_sim = Radiobutton(self.window, text="Sim", variable=self.var, value=1, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        self.entrada_sim.place(x=160, y=170)

        self.entrada_nao = Radiobutton(self.window, text="Não", variable=self.var, value=2, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        self.entrada_nao.place(x=270, y=170)

        # BOTÕES
        self.botao_salvar = Button(self.window, text="Cadastrar", bg="#040404", fg="#24cb5b", font="Arial 10 bold", command=self.salvar)
        self.botao_salvar.place(x=150, y=200)

        self.botao_buscar = Button(self.window, text="Lista de álbuns", bg="#040404", fg="#24cb5b", font="Arial 10 bold", command=self.get_tela3)
        self.botao_buscar.place(x=260, y=200)

        self.window.mainloop()
    
    def tela3(self):
        self.registros = self.obter_registros()

        self.window = Tk()
        self.window.title("Spotify List")
        self.window.geometry("600x400+650+80")
        self.window.resizable(False, False)
        self.window.configure(bg="#040404")
        self.window.focus_force()

        self.btn_pesquisar = Button(self.window, text="Pesquisar", bg="gray", font="Arial 12 bold", bd=2, command=self.get_tela4)
        self.btn_pesquisar.place(x=490, y=12)

        self.lb1 = Label(self.window, text="Dados cadastrados", bg="#040404", fg="#24cb5b", font="Arial 16 bold")
        self.lb1.place(x=200, y=12)

        self.btn1 = Button(self.window, text="Voltar", bg="gray", font="Arial 9 bold", width=25, command=self.get_tela2)
        self.btn1.place(x=200, y=360)

        self.treeview = ttk.Treeview(self.window, columns=("1", "2", "3"), show="headings")
        self.scroll = ttk.Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        self.scroll.place(x=552, y=100, height=227)
        self.treeview.configure(yscrollcommand=self.scroll.set)

        self.style = ttk.Style(self.window)
        self.style.theme_use("classic")
        self.style.configure("Treeview", font="Arial 10 bold", background="#ced0ba", foreground="#040404")
        self.style.configure("Heading", font="Arial 12 bold", foreground="#040404")

        self.treeview.column("1", minwidth=0, width=170)
        self.treeview.column("2", minwidth=0, width=170)
        self.treeview.column("3", minwidth=0, width=170)

        self.treeview.heading("1", text="Nome do álbum")
        self.treeview.heading("2", text="Nome do artista")
        self.treeview.heading("3", text="Ano de lançamento")

        self.treeview.place(x=40, y=100)

        for e in self.registros:
            self.treeview.insert("", "end", values=[f"{e[0]}", f"{e[2]}", f"{e[1]}"])

        self.window.mainloop()
    
    def tela4(self):
        # LISTA PARA SER UTILIZADA NA COMBOBOX
        self.lista_anos = self.lista_combobox()        

        self.window = Tk()
        self.window.title("Spotify List")
        self.window.geometry("600x600+650+80")
        self.window.resizable(False, False)
        self.window.configure(bg="#040404")
        self.window.focus_force()
        # BOTÃO PARA RETORNAR À TELA 3
        self.btn1 = Button(self.window, text="Ver todos", font="Arial 10 bold", bg="gray", width=25, command=self.get_tela3)
        self.btn1.place(x=70, y=520)

        self.btn_pesquisar_nm = Button(self.window, text="Pesquisar por nome", font="Arial 10 bold", bg="gray", width=25, command=self.get_tela5)
        self.btn_pesquisar_nm.place(x=350, y=520)
        # RADIO BUTTONS
        self.var = IntVar()
        self.r_btn1 = Radiobutton(self.window, text="Anterior a", variable=self.var, value=1, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        self.r_btn1.place(x=30, y=50)

        self.r_btn2 = Radiobutton(self.window, text="Igual a", variable=self.var, value=2, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        self.r_btn2.place(x=30, y=100)

        self.r_btn3 = Radiobutton(self.window, text="Posterior a", variable=self.var, value=3, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        self.r_btn3.place(x=30, y=150)

        self.lb_busca = Label(self.window, text="Selecione o ano do álbum", bg="#040404", fg="#24cb5b", font="Arial 12 bold")
        self.lb_busca.place(x=240, y=32)

        # DEFINIÇÃO DO COMBOBOX (DROP DOWN)
        self.ano_busca = ttk.Combobox(self.window, font="Arial 10 bold", values=self.lista_anos)
        self.ano_busca.place(x=250, y=70)

        self.btn_busca = Button(self.window, text="Buscar", bg="gray", fg="black", font="Arial 10 bold", command=self.pesquisar)
        self.btn_busca.place(x=450, y=68)

        self.treeview = ttk.Treeview(self.window, columns=("1", "2", "3"), show="headings")
        self.scroll = ttk.Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        self.scroll.place(x=552, y=210, height=227)
        self.treeview.configure(yscrollcommand=self.scroll.set)

        self.style = ttk.Style(self.window)
        self.style.theme_use("classic")
        self.style.configure("Treeview", font="Arial 10 bold", background="#ced0ba", foreground="#040404")
        self.style.configure("Heading", font="Arial 12 bold", foreground="#040404")

        self.treeview.column("1", minwidth=0, width=170)
        self.treeview.column("2", minwidth=0, width=170)
        self.treeview.column("3", minwidth=0, width=170)

        self.treeview.heading("1", text="Nome do álbum")
        self.treeview.heading("2", text="Nome do artista")
        self.treeview.heading("3", text="Ano de lançamento")

        self.treeview.place(x=40, y=210)

        self.window.mainloop()
    

    def tela5(self):
        self.window = Tk()
        self.window.title("Spotify List")
        self.window.geometry("600x600+650+80")
        self.window.resizable(False, False)
        self.window.configure(bg="#040404")
        self.window.focus_force()

        self.lb1 = Label(self.window, text="Digite o nome do(a) artista/banda", font="Arial 12 bold", bg="#040404", fg="#24cb5b")
        self.lb1.place(x=66, y=50)

        self.entrada1 = Entry(self.window, width=30)
        self.entrada1.place(x=70, y=80)

        self.btn1 = Button(self.window, text="Buscar", font="Arial 10 bold", bg="gray", command=self.pesquisar_nome)
        self.btn1.place(x=280, y=76)

        self.treeview = ttk.Treeview(self.window, columns=("1", "2", "3"), show="headings")
        self.scroll = ttk.Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        self.scroll.place(x=552, y=150, height=227)
        self.treeview.configure(yscrollcommand=self.scroll.set)

        self.style = ttk.Style(self.window)
        self.style.theme_use("classic")
        self.style.configure("Treeview", font="Arial 10 bold", background="#ced0ba", foreground="#040404")
        self.style.configure("Heading", font="Arial 12 bold", foreground="#040404")

        self.treeview.column("1", minwidth=0, width=170)
        self.treeview.column("2", minwidth=0, width=170)
        self.treeview.column("3", minwidth=0, width=170)

        self.treeview.heading("1", text="Nome do álbum")
        self.treeview.heading("2", text="Nome do artista")
        self.treeview.heading("3", text="Ano de lançamento")

        self.treeview.place(x=40, y=150)

        self.btn2 = Button(self.window, text="Ver todos", font="Arial 10 bold", bg="gray", width=25, command=self.get_tela3)
        self.btn2.place(x=70, y=540)

        self.btn3 = Button(self.window, text="Pesquisar por ano", font="Arial 10 bold", bg="gray", width=25, command=self.get_tela4)
        self.btn3.place(x=350, y=540)

        self.window.mainloop()



App()