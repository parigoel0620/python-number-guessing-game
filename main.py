import random 
n= random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("guess the no :"))
    if(a>n):
       print("lower no please")
       guesses +=1
    elif(a<n):
        print("higher no please")
        guesses+=1

print(f"you have guessed the no {n} coorectly in {guesses} attempts")
