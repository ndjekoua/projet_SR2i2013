"""
@author
********NDJEKOUA ANDJO JRNA THIBAUT*********
"""

import functions
import params
import sys

def main():
    
    if len(sys.argv) != 2:
     print("\n **************USAGE ERROR************\n please have a carefull look at the usage of the program. \n")
     print("the usage of {} using the make file is : make hash='your hash' run. TIPS: do not put any sapce between the equal and your hash string\n".format(sys.argv[0]))
     exit(-1)
    print("***************DEBUT DE LA RECHERCHE DANS LA RAINBOW TABLE**************** \n\n"," \t HEURE DE DEBUT :",functions.get_time())
    
  #******import the parameters*******
    my_hash = str(sys.argv[1])
    data_base = params.data_base
    P = params.P 
    i = P-1
    
    print("Searching the password corresponding to the hash : \n",my_hash,"\n")
  #*******start the search in the ranbow table***********
    flag,returned_password = functions.check(my_hash,data_base)
  
  
    while i >=0 and flag == False:
     j = i
     while j <= P:
        nom = functions.reduce_hash_to_pass(my_hash,j)
        my_hash = functions.sha256(nom)
        j+=1
     flag,returned_password = functions.check(my_hash,data_base)
     i-=1
   
  #*******cherk the result of the search***********
    if flag == True:
     print("Le mot de passe provient de : ",returned_password," de la rainbow table, on applique : ", P-i+1," transformations de hachage et reduction")
     for j in range(i+1):
      my_hash = functions.sha256(returned_password) 
      returned_password =  functions.reduce_hash_to_pass(my_hash,j)
   
     print("le mot de passe en clair est : " ,returned_password)
   
    if flag == False:
      print("le mot de passe n existe pas dans notre base de donnée " )
 
    print("\tHEURE DE FIN  ",functions.get_time(),"\n")

    print("***************FIN DE LA RECHERCHE.***************") 

    print("\nMERCI D AVOIR UTILISE NOTRE APP !!!")

main()

