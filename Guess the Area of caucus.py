from turtle import *
import random
import time
#list of asian nations and some other stuff
asia = ["JohnWetton","Tibet"," Siberia"]

#first def class
def wormwaiting():
    rice=random.choice(asia)
#COLOURING
    bgcolor('#6f1b72')
    pencolor('#85b25b')
#Atual Start
    penup()
    goto(-250,0)
    write(rice, font=("Comic Sans",100))
    time.sleep(.5) #look below
    reset()
    penup()
    goto(-250, 0)
    write("ASIA TIME LETS DO THIS FRIEND", font=("Times New Roman",45))
    goto(-250,-45)
    write("check out the thingy", font=("Times New Roman",45))
    time.sleep(4) #dramatic pauses are for the weak
    reset()
    suicide()

def suicide():
    quitter=input("Don't be a quitter. Choose Y you coward (Y/N)")
    if quitter.lower()=="y":
        whydoeslaosexist()
    elif quitter.lower()=="n":
        print ("You moist golfball")
    else:
        print("The human earlobe (lobulus auriculae) is composed of tough areolar and adipose connective tissues, lacking the firmness and elasticity of the rest of the auricle (the external structure of the ear). In some cases the lower lobe is connected to the side of the face. Since the earlobe does not contain cartilage[1] it has a large blood supply and may help to warm the ears and maintain balance. The zoologist Desmond Morris in his book The Naked Ape (1967) conjectured that the lobes developed as an additional erogenous zone to facilitate the extended sexuality necessary in the evolution of human monogamous pair bonding.[2] However, earlobes are not generally considered to have any major biological function.[3] The earlobe contains many nerve endings, and for some people is an erogenous zone.")
        suicide()
def whydoeslaosexist():
    pencolor('#438c82')
    penup()
    goto(-250,0)
    write("lets start this")
    wormwaiting()
    
    
whydoeslaosexist()
