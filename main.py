#power by little ai
#github: https://github.com/little-file
#0.1V
import random

def zerototen():
    x = random.randint(0,10)
    print("I kept a number between 0 and 10, guess.")
    while True:
        T = input("Enter: ")
        if T == "exit" or T == "quit" or T == "q" or T == "e":
            break
        z = int(T)
        if z  == x:
            print("True")
            x = random.randint(0,10)
        elif z != x:
            print("Try again.")

def zerotohundred():
    x = random.randint(0,100)
    print("I kept a number between 0 and 100, guess.")
    while True:
        T = input("Enter: ")
        if T == "exit" or T == "quit" or T == "q" or T == "e":
            break
        z = int(T)
        if z  == x:
            print("True")
            x = random.randint(0,100)
        elif z != x:
            print("Try again.")


while True:
    print("""
1) 0 to 10
2) 0 to 100
3) quit
    """)
    choice = input("Enter: ")
    
    if choice == "1" or choice == "0 to 10":
        zerototen()
    elif choice == "2" or choice == "0 to 100":
        zerotohundred()
#    elif choice == "3" or choice == "random":
 #       print("3")
    elif choice == "3" or choice == "quit" or choice == "exit":
        exit()
    else:
        print("try again.")
