from tkinter import *


albuns = []
dados = []
def arquivo():
    dados = []

    ialbum = str(entrada_album.get())
    dados.append(ialbum)
    albuns.append(ialbum)

    ilançamento = str(entrada_ano_lancamento.get())
    dados.append(ilançamento)

    ibanda_artista = str(entrada_banda_artista.get())
    dados.append(ibanda_artista)

    isim_nao = str(entrada_sim_nao.get())
    dados.append(isim_nao)

    dados_p_salvar = ' | '.join(dados)
    dados_para_salvar = dados_p_salvar + '\n'
    executar = open('arquivo.txt', 'a', encoding='utf-8')
    executar.write(dados_para_salvar)
    print(albuns)
    executar.close()

"janela:"
window = Tk()
window.title('Versão 1.0')
window.geometry('500x250')

"Labels e Entry:"
album = Label(window, text='Álbum: ', font=14).pack()
entrada_album = Entry(window)
entrada_album.pack()
ano_lancamento = Label(window, text='Ano de lançamento: ', font=14).pack()
entrada_ano_lancamento = Entry(window)
entrada_ano_lancamento.pack()
banda_artista = Label(window, text='Banda/Artista:', font=14).pack()
entrada_banda_artista = Entry(window)
entrada_banda_artista.pack()
ultimo_album = Label(window, text='Ultimo album de lançamento(Sim/Não):', font=14).pack()
entrada_sim_nao = Entry(window)
entrada_sim_nao.pack()

"botão e loop"
botao_salvar = Button(window, text='cadastrar', command=arquivo).place(x=150, y=200)
botao_buscar = Button(window, text='Lista de Álbuns', command=arquivo).place(x=260, y=200)
window.mainloop()
