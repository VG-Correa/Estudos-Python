from datetime import date, datetime
import datetime
from genericpath import exists
from locale import strcoll
from tkinter import messagebox, ttk
from tkinter import *
from types import NoneType
from numpy import place
import pandas as pd
from pandas import DataFrame
import openpyxl
# import Banco_de_dados 
import sqlite3
from sqlite3 import Error

from setuptools import Command
import Banco_de_dados

# criar conexão
conexão = Banco_de_dados.ConexaoBancoDados()

#criando banco de dados caso não exista:

#Variáveis para inserção do banco de dados:
BD = "TB_Coletas"
Cód = "2"
Data = "05/05/2022"
Familia = "Asteraceae"
NomeComum = ""
Gênero = "Onix"
Espécie = "Carro"
Hábito = ""
Recurso = ""
Origem = ""
Referência = ""
CampoColeta = ""

#### Colunas:
Col_Cód = ""
Col_Data = ""
Col_Fam = ""
Col_Gen = ""
Col_Esp = ""
Col_Nome = ""
Col_Háb = ""
Col_Rec = ""
Col_Ori = ""
Col_Ref = ""
Col_Camp = ""


#------------------------------------------

Banco_de_dados.CriarTabela(conexão,Banco_de_dados.vsql)


Nova_Lista = Banco_de_dados.vsqlInserir(BD,Col_Cód,Data,Familia,Gênero,Espécie,NomeComum,Hábito,Recurso,Origem,Referência,CampoColeta)
print(Nova_Lista)
#----Para inserir linhas no banco de dados-----
# Banco_de_dados.inserir(conexão,Nova_Lista)

#----Para deletar linhas no banco de dados a partir do ID--------
# Banco_de_dados.deletar(conexão,Banco_de_dados.vsqlDeletar(BD,1))

#----Para atualizar um dado específico no banco de dados--------------------------------
# Banco_de_dados.Atualizar(conexão,Banco_de_dados.vsqlAtualizar(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Háb,Col_Rec,Col_Ori,Col_Ref))

#----Para consultar a tablea principal--------------------------
# Tabela_Principal = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsultaPrincipal(BD))
# for n in Tabela_Principal:
#     print(n)


# #----Para consultar informações específicas da tabela----------------------------------------
# Col_Fam = "Mangaceae"
# Consulta = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsulta(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Háb,Col_Rec,Col_Ori,Col_Ref))
# for n in Consulta:
#     print(n)

root = Tk()

