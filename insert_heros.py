from models import engine,Hero
from sqlmodel import Session
from faker import Faker
import random

superHero=['Tarzan','Miles Davis','Toroto','Super Jamie','Jane']
age=[10,12,15,19,23,34,48,69]

"""
on ouvre une session sur le moteur sql
"""
session=Session(engine)
"""
identites bidons français
"""
faux=Faker('fr_FR')

"""
création d'une instance Hero
"""
for _ in range(4) :
    nom=faux.name()
    random_hero=random.choice(superHero)
    random_age=random.choice(age)
    hero=Hero(name=random_hero,secret_name=nom,age=random_age)
    """
    on l'ajoute à la DB
    """
    session.add(hero)
"""
on confirme
"""
session.commit()
"""
on ferme la session
"""
session.close()