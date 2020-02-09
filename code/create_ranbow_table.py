"""
@author
********NDJEKOUA ANDJO JRNA THIBAUT*********
"""


import params 
import functions

data_base_clair = params.data_base_clair
output_path = params.output_path
P = params.P

try:
   f_in = open(data_base_clair,"r")
   f_out = open(output_path,"w+")

except IOError:
    print ("Could not open either input or ouput file! Please check the correctness of both paths")
    
print("DEBUT DE LA CREATION DE LA BASE DE DONNE A L'HEURE: ",functions.get_time())
for pass_clair in f_in:
    if len(pass_clair) != 0:
     #f_out.write(pass_clair)
     for i in range(P-900):
      my_hash = functions.sha256(pass_clair)
      clair = functions.reduce_hash_to_pass(my_hash,i)
     f_out.write(pass_clair.rstrip("  \n")+" "+my_hash+"\n") 
      
f_in.close()
f_out.close()  
    
print("FIN DE LA CREATION DE LA BASE DE DONNE ",functions.get_time())