class Janela_Principal:
    
    def __init__(self):
        self.root = root
        self.Janela()
        self.Frames_MenuPrincipal()
        self.botões_MenuPrincipal()
        self.Label_ManuPrincipal()
        self.Coletas()
        self.Relatórios()
        self.botões_MenuRelatórios()
        self.root.mainloop()

    def Janela(self):
        self.root.title("UMCientist")
        self.root.configure(background="DarkGreen")
        self.root.geometry("1200x700")
        self.root.resizable(True,True)
        self.root.minsize(width="1200",height="700")
    def Frames_MenuPrincipal(self):
        #---------------------------Menu de botões principal----------------------------
        self.frame_Menu = Frame(self.root, bd=4, bg="Gainsboro",highlightbackground= "Green",highlightthickness=0.5)
        self.frame_Menu.place(relx=0.005,rely=0.005,relwidth=0.30,relheight=0.48)
      
        #---------------------------Menu de relatórios gráficos-------------------------
        self.frame_relatórios = Frame(self.root, bd=4, bg="Gainsboro",highlightbackground= "Green",highlightthickness=0.5)
        self.frame_relatórios.place(relx=0.50,rely=0.005,relwidth=0.495,relheight=0.48)
        #---------------------------Menu para visualizar planilha-------------------------
        self.frame_VisPlanilha = Frame(self.root, bd=4, bg="Gainsboro",highlightbackground= "Black",highlightthickness=0.5)
        self.frame_VisPlanilha.place(relx=0.005,rely=0.50,relwidth=0.99,relheight=0.49)
    def Label_ManuPrincipal(self):
        #---------------------------Código de coleta--------------------------------------
        Cód_coletatextY = 0.0005
        Cód_coletaLabelY = Cód_coletatextY + 0.055
        self.Label_CódColeta = Label(self.frame_Menu,text="Cód",background="Gainsboro",fg="DarkGreen")
        self.Label_CódColeta.place(relx=0.005,rely=Cód_coletatextY)
        global Campo_CódColeta
        Campo_CódColeta = Entry(self.frame_Menu)
        Campo_CódColeta.place(relx=0.01,rely=Cód_coletaLabelY,relwidth=0.1,relheight=0.05)
        

        #---------------------------Data da coleta--------------------------------------
        Cód_DatacoletatextY = 0.0005
        Cód_DatacoletaLabelY = Cód_DatacoletatextY + 0.055
        self.Label_DataColeta = Label(self.frame_Menu,text="Data coleta",background="Gainsboro",fg="DarkGreen")
        self.Label_DataColeta.place(relx=0.15,rely=Cód_DatacoletatextY)
        global Campo_DataColeta
        Campo_DataColeta = Entry(self.frame_Menu)
        Campo_DataColeta.place(relx=0.15,rely=Cód_DatacoletaLabelY,relwidth=0.16,relheight=0.05)

        #---------------------------Família--------------------------------------
        Cód_FamiliatextY = Cód_coletatextY
        Cód_FamiliaLabelY = Cód_FamiliatextY + 0.055
        self.Label_Familia = Label(self.frame_Menu,text="Família",background="Gainsboro",fg="DarkGreen")
        self.Label_Familia.place(relx=0.40,rely=Cód_FamiliatextY)
        global Campo_Familia
        Campo_Familia = Entry(self.frame_Menu)
        Campo_Familia.place(relx=0.35,rely=Cód_FamiliaLabelY,relwidth=0.255,relheight=0.05)

        #---------------------------Gênero--------------------------------------
        Cód_GenerotextY = Cód_FamiliaLabelY	+ 0.05
        Cód_GeneroLabelY = Cód_GenerotextY + 0.055
        self.Label_Genero = Label(self.frame_Menu,text="Gênero",background="Gainsboro",fg="DarkGreen")
        self.Label_Genero.place(relx=0.005,rely=Cód_GenerotextY)
        global Campo_Genero
        Campo_Genero = Entry(self.frame_Menu)
        Campo_Genero.place(relx=0.01,rely=Cód_GeneroLabelY,relwidth=0.3,relheight=0.05)
        
        #---------------------------Espécie--------------------------------------
        Cód_EspécietextY = Cód_GenerotextY
        Cód_EspécieLabelY = Cód_EspécietextY + 0.055
        self.Label_Espécie = Label(self.frame_Menu,text="Espécie",background="Gainsboro",fg="DarkGreen")
        self.Label_Espécie.place(relx=0.35,rely=Cód_EspécietextY)
        global Campo_Espécie
        Campo_Espécie = Entry(self.frame_Menu)
        Campo_Espécie.place(relx=0.35,rely=Cód_EspécieLabelY,relwidth=0.255,relheight=0.05)

        #---------------------------Hábito--------------------------------------
        Cód_HabitotextY = Cód_GeneroLabelY + 0.05
        Cód_HabitoLabelY = Cód_HabitotextY + 0.055
        self.Label_Hábito = Label(self.frame_Menu,text="Hábito",background="Gainsboro",fg="DarkGreen")
        self.Label_Hábito.place(relx=0.005,rely=Cód_HabitotextY,height=15)
        global Campo_Hábito
        Campo_Hábito = Entry(self.frame_Menu)
        Campo_Hábito.place(relx=0.01,rely=Cód_HabitoLabelY,relwidth=0.3,relheight=0.05)

        #---------------------------Nome comum--------------------------------------
        Cód_NomeComumtextY = Cód_EspécieLabelY	+ 0.05
        Cód_NomeComumLabelY = Cód_NomeComumtextY + 0.055
        self.Label_NomeComum = Label(self.frame_Menu,text="Nome Comum",background="Gainsboro",fg="DarkGreen")
        self.Label_NomeComum.place(relx=0.35,rely=Cód_NomeComumtextY)
        global Campo_NomeComum
        Campo_NomeComum = Entry(self.frame_Menu)
        Campo_NomeComum.place(relx=0.35,rely=Cód_NomeComumLabelY,relwidth=0.255,relheight=0.05)

        #---------------------------Recurso--------------------------------------
        Cód_RecursotextY = Cód_HabitoLabelY	+ 0.05
        Cód_RecursoLabelY = Cód_RecursotextY + 0.055
        self.Label_Recurso = Label(self.frame_Menu,text="Recurso Fornecido",background="Gainsboro",fg="DarkGreen")
        self.Label_Recurso.place(relx=0.005,rely=Cód_RecursotextY)
        global Campo_Recurso
        Campo_Recurso = Entry(self.frame_Menu)
        Campo_Recurso.place(relx=0.01,rely=Cód_RecursoLabelY,relwidth=0.3,relheight=0.05)


        #---------------------------Origem--------------------------------------
        Cód_OrigemtextY = Cód_RecursotextY
        Cód_OrigemLabelY = Cód_OrigemtextY + 0.055
        self.Label_Origem = Label(self.frame_Menu,text="Origem",background="Gainsboro",fg="DarkGreen")
        self.Label_Origem.place(relx=0.35,rely=Cód_OrigemtextY)
        global Campo_Origem
        Campo_Origem = Entry(self.frame_Menu)
        Campo_Origem.place(relx=0.35,rely=Cód_OrigemLabelY,relwidth=0.255,relheight=0.05)

        #---------------------------Referência--------------------------------------
        Cód_ReferenciatextY = Cód_OrigemLabelY	+ 0.05
        Cód_ReferenciaLabelY = Cód_ReferenciatextY + 0.055
        self.Label_Referencia = Label(self.frame_Menu,text="Referência",background="Gainsboro",fg="DarkGreen")
        self.Label_Referencia.place(relx=0.005,rely=Cód_ReferenciatextY)
        global Campo_Referencia
        Campo_Referencia = Entry(self.frame_Menu)
        Campo_Referencia.place(relx=0.01,rely=Cód_ReferenciaLabelY,relwidth=0.3,relheight=0.05)

        #---------------------------Campo--------------------------------------
        Cód_CampotextY = Cód_ReferenciatextY
        Cód_CampoLabelY = Cód_CampotextY + 0.055
        self.Label_Campo = Label(self.frame_Menu,text="Campo de coleta",background="Gainsboro",fg="DarkGreen")
        self.Label_Campo.place(relx=0.35,rely=Cód_CampotextY)
        global Campo_CampoColeta
        Campo_CampoColeta = Entry(self.frame_Menu)
        Campo_CampoColeta.place(relx=0.35,rely=Cód_CampoLabelY,relwidth=0.255,relheight=0.05)


