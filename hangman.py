import sys
import os
import time
import random
import copy


h1=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





liste0=[]
j=6                             #Tries
o=0
l3=[]

a1=sys.argv[1]
b1=open(a1)
a2=b1.read()
a2=a2.lower()
b2=list(a2.split("\n"))
b2.pop()
a3=random.randint(0,len(b2)-1)  #Random integer picked
b3=b2[a3]                       #Random word picked


for l in range(len(b3)):
	liste0.append("_")





#Funcion to convert string to list 

def convertolist(x):
	liste=[]
	for k in range(len(x)):
		liste.append(x[k])
	return liste

liste1=convertolist(b3)

#The Game Source 
print(liste0)
while j>=0:
	
	
	
	
	inp=input("Guess the word:")
	a=copy.copy(liste0)
	l3.append(inp) #Used words
	for i in range(len(b3)) :
	
		
		if inp==b3[i]:
			liste0[i]=inp
	
	
	if j==0 and liste0!=liste1:
		print("Game Over",h1[6],"\nAnswer is:",b3)
		break
	if a==liste0:
		j-=1
		o+=1
		print(liste0,h1[o],"\n Used words",l3)
		
	elif liste0==liste1:
		print("Congrulations You Win")
		print(liste0)
		break
	else:
		print(liste0,h1[o])	

