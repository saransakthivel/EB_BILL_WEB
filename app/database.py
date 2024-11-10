from sqlalchemy import create_engine

CONNECTION_STRING = "mssql+pyodbc://sa:RPSsql12345@45.127.108.208:5863/SQLEXPRESS/PssDataExport?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(CONNECTION_STRING)