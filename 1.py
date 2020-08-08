import random
import os
import time

print("""********************************** \n
Welcome To The  Number Guessing Game \n \n I have a number in my mind in range 1-100 \n Can you guess it with 7 tries?
************************************""")



a=random.randint(1,100)


i=7
while i >= 0:
	
	b=input("Guess the number:")
	if int(b)==a:
		print("Congurulations Number is:", a)
		break
	elif int(b)>a and i!=0:
		i-=1
		print("Wrong Guess! \n Aim Lower! \n You've got",i,"tries left")
		
	elif int(b)<a and i!=0:
		i-=1
		print("Wrong Guess! \n Aim Higher! \n You've got",i,"tries left")
		
		
	elif i==0:
		print("""You do not have tries left\n******************\n GAME OVER \n""")
		break
	else:
		print("Please only enter integer values.")
