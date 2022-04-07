from tkinter import *
from tkinter import messagebox


def tela3():
    def get_tela2():
        window.destroy()
        tela2()
    registros = []
    arquivo = open("arquivo.txt", "r", encoding="utf-8")
    for linha in arquivo:
        dados = linha.split(" | ")
        registros.append(dados)
        
    arquivo.close()
    

    window = Tk()
    window.title("Spotify List")
    window.geometry("600x800")
    window.configure(bg="#040404")

    lb1 = Label(window, text="Dados cadastrados", bg="#040404", fg="#24cb5b", font="Arial 16 bold")
    lb1.pack()

    btn1 = Button(window, text="Voltar", bg="gray", width=25, command=get_tela2)
    btn1.place(x=200, y=600)

    lb2 = Label(window, text="Nome do álbum", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=20, y=50)
    eixo_x = 30
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[0], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y+=30
    
    lb2 = Label(window, text="Nome do artista", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=230, y=50)
    eixo_x = 250
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[2], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y+=30
    
    lb2 = Label(window, text="Ano de lançamento", bg="#040404", fg="#24cb5b", font="Arial 13 bold")
    lb2.place(x=430, y=50)    
    eixo_x = 470
    eixo_y = 90
    for e in registros:
        exibicao = Label(window, text=e[1], bg="#040404", fg="#24cb5b", font="Arial 10 bold")
        exibicao.place(x=eixo_x, y=eixo_y)
        eixo_y+=30

    window.mainloop()

def tela2():
    def store():
        status = messagebox.askyesno(message="Tem certeza que deseja cadastrar ?")
        if status != False:
            dados = []
            
            ialbum = str(entrada_album.get().capitalize())
            dados.append(ialbum)

            ilançamento = str(entrada_ano_lancamento.get())
            dados.append(ilançamento)

            ibanda_artista = str(entrada_banda_artista.get().capitalize())
            dados.append(ibanda_artista)

            isim_nao = str(entrada_sim_nao.get().capitalize())
            dados.append(isim_nao)

            valid = True
            for e in dados:
                if ( e == "" or e.isspace() ): # VALIDAÇÃO DOS DADOS
                    valid = False
                    break
            
            if valid == True:
                albuns_salvos = []
                arquivo = open("arquivo.txt", "r", encoding="utf-8")
                for e in arquivo:
                    e = e.split(" | ")
                    albuns_salvos.append(e[0])
                
                arquivo.close()

                if dados[0] not in albuns_salvos and dados[1].isnumeric():
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
    window.geometry("500x250")
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
    banda_artista .pack()

    entrada_banda_artista = Entry(window, width=30)
    entrada_banda_artista.pack()


    ultimo_album = Label(window, text="Ultimo album de lançamento(Sim/Não):", font="Arial 14 bold", fg="#24cb5b", bg="#040404")
    ultimo_album .pack()

    entrada_sim_nao = Entry(window, width=30)
    entrada_sim_nao.pack()

    # BOTÕES
    botao_salvar = Button(window, text="Cadastrar", bg="#040404", fg="#24cb5b", font="Arial 10 bold", command=store)
    botao_salvar.place(x=150, y=200)

    botao_buscar = Button(window, text="Lista de álbuns", bg="#040404", fg="#24cb5b", font="Arial 10 bold", command=get_tela3)
    botao_buscar.place(x=260, y=200)

    window.mainloop()


def tela1():
    def get_tela2():
        window.destroy()
        tela2()

    window = Tk()
    window.title("Spotify List")
    window.geometry("500x250")
    window.configure(bg="#040404")
    # O PARÂMETRO True DEFINE QUE ESSA logo_top.ico TAMBÉM SE APLICA PARA AS OUTRAS TELAS TOPLEVEL
    window.iconbitmap(True, "img/logo_top.ico")

    lb1 = Label(window, text="Spotify List", font="Arial 16 bold", fg="#24cb5b", bg="#040404")
    lb1.place(x=200, y=30)

    img = PhotoImage(file="img/spotify-logo.png")


    btn1 = Button(window, image=img, width=160, height=120, bd=2, bg="#040404", command=get_tela2)
    btn1.place(x=170, y=90)

    window.mainloop()



tela1()