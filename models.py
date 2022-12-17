from db.config import user,password,port,host,base
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id : Optional[int] = Field(default=None,primary_key=True)
    name : str
    secret_name :str
    age : Optional[int] = None

"""
chaine de connexion pour une connexion à postgres
"""
chaine_cnx=f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{base}"
"""
en mode verbeux => echo=True
"""
engine=create_engine(chaine_cnx,echo=False)
"""
création de la table Hero
opération de migration de 
"""
def create_db_and_tables() :
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    """
    l'appel en mode principal crée la base de données
    """
    create_db_and_tables()