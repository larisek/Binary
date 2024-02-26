print("Převodník do binárního kódu.(Pouze pro malá písmena.)")
print("Vytvořil larisek")
input()
for i in range(1, 101):
    print()
x = ""
while True:
    let = input("Napiš písmeno: ").lower()
    if let == str("a"):
        x = x + " " + "01100001"
    elif let == str("b"):
        x = x + " " + "01100010"
    elif let == str("c"):
        x = x + " " + "01100011"
    elif let == str("d"):
        x = x + " " + "01100100"
    elif let == str("e"):
        x = x + " " + "01100101"
    elif let == str("f"):
        x = x + " " + "01100110"
    elif let == str("g"):
        x = x + " " + "01100111"
    elif let == str("h"):
        x = x + " " + "01101000"
    elif let == str("i"):
        x = x + " " + "01101001"
    elif let == str("j"):
        x = x + " " + "01101010"
    elif let == str("k"):
        x = x + " " + "01101011"
    elif let == str("l"):
        x = x + " " + "01101100"
    elif let == str("m"):
        x = x + " " + "01101101"
    elif let == str("n"):
        x = x + " " + "01101110"
    elif let == str("o"):
        x = x + " " + "01101111"
    elif let == str("p"):
        x = x + " " + "01110000"
    elif let == str("q"):
        x = x + " " + "01110001"
    elif let == str("r"):
        x = x + " " + "01110010"
    elif let == str("s"):
        x = x + " " + "01110011"
    elif let == str("t"):
        x = x + " " + "01110100"
    elif let == str("u"):
        x = x + " " + "01110101"
    elif let == str("v"):
        x = x + " " + "01110110"
    elif let == str("w"):
        x = x + " " + "01110111"
    elif let == str("x"):
        x = x + " " + "01111000"
    elif let == str("y"):
        x = x + " " + "01111001"
    elif let == str("z"):
        x = x + " " + "01111010"
    elif let == 0:
        break
    else:
        print("špatně zadané číslo")
        input()
    for i in range(1,101):
        print()
    print(x)