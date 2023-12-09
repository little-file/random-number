#power by little ai
#github: https://github.com/little-file
#0.1V
import random

def zerototen():
    def human():
                while True:
                    x = random.randint(0,10)
                    print(x)
                    T = input("True(t) or False(f) Enter:")
                    if T == "True" or T == "true" or T == "t" or T == "T":
                        print("nice")
                        continue
                    elif T == "quit" or T == "q" or T == "exit" or T == "e":
                        exit()
                    elif T == "False" or T == "false" or T == "f" or T == "F":
                        while True:
                            g = input("can i try again ?(y/n): ")
                            if g == "y":
                                break
                            elif g == "n":
                                exit()
    def robot():
                x = random.randint(0,10)
                print("I kept a number between 0 and 10, guess.")
                while True:
                    T = input("Enter: ")
                    if T == "exit" or T == "quit" or T == "q" or T == "e":
                        exit()
                    z = int(T)
                    if z  == x:
                        print("True")
                        x = random.randint(0,10)
                    elif z != x:
                        print("Try again.")
    while True:
        print("""
Will you guess or will I?(i/u)
        """)
        choice = input("Enter:")
        if choice == "i":
            human()
        elif choice == "you" or choice == "u":
            robot()     
                 

def zerotohundred():
    def human():
                while True:
                    x = random.randint(0,100)
                    print(x)
                    T = input("True(t) or False(f) Enter:")
                    if T == "True" or T == "true" or T == "t" or T == "T":
                        print("nice")
                        continue
                    elif T == "quit" or T == "q" or T == "exit" or T == "e":
                        exit()
                    elif T == "False" or T == "false" or T == "f" or T == "F":
                        while True:
                            g = input("can i try again ?(y/n): ")
                            if g == "y":
                                break
                            elif g == "n":
                                exit()
    def robot():
                x = random.randint(0,100)
                print("I kept a number between 0 and 10, guess.")
                while True:
                    T = input("Enter: ")
                    if T == "exit" or T == "quit" or T == "q" or T == "e":
                        exit()
                    z = int(T)
                    if z  == x:
                        print("True")
                        x = random.randint(0,10)
                    elif z != x:
                        print("Try again.")
    while True:
        print("""
Will you guess or will I?(i/u)
        """)
        choice = input("Enter:")
        if choice == "i":
            human()
        elif choice == "you" or choice == "u":
            robot()    

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
