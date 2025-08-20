import time
import random
from os import system as sys; sys('clear') 

user_info = [] #Will contain the informations of the character

print("Crie seu personagem!!!") #"Create your character!" text
time.sleep(3)
sys('clear')
user_info.append(input("Seu nick:")) #Your nickname
sys('clear')

print("Os dados estão decidindo seu HP...") #Randomizing the HP
time.sleep(3)

n1 = random.randint (1,6) #"Dice" one
n2 = random.randint (1,6) #"Dice" two
n3 = (n1 + n2) * 10 #The HP
print (f"Sua vida: {n3}") #"Your Health: "
user_info.append(n3)
time.sleep(2)
sys('clear')

print ("Os dados estão decidindo seu ATK...") #Randomizing the ATK
time.sleep(3)

user_info.append(random.randint(1, 6) * 10) #The ATK
print(f"Seu ATK: {user_info[2]}")  
time.sleep(3)

sys('clear')



print(f"Nick: {user_info[0]} \nHP: {user_info[1]} \nATK: {user_info[2]}")

print("\n Por enquanto é só isso, obrigado por testar! :) ")
