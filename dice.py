#!/usr/bin/python3
import random
import os
import time

print("""***********************************\nROLE THE DICE\n***********************************""")
print("""

    _______            
  /\       \           
 /()\   ()  \          
/    \_______\         
\    /()     /         
 \()/   ()  /          
  \/_____()/

""")




def dice():

	
	print("Rolling the dice...\n")
	dice1=random.randint(1,6)	
	time.sleep(1)
	print("Number is:",dice1)

while 1:
	command1=input("""***********************************\n\n1-)Roll the Dice\n2-)Quit\n3-)Clear the screen\n\n***********************************:""")
	if command1=="1":
		dice()
	elif command1=="2":
		print("Quiting...Bye")
		break	
	elif command1=="3":
		os.system("clear")

