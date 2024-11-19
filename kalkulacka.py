# Calculejtor v Pajthone

import math

print ("Operacie: +, -, *, /, ^, √")

# Scitanie cisel
def addition(num1, num2):
    return num1 + num2

# Odcitanie cisel
def subtraction(num1, num2):
    return num1 - num2

# Nasobenie cisel
def multiplication(num1, num2):
    return num1 * num2

# Delenie cisel
def divison(num1, num2):
    return num1 / num2

# Mocniny
def power(num1, num2):
    return num1 ** num2

# Odmocniny
def nth_root(num, n):
    return num ** (1 / n)

print("Zvol operaciu -/n" \
      "1. Addition/n" \
      "2. Subtraction/n" \
      "3. Multiplication/n" \
      "4. Division/n" \
      "5. Power/n" \
      "6. Nth_Root/n")

# Input od pouzivatela
select = int(input("Vyber operaciu z 1, 2, 3, 4, 5, 6 : "))

if select in [1, 2, 3, 4, 5]:
    number_1 = int(input("Vyber prve cislo: "))
    number_2 = int(input("Vyber druhe cislo: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          addition(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtraction(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
          multiplication(number_1, number_2))
    
elif select == 4:
    print(number_1, "/", number_2, "=",
          divison(number_1, number_2))
    
elif select == 5:
    print(number_1, "**", number_2, "=",
          power(number_1, number_2))
    
elif select == 6:
    number_1 = float(input("Vyber cislo ktore odmocnis: "))
    n = int(input("Vyber hodnotu odmocniny: "))
    if n <= 0:
        print("Musi byt kladne cislo!")
    else:
        print(f"{n} odmocnina z {number_1} je {nth_root(number_1, n)}")
    
else:
    print("Invalid input")