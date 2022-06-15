#   Developed & maintaned by @coderpy4
#   Contact info:
#       Email: coderpy4@proton.me
#       Telegram: @coderpy4
#       Twitter: @CoderPY4
#       Instagram: coderpy.4
import sys
import os
import time
import webbrowser

v = "v0.2_rc1"
os.system("title" + f" CalculatorPY_{v}")

answerlist = list(range(1,7))
val = []
answer = []

def splash_screen(seconds):
    os.system('cls')
    print(sys.version)
    print("\n")
    print(" ***********************")
    print(" *                     *")
    print(" *     CalculatorPY    *")
    print(f" *       {v}      *")
    print(" *                     *")
    print(" ***********************")
    time.sleep(seconds)
    os.system('cls')

def clearval():
    val.clear()
    answer.clear()

def valcheck(g):
    s = input(f"Enter {g} number: ")
    if s.isnumeric() == False:
        print("Invalid input. Please try again.")
        time.sleep(1)
        os.system("cls")
        valcheck(g)
    else:
        s = int(s)
        val.append(s)

def anscheck(u):
    print(f"Choose {u} action:")
    print("1. + \n2. - \n3. * \n4. / \n5. None \n6. Exit")
    a = input(f"Enter number of {u} action: ")
    a = int(a)
    if a not in answerlist:
        print("Invalid input. Please try again.")
        time.sleep(1)
        os.system("cls")
        anscheck(u)
    else:
        answer.append(a)



splash_screen(1)

print(sys.version)
print(f'CalculatorPY {v}')
print('Welcome to calculatorPY!')
print(answerlist)

while True:
    valcheck("first")
    valcheck("second")
    valcheck("third")
    anscheck("first")
    anscheck("second")
    print(val)
    if answer[0] == 1 and answer[1] == 1:
        print(f"{val[0]} + {val[1]} + {val[2]} = {val[0] + val[1] + val[2]}")
        clearval()
    elif answer[0] == 1 and answer[1] == 2:
        print(f"{val[0]} + {val[1]} - {val[2]} = {val[0] + val[1] - val[2]}")
        clearval()
    elif answer[0] == 1 and answer[1] == 3:
        print(f"{val[0]} + {val[1]} * {val[2]} = {val[0] + val[1] * val[2]}")
        clearval()
    elif answer[0] == 1 and answer[1] == 4:
        if val[2] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} + {val[1]} / {val[2]} = {val[0] + val[1] / val[2]}")
            clearval()
    elif answer[0] == 2 and answer[1] == 1:
        print(f"{val[0]} - {val[1]} + {val[2]} = {val[0] - val[1] + val[2]}")
        clearval()
    elif answer[0] == 2 and answer[1] == 2:
        print(f"{val[0]} - {val[1]} - {val[2]} = {val[0] - val[1] - val[2]}")
        clearval()
    elif answer[0] == 2 and answer[1] == 3:
        print(f"{val[0]} - {val[1]} * {val[2]} = {val[0] - val[1] * val[2]}")
        clearval()
    elif answer[0] == 2 and answer[1] == 4:
        if val[2] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} - {val[1]} / {val[2]} = {val[0] - val[1] / val[2]}")
            clearval()
    elif answer[0] == 3 and answer[1] == 1:
        print(f"{val[0]} * {val[1]} + {val[2]} = {val[0] * val[1] + val[2]}")
        clearval()
    elif answer[0] == 3 and answer[1] == 2:
        print(f"{val[0]} * {val[1]} - {val[2]} = {val[0] * val[1] - val[2]}")
        clearval()
    elif answer[0] == 3 and answer[1] == 3:
        print(f"{val[0]} * {val[1]} * {val[2]} = {val[0] * val[1] * val[2]}")
        clearval()
    elif answer[0] == 3 and answer[1] == 4:
        if val[2] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} * {val[1]} / {val[2]} = {val[0] * val[1] / val[2]}")
            clearval()
    elif answer[0] == 4 and answer[1] == 1:
        if val[1] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} / {val[1]} + {val[2]} = {val[0] / val[1] + val[2]}")
            clearval()
    elif answer[0] == 4 and answer[1] == 2:
        if val[1] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} / {val[1]} - {val[2]} = {val[0] / val[1] - val[2]}")
            clearval()
    elif answer[0] == 4 and answer[1] == 3:
        if val[1] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} / {val[1]} * {val[2]} = {val[0] / val[1] * val[2]}")
            clearval()
    elif answer[0] == 4 and answer[1] == 4:
        if val[1] == '0' and val[2] == '0' or val[1] == '0' or val[2] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} / {val[1]} / {val[2]} = {val[0] / val[1] / val[2]}")
            clearval()
    elif answer[0] == 5 and answer[1] == 1:
        print(f"{val[1]} + {val[2]} = {val[1] + val[2]}")
        clearval()
    elif answer[0] == 5 and answer[1] == 2:
        print(f"{val[1]} - {val[2]} = {val[1] - val[2]}")
        clearval()
    elif answer[0] == 5 and answer[1] == 3:
        print(f"{val[1]} * {val[2]} = {val[1] * val[2]}")
        clearval()
    elif answer[0] == 5 and answer[1] == 4:
        if val[2] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[1]} / {val[2]} = {val[1] / val[2]}")
            clearval()
    elif answer[0] == 1 and answer[1] == 5:
        print(f"{val[0]} + {val[1]} = {val[0] + val[1]}")
        clearval()
    elif answer[0] == 2 and answer[1] == 5:
        print(f"{val[0]} - {val[1]} = {val[0] - val[1]}")
        clearval()
    elif answer[0] == 3 and answer[1] == 5:
        print(f"{val[0]} * {val[1]} = {val[0] * val[1]}")
        clearval()
    elif answer[0] == 4 and answer[1] == 5:
        if val[1] == '0':
            print('Cannot divide by zero')
        else:
            print(f"{val[0]} / {val[1]} = {val[0] / val[1]}")
            clearval()
    elif answer[0] == 6 or answer[1] == 6:
        sup = input("Do you want to support me? [y/n] ")
        if sup == 'y' or sup == 'yes' or sup == 'Y':
            print('1. Patreon \n2. Buy Me A Coffee')
            cos = input('Choose a service: ')
            if cos == '1':
                webbrowser.open('https://www.patreon.com/coderpy4')
                break
            elif cos == '2':
                webbrowser.open('https://www.buymeacoffee.com/coderpy4')
                break
        elif sup == 'n' or sup == 'N' or sup == 'no':
            print('Thanks for using my app.')
            print('Made with ❤  by CoderPY4')
            time.sleep(2)
            break
