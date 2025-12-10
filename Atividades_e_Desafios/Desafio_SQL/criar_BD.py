
import sqlite3


conn = sqlite3.connect('meu_banco.db')

print("Conexão bem-sucedida ao banco de dados SQLite")

conn.close()