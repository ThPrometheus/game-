import random 

rastgelesayı = random.randint(1,100)
tahmin = int(input("Say a number between 1 and 100: "))

while True:
    if rastgelesayı < tahmin:
        print("say a lower number")
        tahmin = int(input("Say a number between 1 and 100: "))
    elif rastgelesayı > tahmin:
        print("say a higher number: ")
        tahmin = int(input("Say a number between 1 and 100: "))
    else:
        print(" !!! congratulations !!!")
        break
        