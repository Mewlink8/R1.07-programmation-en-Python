def exercice 1 ():
  table=[] 
  valeur = float(input("entrer la valeur a multiplier")) 
  for i in range(10): 
    result = valeur(i) 
    table.append(round(result,2)) 
    i=0 
  for i in range(10): 
    print(f"{valeur} {i} = {table[i]}")
    
def exerice 2 ():
  nombreEtudiants = int(input("Donnez le nombre d'etudiants : ")) 
  moyenne = 0.0; 
  # déclaration d’une liste vide qui va contenir autant de notes que d'étudiants 
  notes = [] 
  result = 0 
    for i in range(nombreEtudiants): 
      notes.append( float(input(f"Note de l'étudiant {i} : "))) 
    for i in range(nombreEtudiants): 
      result = notes[i] + result moyenne = result/nombreEtudiants 
      print(f"Moyenne de classe : {round(moyenne,2)}\n") 
      print("Numéro de l’Etudiant | note | ecart a la moyenne") 
    for i in range(nombreEtudiants): 
      print(f"{i} | {notes[i]} | {round((notes[i]-moyenne),2)}")

def exercice 3 ():
 nmax = 10 
 #taille max du vecteur 
 v1=[]
 v2=[] 
 n=0 
 i=0 
 scal=0 
 while n<1 or n >= nmax: 
 n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et 10] ? ")) 
 print("Saisie du premier vecteur : ") 
 while i !=n : 
 v1.append(int(input(f"v1[{i}] = "))) 
 i=i+1 
 i=0 
 print("Saisie du second vecteur : ")
 while i !=n : 
 v2.append(int(input(f"v2[{i}] = "))) 
 i=i+1 
 for i in range(n): 
 scal = scal+(v1[i]*v2[i]) 
 print(f"Le produit scalaire de v1 par v2 vaut {scal}")


def exercice 4 () : 
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
i=0
nbr=0
oldcnbr=0
cnbr=0
snbr=0
for i in range(len(L1)):
    nbr = L1[i]
    for j in range(len(L1)):
        if nbr == L1[j]:
            cnbr +=1
    if oldcnbr < cnbr:
        snbr = nbr
        oldcnbr = cnbr
    cnbr = 0
print(f"Le nombre le plus fréquent dans la liste est le : {snbr}(x{oldcnbr})")


def exercice 4 bis ():
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
i=0
nbr=0
oldcnbr=0
cnbr=0
snbr=0
for i in range(len(L1)):
    nbr = L1[i]
    cnbr = L1.count(L1[i])
    if oldcnbr < cnbr:
        snbr = nbr
        oldcnbr = cnbr
    cnbr = 0
print(f"Le nombre le plus fréquent dans la liste est le : {snbr}(x{oldcnbr})") 


def exercice 5 ():
m=0
n=0
j=0
a=0
n=(input("donnez la date dans le format JJMMAAAA :"))
if len(n)==8 :
   j = int(n[0] + n[1])
   m = int(n[2] + n[3])
   a = int(n[4] + n[5] + n[6]+ n[7])
   if 0<a and a<9999 :
      if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 :
         if 1<= j and j<= 31 :
            print("date correcte")
         else:
            print("date incorrecte")
      elif m == 2:
         if (a%4==0) and (a%100!=0) or (a%400==0) :
            if 1<= j and j<= 29 :
               print("date correct")
            else:
               print("date incorrecte")
         else:
               if 1 <= j and j <= 28:
                  print("date correcte")
               else:
                  print("date incorrecte")
      elif m==4 or m==6 or m==8 or m==9 or m==11:
         if 1 <= j and j <= 30:
            print("date correcte")
         else:
            print("date incorrecte")
      else:
         print("date incorrecte")
   else:
      print("date incorrecte")
else:
   print("date incorrecte")
   
   
   
def exercice 6() :
def 1():
    m = [5, 2, 4, 8, 1, 3]
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
        print(m)

def 2():
    m = [5, 2, 4, 8, 1, 3]
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
    print(sorted(m))
def 3():
    m = [5, 2, 4, 8, 1, 3]
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
        m.sort(reverse=True)
    print(m)


def exercice 7(): 
1)
binome = ("Mathieu", "Mohammed")
print(f"L'étudiant {binome[0]} est en binome avec {binome[1]}")
#####################################
2)
bi=list(binome)
bi[1] = input("Qui est le nouveau binome?:")
binome = tuple(bi)
print(f"L'étudiant {binome[0]} est en binome avec {binome [1]}")
####################################
3)
bi=list(binome)
del bi[1]
binome = tuple(bi)
print(binome)
####################################
4)
binome = ("Mohammed", "Mathieu")
bi = list(binome)
bi.append(input("Entrez le prénom de la troisième personne :"))
binome = tuple(bi)
print(binome)


def exercice 8():
dico= {}
dico['firstname'] = 'Mohammed'
dico['name'] = 'MACOUR'
dico['promo'] = '2022'
dico['group'] = 'RT122'
print("Votre nom est {}, votre prenom est {}, vous faites partie de la promotion {} et votre groupe est {}".format(dico['name'], dico['firstname'], dico['promo'], dico['group']))
#################################
tuplets = {
    "name": dico['name'],
    "firstname": dico['firstname'],
    "promo": dico['promo'],
    "group": dico['group']
}
print("Les clés du dictionnaire sont:")
for key, value in tuplets.items():
    print("-" + key)
print("Les valeurs du dictionnaire sont:")
for key, value in tuplets.items():
    print("-"+ value)
print("Les tuplets du dictionnaire sont:")
for key, value in tuplets.items():
    print("-" + "(" + "'"+ key + "'" + "," + value + ")")
############################################
binome = {}
binome['firstname'] = 'Mathieu'
binome['name'] = 'BIANCHI'
binome['promotion'] = '2022'
binome['group'] = 'RT121'
tuplets2 = {
    "name": binome['name'],
    "firstname": binome['firstname'],
    "promotion": binome['promotion'],
    "group": binome['group']
}
print("Les clés du dictionnaires sont:")
for key, value in tuplets.items():
    print(key)
print("Les valeurs du dictionnaires sont:")
for key, value in tuplets.items():
    print(value)
print("Les tuplets du dictionnaires sont:")
for key, value in tuplets.items():
    print(key + ":" + value)
print("Les étudiants formants le binôme sont:")
print("-L'étudiant {} {} du groupe {}".format(dico['name'], dico['firstname'], dico['group']))
print("-L'étudiant {} {} du groupe {}".format(binome['name'], binome['firstname'], binome['group']))