#--------------------------------Relatórios-------------------------------------
   
    def Relatórios(self):
        self.qtd_coletas = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsultaPrincipal(BD))
        self.qtd_coletas = len(self.qtd_coletas)

        self.qtd_familias = Banco_de_dados.Consulta(conexão,Banco_de_dados.consultaRelatório(BD,"Família","!=","N/Id"))
        self.qtd_familias = len(self.qtd_familias)
        self.porc_familias = round((self.qtd_familias / self.qtd_coletas)*100)

        self.rel_qtd_coletas = Label(self.frame_relatórios,text=f"Quantidade de coletas: {self.qtd_coletas}")
        self.rel_qtd_coletas.place(relx=0.005)

        self.rel_familiasidentificadas = Label(self.frame_relatórios,text=f"Famílias identificadas: {self.qtd_familias} | {self.porc_familias}%")
        self.rel_familiasidentificadas.place(relx=0.005,rely=0.07)

        self.qtd_familias_Nid = self.qtd_coletas - self.qtd_familias
        self.rel_famnaoidentificadas = Label(self.frame_relatórios,text=f"Famílias não identificadas: {self.qtd_familias_Nid} | {100 - self.porc_familias}%")
        self.rel_famnaoidentificadas.place(relx=0.005,rely=0.14) 


        self.qtd_generos = Banco_de_dados.Consulta(conexão,Banco_de_dados.consultaRelatório(BD,"Gênero","!=","N/Id"))
        self.qtd_generos = len(self.qtd_generos)
        self.porc_generos = round((self.qtd_generos / self.qtd_coletas)*100)

        self.rel_generoIdentificados = Label(self.frame_relatórios,text=f"Identificados até Gênero: {self.qtd_generos} | {self.porc_generos}%")
        self.rel_generoIdentificados.place(relx=0.005,rely=0.21)

        self.rel_generoNidentificados = Label(self.frame_relatórios,text=f"Gêneros não identificados: {self.qtd_coletas - self.qtd_generos} | {100 - self.porc_generos}%")
        self.rel_generoNidentificados.place(relx=0.005,rely=0.28)

        self.qtd_especies = Banco_de_dados.Consulta(conexão,Banco_de_dados.consultaRelatório(BD,"Espécie","!=","N/Id"))
        self.qtd_especies = len(self.qtd_especies)
        self.porc_especies = round((self.qtd_especies / self.qtd_coletas)*100)

        self.rel_especiesIdentificadas = Label(self.frame_relatórios,text=f"Espécies identificadas: {self.qtd_especies} | {self.porc_especies}%")
        self.rel_especiesIdentificadas.place(relx=0.005,rely=0.35)

        self.rel_especiesNidentificadas = Label(self.frame_relatórios,text=f"Espécies não identificadas: {self.qtd_coletas - self.qtd_especies} | {100 - self.porc_especies}%")
        self.rel_especiesNidentificadas.place(relx=0.005,rely=0.42)




        self.qtd_duvidosos = Banco_de_dados.Consulta(conexão,Banco_de_dados.consultaDuvidosos(BD))
        self.qtd_duvidosos = len(self.qtd_duvidosos)
        self.porc_duvidosos = round((self.qtd_duvidosos / self.qtd_coletas)*100)

        self.rel_Duvidosos = Label(self.frame_relatórios,text=f"Duvidosos: {self.qtd_duvidosos} | {self.porc_duvidosos}%")
        self.rel_Duvidosos.place(relx=0.005,rely=0.49)



    def botões_MenuRelatórios(self):
    
        self.bt_atualizarrelatório = Button(self.frame_relatórios,text="Atualizar",command=self.Relatórios)
        self.bt_atualizarrelatório.place(relx=0.90,rely=0.005)

    def botões_MenuPrincipal(self):
        
        self.bt_AdicionarColeta = Button(self.frame_Menu,text="Adicionar nova coleta",bg="lightGreen",fg="DarkGreen",command=BotãoAddColeta)
        self.bt_AdicionarColeta.place(relx=0.65,rely=0.003,relwidth=0.35,relheight=0.07)

        self.bt_ExcluirColena = Button(self.frame_Menu,text="Excluir Coleta",bg="Red",command=ExcluirColeta)
        self.bt_ExcluirColena.place(relx=0.65,rely=0.080,relwidth=0.35,relheight=0.07)

        self.bt_AlterarColeta = Button(self.frame_Menu,text="Alterar Coleta",bg="Yellow",command=AlterarColeta)
        self.bt_AlterarColeta.place(relx=0.65,rely=0.155,relwidth=0.35,relheight=0.07)

        self.bt_Filtrar = Button(self.frame_Menu,text="Filtrar",bg="#f6f5da",command=Filtrar)
        self.bt_Filtrar.place(relx=0.65,rely=0.23,relwidth=0.150,relheight=0.07)

        self.bt_Todos = Button(self.frame_Menu,text="Todos",bg="#f6f5da",command=popular)
        self.bt_Todos.place(relx=0.85,rely=0.23,relwidth=0.150,relheight=0.07)

        self.bt_Limpar = Button(self.frame_Menu,text="Limpar Campos",bg="#e3e3d1",command=LimparCampos)
        self.bt_Limpar.place(relx=0.65,rely=0.305,relwidth=0.35,relheight=0.07)

    def Coletas(self):
        global coletas
        coletas = ttk.Treeview(self.frame_VisPlanilha,columns=("Cod_Coleta","Data_Coleta","Família","Gênero","Espécie","NomeComum","Hábito","Recurso","Origem","Referência","Campo de Coleta"))

        coletas.column("#0",width=0)
        coletas.column("#1",width=75)
        coletas.column("#2",width=100)
        coletas.column("#3",width=100)
        coletas.column("#4",width=100)
        coletas.column("#5",width=100)
        coletas.column("#6",width=100)
        coletas.column("#7",width=100)
        coletas.column("#8",width=100)
        coletas.column("#9",width=50)
        coletas.column("#10",width=150)
        coletas.column("#11",width=100)

        coletas.heading("#0",text="")
        coletas.heading("#1",text="Cod coleta")
        coletas.heading("#2",text="Data")
        coletas.heading("#3",text="Família")
        coletas.heading("#4",text="Gênero")
        coletas.heading("#5",text="Espécie")
        coletas.heading("#6",text="Nome Comum")
        coletas.heading("#7",text="Hábito")
        coletas.heading("#8",text="Recurso")
        coletas.heading("#9",text="Origem")
        coletas.heading("#10",text="Referência")
        coletas.heading("#11",text="Campo")

        global linhas
        linhas = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsultaPrincipal(BD))
        for i in linhas:
            coletas.insert("","end",value=i)        

        coletas.place(relx=0.005,rely=0.005,relheight=0.99,relwidth=0.92)
        

        self.scroollist = Scrollbar(self.frame_VisPlanilha,orient="vertical")
        coletas.configure(yscrollcommand=self.scroollist.set)
        self.scroollist.place(relx=0.93,rely=0.010,relwidth=0.063,relheight=0.98)


