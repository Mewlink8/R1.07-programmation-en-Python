def Exercice 1() :
x = 1
y = 2
t = 0
t= x
x = y
y = t
print('x=', x, 'y=', y)
  
def Exercice 2 (): 
 age = int(input("donnez votre age : ")) 
 annee = int(input("donner l'année actuelle : ")) 
 result = annee-age print("votre annee de naissance est : ", result) 

def exercice 3():
 a=input("Entrez la premiere valeur : ") 
 b=input("Entrez la deuxieme valeur : ")
 c=input("Entrez la troisieme valeur : ")
 print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
 print("Permutation : a ==> b, b ==> c, c ==> a") 
 print("Les valeurs permutees sont : a = " + c + ", b = " + a + " et c = " + b)
 
def exerice 4 ():
base = int(input("donnez le nombre de personne : ")) 
fromage = base * 200.0 
eau = base / 2 
goussedail = base / 2 
pain = base *100.0 
print("Pour faire une fondue avec", base, "personne, il faut :", fromage, "gr de fromage", eau,"dl d'eau", goussedail, "gousse d'aile", pain,"gr de pain")

def exerice 5 ():
nombre = int(input("Entrez un nombre entier :")) 
  if nombre%2 ==1 : 
    if nombre > 0 : print("Le nombre est positif et impair", nombre) 
    else : print("Le nombre est negatif et impair", nombre) 
  else : 
    if nombre < 0 : 
      print("Le nombre est negatif et pair",nombre) 
    else : 
      print("Le nombre est positif et pair",nombre)

def exercice 6 (): 
  from random import * 
  nombre = (randint(0,100)) 
    if nombre >50 : 
      print("Face", nombre) 
  else : print("Pile", nombre)
  
  
def exercice 7 (): 
  from random import * 
  nombre = (randint(1,3)) 
    if nombre ==1 :
      print("Face" ) 
    else : print("Pile")
      
def exerice 8  ():
  x = float(input("Entre nombre:")) 
    if (x >= -10 and x <= -2) or (x > 0 and x <= 1) or (x >= 2 and x < 3): 
      print(x,"appartient a I") 
    else: 
      print("n'apartient pas à I")
