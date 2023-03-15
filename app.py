import os
import pandas as pd
import pyodbc
import conect as cn #Importando arquivo de password para a segurança de conexão bd

#Conexão BD 
server = cn.server
database = cn.database
username = cn.username
password = cn.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)

cursor = conn.cursor()

#Minha query para consultar no bd
query = '''SELECT X6_VAR AS NOME, X6_DESCRIC AS DESCRICAO, X6_DESC1, X6_DESC2  AS DESCRICAO2 FROM SX6010
WHERE

X6_VAR = 'MV_SUBTRIB' OR X6_VAR = 'MV_STUFS' OR X6_VAR = 'MV_STUF'
'''

df = pd.read_sql(query, con=conn) #Consulto
df.to_excel('query sql.xlsx', index=False) #Cria um arquivo Excel