def BotãoAddColeta():
    verificador = ""
    Col_Cód = Campo_CódColeta.get()
    if Col_Cód == "":
        pass
    else:
        if not(VerificarCód(Col_Cód)):
            verificador = verificador + f"O código precisa ser um número válido\n"

    Col_Data = Campo_DataColeta.get()
    
    Col_Data = VerificarData(Col_Data)

    if Col_Data == "Data inválida":
        verificador = verificador + f"A data é inválida!\n"
    
    Col_Fam = Campo_Familia.get()
    Col_Fam = Col_Fam.title()
    Col_Gen = Campo_Genero.get()
    Col_Gen = Col_Gen.title()
    Col_Esp = Campo_Espécie.get()
    Col_Esp = Col_Esp.lower()
    Col_Nome = Campo_NomeComum.get()
    Col_Nome = Col_Nome.title()
    Col_Háb = Campo_Hábito.get()
    Col_Háb = Col_Háb.title()
    Col_Rec = Campo_Recurso.get()
    Col_Rec = Col_Rec.title()
    Col_Ori = Campo_Origem.get()
    Col_Ori = Col_Ori.title()
    Col_Ref = Campo_Referencia.get()
    Col_Camp = Campo_CampoColeta.get()
    Col_Camp = Col_Camp.title()

    if verificador == "":      
        Banco_de_dados.inserir(conexão,Banco_de_dados.vsqlInserir(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Nome,Col_Háb,Col_Rec,Col_Ori,Col_Ref,Col_Camp))

        popular()
        print("Coleta adicionada")
        Janela_Principal.Relatórios()
    else:
        messagebox.showerror("ATENÇÃO!",verificador)
    
    

