import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
import os

c = os.path.dirname(__file__)
nomeArquivo = c+'\\nomes.txt'


def ConexaoBanco():
    caminho = r'C:\Users\rjgug\OneDrive\Documentos\Python MACH556\MACH556.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print('Erro na conexão com BD.')
        print(ex)
    return con


vcon = ConexaoBanco()


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido.')
    except Error as ex:
        print('Erro na inserção de dados.')
        print(ex)


def gravarDados():
    if tb_cpf.get() != '':
        vcpf = tb_cpf.get()
        vnome = tb_nome.get()
        vtel = tb_tel.get()
        vend = tb_end.get()
        vnum = tb_num.get()
        vbairro = tb_bairro.get()
        vemail = tb_email.get()
        vobs = tb_obs.get('1.0', END)
        vsql = 'INSERT INTO tb_clientes' \
               '    (CPF, NOME, TELEFONE, ENDERECO, NUMERO, BAIRRO, EMAIL, OBS)' \
               'VALUES("' + vcpf + '", "' + vnome + '", "' + vtel + '", "' + vend + '", "' + vnum + '", "' + vbairro + '", "' + vemail + '", "' + vobs + '")'
        inserir(vcon, vsql)
        tb_cpf.delete(0, END)
        tb_nome.delete(0, END)
        tb_tel.delete(0, END)
        tb_end.delete(0, END)
        tb_num.delete(0, END)
        tb_bairro.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete('1.0', END)
        print('Dados gravados!')
    else:
        print('ERRO!')


def msg():
    messagebox.showinfo(title='BD', message='Dados gravados!')


app = Tk()
app.title('MACH556 Informática')
app.geometry('700x550')
app.configure(bg='#585858')

imgLogo = PhotoImage(file=c+'\\Logo.gif')
l_logo = Label(app, image=imgLogo)
l_logo.place(x=80, y=5)

Label(app, text='CPF', bg='#585858', fg='#F2F2F2', anchor=W).place(x=10, y=110, width=100, height=20)
tb_cpf = Entry(app)
tb_cpf.place(x=10, y=130, width=200, height=20)

Label(app, text='Nome', bg='#585858', fg='#F2F2F2', anchor=W).place(x=230, y=110, width=100, height=20)
tb_nome = Entry(app)
tb_nome.place(x=230, y=130, width=200, height=20)

Label(app, text='Telefone', bg='#585858', fg='#F2F2F2', anchor=W).place(x=460, y=110, width=100, height=20)
tb_tel = Entry(app)
tb_tel.place(x=460, y=130, width=200, height=20)

Label(app, text='Endereço', bg='#585858', fg='#F2F2F2', anchor=W).place(x=10, y=160, width=100, height=20)
tb_end = Entry(app)
tb_end.place(x=10, y=180, width=200, height=20)

Label(app, text='Numero', bg='#585858', fg='#F2F2F2', anchor=W).place(x=230, y=160, width=100, height=20)
tb_num = Entry(app)
tb_num.place(x=230, y=180, width=200, height=20)

Label(app, text='Bairro', bg='#585858', fg='#F2F2F2', anchor=W).place(x=460, y=160, width=100, height=20)
tb_bairro = Entry(app)
tb_bairro.place(x=460, y=180, width=200, height=20)

Label(app, text='E-Mail', bg='#585858', fg='#F2F2F2', anchor=W).place(x=10, y=210, width=100, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=230, width=300, height=20)

Label(app, text='OBS', bg='#585858', fg='#F2F2F2', anchor=W).place(x=10, y=260, width=100, height=20)
tb_obs = Text(app)
tb_obs.place(x=10, y=280, width=650, height=100)

Button(app, text='GRAVAR', command=gravarDados, bg='#fff').place(x=300, y=450, width=100, height=50)

app.mainloop()
