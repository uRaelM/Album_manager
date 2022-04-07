from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def tela4():
    
    def get_ano():
        print(ano_busca.get())


    lista_anos = []

    arquivo = open("arquivo.txt", "r")
    for e in arquivo:
        linha = e.split(" | ")
        if linha[1] not in lista_anos:
            lista_anos.append(linha[1])
    
    lista_anos.sort()
    
    arquivo.close()


    window = Tk()
    window.title("Spotify List")
    window.geometry("600x800+650+80")
    window.resizable(0,0)
    window.configure(bg="#040404")

    var = IntVar()
    r_btn1 = Radiobutton(window, text="Anterior a", variable=var, value=1, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
    r_btn1.place(x=30, y=50)

    r_btn2 = Radiobutton(window, text="Igual a", variable=var, value=2, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
    r_btn2.place(x=30, y=100)

    r_btn3 = Radiobutton(window, text="Posterior a", variable=var, value=3, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
    r_btn3.place(x=30, y=150)

    ano_busca = ttk.Combobox(window, values=lista_anos)
    ano_busca.place(x=250, y=100)

    btn_busca = Button(window, text="Buscar", bg="gray", fg="black", command=get_ano)
    btn_busca.place(x=450, y=98)


    window.mainloop()

def tela3():
    def get_tela2():
        window.destroy()
        tela2()
    
    def get_tela4():
        window.destroy()
        tela4()

    registros = []
    try:
        arquivo = open("arquivo.txt", "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.split(" | ")
            registros.append(dados)

        arquivo.close()
    except:
        arquivo = open("arquivo.txt", "a", encoding="utf-8")
        arquivo.close()

    window = Tk()
    window.title("Spotify List")
    window.geometry("600x800+650+80")
    window.resizable(0,0)
    window.configure(bg="#040404")

    btn_pesquisar = Button(window, text="Pesquisar", bg="gray", fg="black", font="Arial 12 bold", bd=2, command=get_tela4)
    btn_pesquisar.place(x=490, y=12)

    lb1 = Label(window, text="Dados cadastrados", bg="#040404", fg="#24cb5b", font="Arial 16 bold")
    lb1.pack()

    btn1 = Button(window, text="Voltar", bg="gray", width=25, command=get_tela2)
    btn1.place(x=200, y=700)

    lb2 = Label(window, text="Nome do álbum", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=20, y=50)
    eixo_x = 30
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[0], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y += 30

    lb2 = Label(window, text="Nome do artista", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=230, y=50)
    eixo_x = 250
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[2], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y += 30

    lb2 = Label(window, text="Ano de lançamento", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=430, y=50)
    eixo_x = 470
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[1], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y += 30

    window.mainloop()


def tela2():
    def store():
        status = messagebox.askyesno(message="Tem certeza que deseja cadastrar ?")
        if status != False:
            dados = []

            ialbum = str(entrada_album.get().lower())
            dados.append(ialbum)

            ilancamento = str(entrada_ano_lancamento.get())
            dados.append(ilancamento)

            ibanda_artista = str(entrada_banda_artista.get().lower())
            dados.append(ibanda_artista)

            isim_nao = var.get()
            if isim_nao == 1:
                dados.append("sim")
            else:
                dados.append("não")

            # FAZ OS ENTRYS SEREM LIMPOS
            entrada_album.delete("0", "end")
            entrada_banda_artista.delete("0", "end")
            entrada_ano_lancamento.delete("0", "end")
            
            valid = True
            for e in dados:
                if (e == "" or e.isspace()):  # VALIDAÇÃO DOS DADOS
                    valid = False
                    break

            if (valid == True):
                albuns_salvos = []

                arquivo = open("arquivo.txt", "r", encoding="utf-8")
                for e in arquivo:
                    e = e.split(" | ")
                    albuns_salvos.append(e[0])

                arquivo.close()

                if (dados[0] not in albuns_salvos and dados[1].isnumeric()):
                    dados_p_salvar = " | ".join(dados)

                    dados_para_salvar = dados_p_salvar + '\n'

                    arquivo = open("arquivo.txt", "a", encoding="utf-8")
                    arquivo.write(dados_para_salvar)

                    arquivo.close()
                    messagebox.showinfo(message="Dados cadastrados com sucesso !")
                else:
                    messagebox.showerror(message="Algo deu errado, tente novamente.")
            else:
                messagebox.showerror(message="Algo deu errado, tente novamente")

    def get_tela3():
        window.destroy()
        tela3()

    # JANELA
    window = Tk()
    window.title("Spotify List")
    window.geometry("500x250+700+300")
    window.resizable(0,0)
    window.configure(bg="#040404")

    # LABELS E ENTRY
    album = Label(window, text="Álbum:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
    album.pack()

    entrada_album = Entry(window, width=30)
    entrada_album.pack()

    ano_lancamento = Label(window, text="Ano de lançamento:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
    ano_lancamento.pack()

    entrada_ano_lancamento = Entry(window, width=30)
    entrada_ano_lancamento.pack()

    banda_artista = Label(window, text="Banda/Artista:", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
    banda_artista.pack()

    entrada_banda_artista = Entry(window, width=30)
    entrada_banda_artista.pack()

    ultimo_album = Label(window, text="Ultimo album de lançamento(Sim/Não):", font="Arial 14 bold", fg="#24cb5b",
                         bg="#040404")
    ultimo_album.pack()

    var = IntVar()
    entrada_sim = Radiobutton(window, text="Sim", variable=var, value=1, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
    entrada_sim.place(x=160, y=170)

    entrada_nao = Radiobutton(window, text="Não", variable=var, value=0, bg="#040404", fg="#24cb5b", font="Arial 10 bold")
    entrada_nao.place(x=270, y=170)

    # BOTÕES
    botao_salvar = Button(window, text="Cadastrar", bg="#040404", fg="#24cb5b", font="Arial 10 bold", command=store)
    botao_salvar.place(x=150, y=200)

    botao_buscar = Button(window, text="Lista de álbuns", bg="#040404", fg="#24cb5b", font="Arial 10 bold",
                          command=get_tela3)
    botao_buscar.place(x=260, y=200)

    window.mainloop()


def tela1():
    def get_tela2():
        window.destroy()
        tela2()

    window = Tk()
    window.title("Spotify List")
    window.geometry("500x250+700+300")
    window.resizable(0,0)
    window.configure(bg="#040404")
    # O PARÂMETRO True DEFINE QUE ESSA logo_top.ico TAMBÉM SE APLICA PARA AS OUTRAS TELAS TOPLEVEL
    window.iconbitmap(True, "img/logo_top.ico")

    lb1 = Label(window, text="Spotify List", font="Arial 16 bold", fg="#24cb5b", bg="#040404")
    lb1.place(x=192, y=30)

    img = PhotoImage(file="img/spotify-logo.png")

    btn1 = Button(window, image=img, width=160, height=120, bd=2, bg="#040404", cursor = "exchange", command=get_tela2)
    btn1.place(x=170, y=90)

    window.mainloop()


tela1()