def ExcluirColeta():
    BD = "TB_Coletas"
    Col_Cód = Campo_CódColeta.get()
    Col_Cód = int(Col_Cód)
            
    Existe_na_lista = 0

    if Col_Cód == "":
        messagebox.showerror("ATENÇÃO!","Para excluir uma coleta, informe o código de coleta no campo correspondente")
    else:

        for i in linhas:
            for e in i:
                if e == Col_Cód:
                    Existe_na_lista += 1
     
        if Existe_na_lista == 0:
            messagebox.showerror("ATENÇÃO!","O código de coleta inserido não foi localizado! Verifique se ele está correto")             
        else:

            Confirmação = messagebox.askokcancel("ATENÇÃO!",f"Você realmente deseja excluir a coleta {Col_Cód}?")
            if Confirmação == True:
                Banco_de_dados.deletar(conexão,Banco_de_dados.vsqlDeletar(BD,Col_Cód))
                popular()
                messagebox.showinfo("Dados atualizados",f"A coleta {Col_Cód} foi excluída do banco de dados!")
                LimparCampos()
    

def AlterarColeta():
    BD = "TB_Coletas"
    verificador = ""
    Col_Cód = Campo_CódColeta.get()
    if Col_Cód == "":
        pass
    else:
        if not(VerificarCód(Col_Cód)):
            verificador = verificador + f"O código precisa ser um número válido\n"
            
    Col_Data = Campo_DataColeta.get()
    
    if Col_Data == "":
        pass
    else:
        Col_Data = VerificarData(Col_Data)

    if Col_Data == "Data inválida":
        verificador = verificador + f"A data é inválida!\n"
    
    Col_Fam = Campo_Familia.get()
    Col_Fam = Col_Fam.title()
    Col_Gen = Campo_Genero.get()
    Col_Gen = Col_Gen.title()
    Col_Esp = Campo_Espécie.get()
    Col_Esp = Col_Esp.lower()
    Col_Nome = Campo_NomeComum.get()
    Col_Nome = Col_Nome.title()
    Col_Háb = Campo_Hábito.get()
    Col_Háb = Col_Háb.title()
    Col_Rec = Campo_Recurso.get()
    Col_Rec = Col_Rec.title()
    Col_Ori = Campo_Origem.get()
    Col_Ori = Col_Ori.title()
    Col_Ref = Campo_Referencia.get()
    Col_Camp = Campo_CampoColeta.get()
    Col_Camp = Col_Camp.title()

    if verificador == "":

        if Col_Cód == "":
            messagebox.showerror("ATENÇÃO!","Para alterar uma coleta, informe o Código de coleta e preencha a nova informação no seu devido campo")
        else:

            if messagebox.askokcancel("ATENÇÃO!",f"Deseja realmente alterar a coleta {Col_Cód}?") == True:
                Banco_de_dados.Atualizar(conexão,Banco_de_dados.vsqlAtualizar(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Nome,Col_Háb,Col_Rec,Col_Ori,Col_Ref,Col_Camp))
                popular()
    else:
        messagebox.showerror("ATENÇÃO!",verificador)

