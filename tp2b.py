import os

listeAmin=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listeAmaj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def nbCMin(Pass):
      global listeAmin
      compteur=0
      for c in Pass:
            if c in listeAmin:
                  compteur+=1
      return compteur
def nbCMaj(Pass):
      global listeAmin
      compteur=0
      for c in Pass:
            i=0
            while i< len(listeAmin):
                  if c == listeAmin[i].upper():
                        compteur+=1
                  i=i+1     
      return compteur
def nbCAlpha(Pass):
      global listeAmin
      compteur=0
      for c in Pass:
            if c not in listeAmin and c not in listeAmaj:
                  compteur+=1
      return compteur
def LongMaj(Pass):
      compt=0
      plusLong=str()
      global listeAmin
      liste=[]
      chaine=str()
      for c in Pass:
            if c in listeAmaj:
                  chaine=chaine+c
            else:
                  if chaine!="":
                        liste.insert(compt,chaine)
                        chaine=""
                        compt+=1
      liste.append(chaine)
      plusLong=liste[0]
      for c in liste:
            if len(c)>len(plusLong):
                  plusLong=c
      return len(plusLong),plusLong
def LongMin(Pass):
      compt=0
      plusLong=str()
      global listeAmin
      liste=[]
      chaine=str()
      for c in Pass:
            if c in listeAmin:
                  chaine=chaine+c
            else:
                  if chaine!="":
                        liste.insert(compt,chaine)
                        chaine=""
                        compt+=1
      liste.append(chaine)
      plusLong=liste[0]
      for c in liste:
            if len(c)>len(plusLong):
                  plusLong=c
      return len(plusLong),plusLong
def Score(Pass):
      bonus=len(Pass)*4+(len(Pass)-nbCMaj(Pass))*2+(len(Pass)-nbCMin(Pass))*3+nbCAlpha(Pass)*5
      d,plusLongMin=LongMin(Pass)
      e,plusLongMaj= LongMaj(Pass)
      penalite=d*2+e*3
      score=bonus-penalite
      return (score)
def comparaison(score):
      if score<20:
            return "Tres faible"
      elif score<40:
            return "Faible"
      elif score<80:
            return "Fort"
      else:
            return"Tres Fort"
      
if __name__=="__main__":
      
      Pass=input("Saisir votre mot de passe : \t")
      a=nbCMin(Pass)
      print("nombre de minuscule : ",a)
      b=nbCMaj(Pass)
      print("nombre de majuscule : ",b)
      c=nbCAlpha(Pass)
      print("nombre de caractere non alphabetique :",c)
      d,plusLongMin=LongMin(Pass)
      print("La longueur de la plus longue séquence de lettres miniscules(‘",plusLongMin,"’) =",d)
      e,plusLongMaj= LongMaj(Pass)
      print("La longueur de la plus longue séquence de lettres majiscules(‘",plusLongMaj,"’) =",e)
      penalite=d*2+e*3
      bonus=len(Pass)*4+(len(Pass)-nbCMaj(Pass))*2+(len(Pass)-nbCMin(Pass))*3+nbCAlpha(Pass)*5
      print("Le score final ={0} - {1} =  ".format(bonus, penalite),Score(Pass))
      print("Votre mot de Passe est ",comparaison(Score(Pass)))
      
      os.system("pause")
