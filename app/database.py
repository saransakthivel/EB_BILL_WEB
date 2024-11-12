from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#CONNECTION_STRING = "mssql+pyodbc://sa:RPSsql12345@localhost:1433/test?driver=ODBC+Driver+17+for+SQL+Server"
CONNECTION_STRING = "mssql+pyodbc://sa:RPSsql12345@45.127.108.208:231/etest?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)