def Filtrar():
    BD = "TB_Coletas"
    Col_Cód = Campo_CódColeta.get()
    Col_Data = Campo_DataColeta.get()
    Col_Fam = Campo_Familia.get()
    Col_Gen = Campo_Genero.get()
    Col_Esp = Campo_Espécie.get()
    Col_Nome = Campo_NomeComum.get()
    Col_Háb = Campo_Hábito.get()
    Col_Rec = Campo_Recurso.get()
    Col_Ori = Campo_Origem.get()
    Col_Ref = Campo_Referencia.get()
    Col_Camp = Campo_CampoColeta.get()

    popularFiltro(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Nome,Col_Háb,Col_Rec,Col_Ori,Col_Ref,Col_Camp)

def LimparCampos():
    Campo_CódColeta.delete(0,END)
    Campo_DataColeta.delete(0,END)
    Campo_Familia.delete(0,END)
    Campo_Genero.delete(0,END)
    Campo_Espécie.delete(0,END)
    Campo_NomeComum.delete(0,END)
    Campo_Hábito.delete(0,END)
    Campo_Recurso.delete(0,END)
    Campo_Origem.delete(0,END)
    Campo_Referencia.delete(0,END)
    Campo_CampoColeta.delete(0,END)

def popular():
    global linhas
    linhas = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsultaPrincipal(BD))
    coletas.delete(*coletas.get_children())
    for i in linhas:
        coletas.insert("","end",value=i)

def popularFiltro(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Nome,Col_Háb,Col_Rec,Col_Ori,Col_Ref,Col_Camp):
    global linhas
    try:
        linhas = Banco_de_dados.Consulta(conexão,Banco_de_dados.vsqConsulta(BD,Col_Cód,Col_Data,Col_Fam,Col_Gen,Col_Esp,Col_Nome,Col_Háb,Col_Rec,Col_Ori,Col_Ref,Col_Camp))
               
        if linhas:
            coletas.delete(*coletas.get_children())
            for i in linhas:
                coletas.insert("","end",value=i)
        else:
            print("Não foi encontrado")
            messagebox.showerror("ATENÇÃO!","O filtro não foi aplicado! A informação não existe ou você não preencheu corretamente")
        
    except Error as er:
        print(er)

def VerificarData(data):
    
    data = str(data)
    if data == "":
        messagebox.showerror("ATENÇÃO","Para fazer isso é necessário inserir a data")
    data = data.split("/")
    dia = data[0]    
    mês = data[1]
    ano = data[2]

    if len(str(dia)) == 1:
        dia = f"0{dia}"
    
    if len(str(mês)) == 1:
        mês = f"0{mês}"

    if len(str(ano)) == 4:
        pass
    elif len(str(ano)) == 2:
        ano = f"20{ano}"
    
    data = f"{dia}/{mês}/{ano}"

    try:
        ver_data = datetime.datetime(int(ano),int(mês),int(dia))
        return data
    except:
        return "Data inválida"
        
def VerificarCód(CódigoColeta):
    Código = str(CódigoColeta)
    if not(Código.isdigit()):
        return False
    else:
        return True


Janela_Principal()
root.mainloop()
conexão.close()
