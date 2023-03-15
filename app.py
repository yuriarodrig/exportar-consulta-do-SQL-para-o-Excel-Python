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
