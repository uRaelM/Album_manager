from tkinter import *


def arquivo():
    dados = []

    rnome = str(entrada_nome.get())
    dados.append(rnome)

    rnascimento = str(entrada_nascimento.get())
    dados.append(rnascimento)

    rcpf = str(entrada_CPF.get())
    dados.append(rcpf)

    rmatricula = str(entrada_matricula.get())
    dados.append(rmatricula)

    dados_p_salvar = ' | '.join(dados)
    dados_para_salvar = dados_p_salvar + '\n'
    executar = open('arquivo.txt', 'a', encoding='utf-8')
    executar.write(dados_para_salvar)
    executar.close()
    dados = []

"janela:"
window = Tk()
window.title('Trabalho de LNPG')
window.geometry('500x250')
dados = []

"Labels e Entry:"
nome = Label(window, text='Nome: ', font=14).pack()
entrada_nome = Entry(window)
entrada_nome.pack()
nascimento = Label(window, text='Nascimento: ', font=14).pack()
entrada_nascimento = Entry(window)
entrada_nascimento.pack()
cpf = Label(window, text='CPF:', font=14).pack()
entrada_CPF = Entry(window)
entrada_CPF.pack()
matricula = Label(window, text='Matricula: ', font=14).pack()
entrada_matricula = Entry(window)
entrada_matricula.pack()

"botão e loop"
botao_salvar = Button(window, text='Cadastrar', command=arquivo).place(x=220, y=200)
window.mainloop()
