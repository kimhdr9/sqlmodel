from models import engine,Hero
from sqlmodel import Session, select
"""
une session à la base de données
"""
session=Session(engine)
"""
équivalent select * from hero avec une condition where
"""
statement=select(Hero).where(Hero.age == 17).where(Hero.name=="Badman")
"""
exécution de la commande select
"""
results=session.exec(statement)
"""
affichage du resultat
"""
for hero in results :
    print(hero)
"""
fermeture de la session
"""
session.close()