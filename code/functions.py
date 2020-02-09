"""
@author
********NDJEKOUA ANDJO JRNA THIBAUT*********
"""

#***************IMPORT******************
from datetime import datetime
import hashlib
import params

#****************VARIABLES******************

alphabet = params.alphabet

#***************FUNCTIONS*******************
    
  
 
"""
function that allow to hash given string using the 256 hash

@input:
-string a string of varibale length containin the string to be hashed

@output
-a hashed string of length 64
"""
def sha256(string):

    return hashlib.sha256(string.encode()).hexdigest()

"""
function that allow to get the current time
"""
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
  

"""
function that allow to extract apssword from a given hash

@input :
-hash : a string of lngth 64 containing the hash
-i : an integer

@returns
-a string conting a newly generated password
"""

def reduce_hash_to_pass(hash,i):
     t = 6 + (ord(hash[0])%5)
     password = ""
     for j in range(t):
      index = ((ord(hash[j])+i)%255)%62
      c = alphabet[index]
      password += c
     return password

"""
function that allow to compare 2 strings
"""
def compare(s1,s2):
 return s1==s2

"""
function that checks wether a given hash, is present in the data_base or not

@input:
-my_string : a string of length 64 containing the searched hash
-my_file : the path to the file containg the data base to search in

@retunrs:
-a flag which indicate wehter the element was present or not
-the original password the hash was derived from
"""
def check(my_hash,my_file): # this funcion should return 2 results.
    f = open(my_file, "r")
    returned_value = ""
    flag = False
    for line in f:
     words = line.split(" ")

     if compare(words[1][:len(words[1])-1],my_hash) :
      returned_value = words[0]
      flag = True 
    f.close() 
    return flag,returned_value


