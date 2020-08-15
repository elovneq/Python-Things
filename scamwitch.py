#!/usr/bin/python3

import random
import os

a="You can do it"
b="Its a really tough one"
c="I'd do it"
d="Don't make me angry"
e="You cannot do it"
f="You are useless for that"
g="If you are not embrassed by that go for it"
e="Not in earth"
j="Piece of cake for you man"
l="Even my grandfather can do it"
q="Good for you little man"
w="Go freaking away"
e="You will learn it slowly..."

print("""*********************************\n
Welcome to scammerwitch\n Enter your question \n Press 2 to clean the screen \n 3 to quit \n
************************* """)
liste=[a,b,c,d,e,f,g,e,j,l,q,w,e]
while 1:

	

	inp=input("Sor veya Çıkmak için q ya bas: ")
	if inp=="3":
		break
	elif inp=="2":
		os.system("clear")
	else:
		num=random.randint(0,12)
		print(liste[num])
	
