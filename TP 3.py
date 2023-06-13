def exercice  1() : 

exercice 1 A)
  n = int(input("enter le nombre d'entier a saisir: "))
  i=0
  temp = 0
  while i<n+1:
    temp = temp+i
    i= i+1
  print(temp) 


exercice 1 B)
  x=0
  while x !=100:
    x = int(input("Entrer la valeur 100 : ")) 
    
    
exercice 1 C)
  i = 0
  x=0
  a=0
  b=0
  c=0
  while i<10:
    x = int(input("entrer la valeur entre 0 et 20 : "))
    if x>=0 and x<=20:
        if x<10:
            a=a+1
            i = i + 1
        elif x>=10 and x<15:
            b=b+1
            i = i + 1
        elif x>=15 and x<20:
            c=c+1
            i = i + 1
  print(f" Le nombre de valeurs inférieur strictement à 10 est {a}")
  print(f" Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est {b}")
  print(f" Le nombre de valeurs supérieur ou égale à 15 est {c}") 


exercice 1 D)
  add= 0
  i=0
  x=0
  while x<=1:
    x = int(input("entrer une valeur: "))
  while add !=x  :
    add = add+i
    if add>x:
        print("il n'y a pas de solution")
        break
    elif add == x:
        print(f"le nombre rechercher est {i} pour la valeur {x} ")
    else:
        i = i + 1 
        

def exercice 2 FOR ()
  from time import*
  print("Entre un nombre")
  l = input()
  l = int(l)
  r = range(l)
  for i in reversed (r):
      print(i)
      sleep(0.2)
    
    
def exercice 2 WHILE()
  from time import*
  print("Entrez un nombre")
  n = int(input())
  while n != 0:
      print(n)
      n = n - 1
      sleep(0.2)


def exercice 3(): 
  import random
  x = random.randint(0 , 100)
  nombre = input("Entre une valeur" "\n")
  nombre = int(nombre)
  tour = 0
  tour = int(tour)
  while nombre != x:
    if nombre > x:
      print("La valeur entrée est trop grande")
      nombre = int(input("Entrez une valeur")
      tour = tour + 1
    elif nombre < x:
      print("La valeur entrée est trop petite" "\n")
      nombre = int(input("Entrez une valeur" "\n"))
      tour = tour + 1
      
      
def exercice 4 (): 
  n = int(input("entrer une valeur: "))
  case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))
  fact = n
  i=0
  if case == 0:
    while i != n-1:
        i = i+1
        fact = n-i
    print(f"le factoriel de {n} et {fact}")
  elif case == 1:
    for i in range(n-1):
        fact= n-(i+1)
    print(f"le factoriel de {n} et {fact}")
  else:
    case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))

def exercice 5 ():
  tarif = 0
  debut = 0
  un = 0
  deux = 0
  debut = int(input("Donnez l’heure de début de la location (un entier) : "))
  fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
  while debut == fin or debut>fin or debut<0 or debut>24 or fin>24 or fin<0:
    if debut==fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    elif debut>fin:
        print("Attention ! le début de la location est après la fin ...\n")
    elif debut<0 or debut>24 or fin>24 or fin<0:
        print("Les heures doivent être comprises entre 0 et 24 ! \n")
    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
  for i in range(debut, fin):
    if debut>=0 and debut<7 or debut>=17 and debut<24:
        tarif = tarif+1
        debut = debut+1
        un = un+1
    elif debut>=7 and debut<17:
        tarif = tarif+2
        debut = debut+1
        deux = deux +1
  print("Vous avez loué votre vélo pendant")
  print(f"{un} heure(s) au tarif horaire de 1.0 euro(s)")
  print(f"{deux} heure(s) au tarif horaire de 2.0 euro(s)")
  print(f"Le montant total à payer est de {tarif} euro(s).")
