from models import engine,Hero
from sqlmodel import Session, select
"""
une session à la base de données
"""
session=Session(engine)
"""
équivalent select * from hero avec une condition where
"""
statement=select(Hero).where(Hero.age == 25).where(Hero.name=="Badman")
"""
exécution de la commande select
"""
results=session.exec(statement)
"""
récupère le résultat
"""
hero=results.one()
"""
on modifie l'age
"""
hero.age=21
"""
ajoute et sauve la modification
"""
session.add(hero)
session.commit()
"""
rafraichir les modifications
"""
session.refresh(hero)
print(" hero :",hero)
"""
fermeture de la session
"""
session.close()