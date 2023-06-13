def exercice  1 ():
str1 = input("Entrez le nom de la 1e personne : ")
str2 = input("Entrez le prénom de la 1e personne : ")
str3 = input("Entrez le nom de la 2e personne : ")
str4 = input("Entrez le prénom de la 2e personne : ")
if str1 != str3 :
    if str1 < str3 :
        print("Cas 1")
        print(str1.upper(), str2.capitalize())
        print(str3.upper(), str4.capitalize())
    elif str3 < str1 :
        print("Cas 2")
        print(str3.upper(), str4.capitalize())
        print(str1.upper(), str2.capitalize())
if str1 == str3 :
    if str2 < str4 :
        print("Cas 3")
        print(str1.upper(), str2.capitalize())
        print(str3.upper(), str4.capitalize())
    elif str4 < str2 :
        print("Cas 4")
        print(str3.upper(), str4.capitalize())
        print(str1.upper(), str2.capitalize())
        
          
def exercice 2 ():      
n =0
no =0
coeff =0
Somme = 0
Somme_coeff = 0
for i in range(5):
    n = input(f"Veuillez entrer la note du module {i} et le coefficient\ncorrespondant:")
    Recherche = n.split(" ")
    no = float(Recherche[0])
    coeff = float(Recherche[1])
    Somme = Somme + (no * coeff)
    Somme_coeff = Somme_coeff + coeff
    moy = Somme / Somme_coeff
    if float(Recherche[0])< 8:
        print("L'étudiant n'est pas admis !")
        break
    if i == 4 :
        if moy>10 :
            print("L'étudiant est  admis")
    else:
        print("L'étudiant n'est pas admis")
print(moy)

def exercice 3():
pal = str(input("Entrez un mot ou une phrase :"))
pal = ''.join(filter(str.isalnum, pal))
pal = str.lower(pal)
print(pal)

if str(pal) == str(pal[::-1]) :
    print("C'est un palimdrome !")
else :
    print("Ce  n'est pas un palimdrome !")
    

def exercice 4():
    somme = int(input("Somme a decomposer? "))
    b100 = somme // 100
    r100 = somme % 100
    print("==> {:4d} billet(s) de 100 euros, reste {:d}".format(b100, r100))
    b50 = r100 // 50
    r50 = r100 % 50
    print("==> {:4d} billet(s) de 50 euros, reste {:d}".format(b50, r50))
    b10 = r50 // 10
    r10 = r50 % 10
    print("==> {:4d} billet(s) de 10 euros, reste {:d}".format(b10, r10))
    p2 = r10 // 2
    r2 = r10 % 2
    print("==> {:4d} pieces(s) de 2 euros, reste {:d}".format(p2, r2))
    p1 = r2
    print("==> {:4d} pieces(s) de 1 euro".format(p1))

def exercice 5 ():
heure = None
argent_h = None
heure = int(input("heure ? "))
argent_h = int(input("argent par heure :"))
if heure <= 160 :
    salaire = heure * argent_h
elif heure >= 161 and heure <= 200 :
    surplus = (heure -160) * (argent_h*1.25)
    salaire = (160 * argent_h + surplus)
elif heure >= 201 :
    surplus_2 = (heure - 200) * (argent_h * 1.50)
    surplus = 39 * argent_h * 1.25
    salaire = (160 * argent_h ) +  surplus + surplus_2
print(salaire)
