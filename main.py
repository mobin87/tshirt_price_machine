# Description:      This program is used to quote tshirt printing price based on
#                   the amount of colors and quantity of tshirts ordered.
# Input:            Integer
# Output:           Real 0.00
# Sources:          Lab 3 Instructions

# Hello. I print tshirts for a living and quoting my cutomers with price breaks
# for different quantities and colors can get confusing.
# This program takes the amount of colors in the design the customer would like printed,
# and the quantity of shirts they would like, and gives pricing accordingly.


def main():
    colors = 0
    qty = 0
    total = 0.00

    welcomeMessage()
    colors = colorsAmt()
    qty = qtyAmt()
    total = calcTotal(colors, qty)
    colorFinder(colors)
    final(total)

def welcomeMessage():
    print("Hello. This is a program used to quote tshirt printing.")
    print("Tshirt printing is priced based on the amount of colors per design,")
    print("and the amount of tshirts ordered.")
    print("There is a MAX amount of 3 colors per order.")


def colorsAmt():
    colors = 0
    while True:
        try:
            colors = int(input("Please enter the amount of colors in the design you are printing: "))
            break
        except:
            print("Please enter a valid number.")
    while colors > 3:
        print("There is a MAX amount of 3 colors per order.")
        while True:
            try:
                colors = int(input("Please enter the amount of colors in the design you are printing: "))
                break
            except:
                print("Please enter a valid number.")
    return colors

def qtyAmt():
    qty = 0
    qty = int(input("Please enter the amount of tshirts you would like to order: "))
    return qty

def calcTotal(num1, num2):
    total = 0.00
    if num1 == 1 and num2 >= 1 and num2 <= 24:
        total = 6.00
    elif num1 == 1 and num2 >=25 and num2 <= 48:
        total = 5.50
    elif num1 == 1 and num2 >= 49 and num2 <= 72:
        total = 5.00
    elif num1 == 1 and num2 > 72:
        total = 4.50
    elif num1 == 2 and num2 >= 1 and num2 <= 24:
        total = 7.00
    elif num1 == 2 and num2 >= 25 and num2 <= 48:
        total = 6.50
    elif num1 == 2 and num2 >= 49 and num2 <= 72:
        total = 6.00
    elif num1 == 2 and num2 > 72:
        total = 5.50
    elif num1 == 3 and num2 >= 1 and num2 <= 24:
        total = 8.00
    elif num1 == 3 and num2 >= 25 and num2 <= 48:
        total = 7.50
    elif num1 == 3 and num2 >= 49 and num2 <= 72:
        total = 7.00
    elif num1 == 3 and num2 > 72:
        total = 6.50
    return total

def colorFinder(colors):
    if colors == 1:
        print("You have chosen the minimum amount of colors. You must be broke.")
    if colors == 3:
        print("You have chosen the maximum amount of colors. You are a big spender!")

def final(num):
    formatTotal = "{:.2f}".format(num)
    print("The cost of printing each shirt will be: $", formatTotal, sep="")

main()
