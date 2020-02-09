
################################################
## Fait par NDJEKOUA SANDJO JEAN THIBAUT     ##
##                                           ##
################################################


.PHONY :  run


run :
	python3 ./code/main.py $(hash)
	
create_ranbow_talbe :
	python3 ./code/create_ranbow_table.py 
	
test :
	python3 ./code/prova.py  $(hash)
	





	


