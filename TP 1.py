def exercice 1 (): 
  nom = "toto"
  prenom = "titi"
  math = 12
  anglais = 15
  info = 12.5
  promotion = 2022
  moy = (math+anglais+info)/3
  print(type(nom),type(prenom),type(math),type(anglais),type(info),type(promotion),type(moy))
  print("L'étudiant",nom,prenom,"de la promotion",promotion,"a une moyenne de",moy)

def exercice 2(): 
  jour = 18
  heure = 13
  minute = 40
  print(minute+(heure*60)+(jour*1440))

def exercice 3 (): 
  jour = int(input("donne jour:"))
  heure = int(input("donne heure:"))
  minute = int(input("donne minute:"))
 
  if jour > 31 or jour < 0:
    print("tu te fous de moi ?"))
    jour = int(input("donne jour:"))
  if heure > 24 or heure < 0:
    print("tu te fous de moi ?"))
    heure = int(input("donne heure:"))
  if minute > 60 or heure < 0:
    print("tu te fous de moi ?"))
    minute = int(input("donne minute:"))
  print(minute+(heure60)+(jour1440))
  
  
def exercice 4 (): 
  x = int(input("nombre de seconde:"))
  x=x/86400
  print(x)

def exercice 5():
  from random import *
  print(randint(0,100))
  
