
@author
***************************  NDJEKOUA SANDJO JEAN THIBAUT ***************************************************


Une Rainbow Table est deja créée avec un nombre de P=1000 fonctions de réduction. Son utilisation est donc instantanée. Cependant l'application permet de crée une Rainbow Table personnalisée à partir d'une base de donnée de mot de passe à l'aide de ./create_rainbowTable.

La Rainbow Table se trouve dans le dossier data_base sous le nom de mot_passe_hash.txt. Github n’acceptant pas les fichiers de plus de 1 MB, une version dégradée y a été uploader.
La version de 1Gb de la rainbow table se trouve à l’adresse suivante :
https://drive.google.com/drive/folders/10AOqjRBmBlhTJ6vNcAETgfeUX-TlDzZC


****************************  CASSER UN MOT DE PASSE EN UTILISANT LA RANBOW TABLE EXISTANTE********************

1) --> placer vous dans le dossier projet_SR2i203, ouvrir un terminal, et lancer l'application à l'aide du make file avec la commande :

2) --> make hash="you hash" 

où hash correspond à l'empreintes ha 256 de 64 caractères, que nous voulons craquer.
Consultez ensuite le résultat de l'ouput pour vérifier le satatus de la recherche.



******************************  CREE SA PROPRE RANBOW TABLE *****************************************************

1) --> vous devez disposer d'un fichier contenant des mots de pass en claire au format .txt.

2) --> Positionnez le fichier dans le dossier data_base

3) --> Renommer le fichier en "mot_pass_clair" et assurez vous qu'il soit de type ".txt"

4) --> Placez-vous dans le dossier projet_SR2i203, ouvrir un terminal, et lancer l'application grace a la commande : make create_ranbow_table

Après avoir reçu le message FIN DE LA CREATION. vous pourrez directement casser votre mot de pass en utilisant la procedure indiquer plus haut

