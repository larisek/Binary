print("Převodník do binárního kódu.")
print("Vytvořil larisek")
print("Jakoukoli chybu hlašte na discord: larisek")
input()
while True:
    print("1.Mapa povolených znaků")
    print("2.Převaděč znaků do BC")
    print("3.Konec")
    choos = int(input("Výběr: "))
    for i in range(1, 101):
        print()
    if choos == 1:
        m = '"'
        print("Malá písmena: abcdefghijklmnopqrstuvwxyz")
        print("Velká písmena: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print("čísla: 0123456789")
        print(f"Znaky: !{m}#%&'()+,-./@_*")
        input()
        for i in range(1, 101):
            print()
    elif choos == 2:
        input("Pokud budete chtít převaděč ukončit napište exit místo znaku.")
        x = ""
        while True:
            let = input("Napište znak: ")
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
            elif let == str("A"):
                x = x + " " + "01000001"
            elif let == str("B"):
                x = x + " " + "01000010"
            elif let == str("C"):
                x = x + " " + "01000011"
            elif let == str("D"):
                x = x + " " + "01000100"
            elif let == str("E"):
                x = x + " " + "01000101"
            elif let == str("F"):
                x = x + " " + "01000110"
            elif let == str("G"):
                x = x + " " + "01000111"
            elif let == str("H"):
                x = x + " " + "01001000"
            elif let == str("I"):
                x = x + " " + "01001001"
            elif let == str("J"):
                x = x + " " + "01001010"
            elif let == str("K"):
                x = x + " " + "01001011"
            elif let == str("L"):
                x = x + " " + "01001100"
            elif let == str("M"):
                x = x + " " + "01001101"
            elif let == str("N"):
                x = x + " " + "01001110"
            elif let == str("O"):
                x = x + " " + "01001111"
            elif let == str("P"):
                x = x + " " + "01010000"
            elif let == str("Q"):
                x = x + " " + "01010001"
            elif let == str("R"):
                x = x + " " + "01010010"
            elif let == str("S"):
                x = x + " " + "01010011"
            elif let == str("T"):
                x = x + " " + "01010100"
            elif let == str("U"):
                x = x + " " + "01010101"
            elif let == str("V"):
                x = x + " " + "01010110"
            elif let == str("W"):
                x = x + " " + "01010111"
            elif let == str("X"):
                x = x + " " + "01011000"
            elif let == str("Y"):
                x = x + " " + "01011001"
            elif let == str("Z"):
                x = x + " " + "01011010"
            elif let == str("!"):
                x = x + " " + "00100001"
            elif let == str('"'):
                x = x + " " + "00100010"
            elif let == str("#"):
                x = x + " " + "00100011"
            elif let == str("%"):
                x = x + " " + "00100101"
            elif let == str("&"):
                x = x + " " + "00100110"
            elif let == str("'"):
                x = x + " " + "00100111"
            elif let == str("("):
                x = x + " " + "00101000"
            elif let == str(")"):
                x = x + " " + "00101001"
            elif let == str("*"):
                x = x + " " + "00101010"
            elif let == str("+"):
                x = x + " " + "00101011"
            elif let == str(","):
                x = x + " " + "00101100"
            elif let == str("-"):
                x = x + " " + "00101101"
            elif let == str("."):
                x = x + " " + "00101110"
            elif let == str("/"):
                x = x + " " + "00101111"
            elif let == str("0"):
                x = x + " " + "00110000"
            elif let == str("1"):
                x = x + " " + "00110001"
            elif let == str("2"):
                x = x + " " + "00110010"
            elif let == str("3"):
                x = x + " " + "00110011"
            elif let == str("4"):
                x = x + " " + "00110100"
            elif let == str("5"):
                x = x + " " + "00110101"
            elif let == str("6"):
                x = x + " " + "00110110"
            elif let == str("7"):
                x = x + " " + "00110111"
            elif let == str("8"):
                x = x + " " + "00111000"
            elif let == str("9"):
                x = x + " " + "00111001"
            elif let == str("?"):
                x = x + " " + "00111111"
            elif let == str("@"):
                x = x + " " + "01000000"
            elif let == str("_"):
                x = x + " " + "01011111"
            elif let == str("exit"):
                break
            elif let == str("Exit"):
                break
            elif let == str("EXIT"):
                break
            else:
                print("Špatně zadané číslo.")
                print("Zkuste to znovu.")
                input()
            for i in range(1,101):
                print()
            print(x)
    elif choos == 3:
        for i in range(1,101):
            print()
        print("program ukončen.")
        break
    elif choos == 22:
        input("Pokud budete chtít převaděč ukončit napište exit místo BC.")
        x = ""
        while True:
            let = input("Napište BC: ")
            if let == str("01100001"):
                x = x + " " + "a"
            elif let == str("01100010"):
                x = x + " " + "b"
            elif let == str("01100011"):
                x = x + " " + "c"
            elif let == str("01100100"):
                x = x + " " + "d"
            elif let == str("01100101"):
                x = x + " " + "e"
            elif let == str("01100110"):
                x = x + " " + "f"
            elif let == str("01100111"):
                x = x + " " + "g"
            elif let == str("01101000"):
                x = x + " " + "h"
            elif let == str("01101001"):
                x = x + " " + "i"
            elif let == str("01101010"):
                x = x + " " + "j"
            elif let == str("01101011"):
                x = x + " " + "k"
            elif let == str("01101100"):
                x = x + " " + "l"
            elif let == str("01101101"):
                x = x + " " + "m"
            elif let == str("01101110"):
                x = x + " " + "n"
            elif let == str("01101111"):
                x = x + " " + "o"
            elif let == str("01110000"):
                x = x + " " + "p"
            elif let == str("01110001"):
                x = x + " " + "q"
            elif let == str("01110010"):
                x = x + " " + "r"
            elif let == str("01110011"):
                x = x + " " + "s"
            elif let == str("01110100"):
                x = x + " " + "t"
            elif let == str("01110101"):
                x = x + " " + "u"
            elif let == str("01110110"):
                x = x + " " + "v"
            elif let == str("01110111"):
                x = x + " " + "w"
            elif let == str("01111000"):
                x = x + " " + "x"
            elif let == str("01111001"):
                x = x + " " + "y"
            elif let == str("01111010"):
                x = x + " " + "z"
            elif let == str("01000001"):
                x = x + " " + "A"
            elif let == str("01000010"):
                x = x + " " + "B"
            elif let == str("01000011"):
                x = x + " " + "C"
            elif let == str("01000100"):
                x = x + " " + "D"
            elif let == str("01000101"):
                x = x + " " + "E"
            elif let == str("01000110"):
                x = x + " " + "F"
            elif let == str("01000111"):
                x = x + " " + "G"
            elif let == str("01001000"):
                x = x + " " + "H"
            elif let == str("01001001"):
                x = x + " " + "I"
            elif let == str("01001010"):
                x = x + " " + "J"
            elif let == str("01001011"):
                x = x + " " + "K"
            elif let == str("01001100"):
                x = x + " " + "L"
            elif let == str("01001101"):
                x = x + " " + "M"
            elif let == str("01001110"):
                x = x + " " + "N"
            elif let == str("01001111"):
                x = x + " " + "O"
            elif let == str("01010000"):
                x = x + " " + "P"
            elif let == str("01010001"):
                x = x + " " + "Q"
            elif let == str("01010010"):
                x = x + " " + "R"
            elif let == str("01010011"):
                x = x + " " + "S"
            elif let == str("01010100"):
                x = x + " " + "T"
            elif let == str("01010101"):
                x = x + " " + "U"
            elif let == str("01010110"):
                x = x + " " + "V"
            elif let == str("01010111"):
                x = x + " " + "W"
            elif let == str("01011000"):
                x = x + " " + "X"
            elif let == str("01011001"):
                x = x + " " + "Y"
            elif let == str("01011010"):
                x = x + " " + "Z"
            elif let == str("00100001"):
                x = x + " " + "!"
            elif let == str('00100010'):
                x = x + " " + '"'
            elif let == str("00100011"):
                x = x + " " + "#"
            elif let == str("00100101"):
                x = x + " " + "%"
            elif let == str("00100110"):
                x = x + " " + "&"
            elif let == str("00100111"):
                x = x + " " + "'"
            elif let == str("00101000"):
                x = x + " " + "("
            elif let == str("00101001"):
                x = x + " " + ")"
            elif let == str("00101010"):
                x = x + " " + "*"
            elif let == str("00101011"):
                x = x + " " + "+"
            elif let == str("00101100"):
                x = x + " " + ","
            elif let == str("00101101"):
                x = x + " " + "-"
            elif let == str("00101110"):
                x = x + " " + "."
            elif let == str("00101111"):
                x = x + " " + "/"
            elif let == str("00110000"):
                x = x + " " + "0"
            elif let == str("00110001"):
                x = x + " " + "1"
            elif let == str("00110010"):
                x = x + " " + "2"
            elif let == str("00110011"):
                x = x + " " + "3"
            elif let == str("00110100"):
                x = x + " " + "4"
            elif let == str("00110101"):
                x = x + " " + "5"
            elif let == str("00110110"):
                x = x + " " + "6"
            elif let == str("00110111"):
                x = x + " " + "7"
            elif let == str("00111000"):
                x = x + " " + "8"
            elif let == str("00111001"):
                x = x + " " + "9"
            elif let == str("00111111"):
                x = x + " " + "?"
            elif let == str("01000000"):
                x = x + " " + "@"
            elif let == str("01011111"):
                x = x + " " + "_"
            elif let == str("exit"):
                break
            elif let == str("Exit"):
                break
            elif let == str("EXIT"):
                break
            else:
                print("Špatně zadané číslo.")
                print("Zkuste to znovu.")
                input()
            for i in range(1,101):
                print()
            print(x)

# import os
# os.system("cls")
# print("Převodník do binárního kódu.\nVytvořil larisek\nJakoukoli chybu hlašte na discord: larisek")
# input()
# while True:
#     print("1.Mapa povolených znaků\n2.Převaděč znaků do BC\n3.Konec")
#     while True:
#         choos = input("Výběr: ")
#         if choos.isdigit():
#             choos = int(choos)
#             if choos == 1 or choos == 2 or choos == 3:
#                 break
#             else:
#                 print("Vyberte pouze možnost z nabídky.")
#         elif not choos:
#             print("Zadejte něco.")
#         else:
#             print("Zadejte celé číslo.")
#     os.system("cls")
#     m = '"'
#     if choos == 1: # info
#         print(f"Malá písmena: abcdefghijklmnopqrstuvwxyz\nVelká písmena: ABCDEFGHIJKLMNOPQRSTUVWXYZ\nčísla: 0123456789\nZnaky: !{m}#%&'()+,-./@_*")
#         input()
#         os.system("cls")
#     elif choos == 2: # převaděč do BC
#         print("2.Převaděč znaků do BC")
#         input("Pokud budete chtít převaděč ukončit napište 'exit' místo znaku | Pokud budete chtít znovu zobrazit možnosti napište 'info' .")
#         x = ""
#         while True:
#             let = input("Napište znak: ")
#             if let == str("a"):
#                 # x = x + " " + "01100001"
#                 x += " 01100001"
#             elif let == str("b"):
#                 x += " 01100010"
#             elif let == str("c"):
#                 x += " 01100011"
#             elif let == str("d"):
#                 x += " 01100100"
#             elif let == str("e"):
#                 x += " 01100101"
#             elif let == str("f"):
#                 x += " 01100110"
#             elif let == str("g"):
#                 x += " 01100111"
#             elif let == str("h"):
#                 x += " 01101000"
#             elif let == str("i"):
#                 x += " 01101001"
#             elif let == str("j"):
#                 x += " 01101010"
#             elif let == str("k"):
#                 x += " 01101011"
#             elif let == str("l"):
#                 x += " 01101100"
#             elif let == str("m"):
#                 x += " 01101101"
#             elif let == str("n"):
#                 x += " 01101110"
#             elif let == str("o"):
#                 x += " 01101111"
#             elif let == str("p"):
#                 x += " 01110000"
#             elif let == str("q"):
#                 x += " 01110001"
#             elif let == str("r"):
#                 x += " 01110010"
#             elif let == str("s"):
#                 x += " 01110011"
#             elif let == str("t"):
#                 x += " 01110100"
#             elif let == str("u"):
#                 x += " 01110101"
#             elif let == str("v"):
#                 x += " 01110110"
#             elif let == str("w"):
#                 x += " 01110111"
#             elif let == str("x"):
#                 x += " 01111000"
#             elif let == str("y"):
#                 x += " 01111001"
#             elif let == str("z"):
#                 x += " 01111010"
#             elif let == str("A"):
#                 x += " 01000001"
#             elif let == str("B"):
#                 x += " 01000010"
#             elif let == str("C"):
#                 x += " 01000011"
#             elif let == str("D"):
#                 x += " 01000100"
#             elif let == str("E"):
#                 x += " 01000101"
#             elif let == str("F"):
#                 x += " 01000110"
#             elif let == str("G"):
#                 x += " 01000111"
#             elif let == str("H"):
#                 x += " 01001000"
#             elif let == str("I"):
#                 x += " 01001001"
#             elif let == str("J"):
#                 x += " 01001010"
#             elif let == str("K"):
#                 x += " 01001011"
#             elif let == str("L"):
#                 x += " 01001100"
#             elif let == str("M"):
#                 x += " 01001101"
#             elif let == str("N"):
#                 x += " 01001110"
#             elif let == str("O"):
#                 x += " 01001111"
#             elif let == str("P"):
#                 x += " 01010000"
#             elif let == str("Q"):
#                 x += " 01010001"
#             elif let == str("R"):
#                 x += " 01010010"
#             elif let == str("S"):
#                 x += " 01010011"
#             elif let == str("T"):
#                 x += " 01010100"
#             elif let == str("U"):
#                 x += " 01010101"
#             elif let == str("V"):
#                 x += " 01010110"
#             elif let == str("W"):
#                 x += " 01010111"
#             elif let == str("X"):
#                 x += " 01011000"
#             elif let == str("Y"):
#                 x += " 01011001"
#             elif let == str("Z"):
#                 x += " 01011010"
#             elif let == str("!"):
#                 x += " 00100001"
#             elif let == str('"'):
#                 x += " 00100010"
#             elif let == str("#"):
#                 x += " 00100011"
#             elif let == str("%"):
#                 x += " 00100101"
#             elif let == str("&"):
#                 x += " 00100110"
#             elif let == str("'"):
#                 x += " 00100111"
#             elif let == str("("):
#                 x += " 00101000"
#             elif let == str(")"):
#                 x += " 00101001"
#             elif let == str("*"):
#                 x += " 00101010"
#             elif let == str("+"):
#                 x += " 00101011"
#             elif let == str(","):
#                 x += " 00101100"
#             elif let == str("-"):
#                 x += " 00101101"
#             elif let == str("."):
#                 x += " 00101110"
#             elif let == str("/"):
#                 x += " 00101111"
#             elif let == str("0"):
#                 x += " 00110000"
#             elif let == str("1"):
#                 x += " 00110001"
#             elif let == str("2"):
#                 x += " 00110010"
#             elif let == str("3"):
#                 x += " 00110011"
#             elif let == str("4"):
#                 x += " 00110100"
#             elif let == str("5"):
#                 x += " 00110101"
#             elif let == str("6"):
#                 x += " 00110110"
#             elif let == str("7"):
#                 x += " 00110111"
#             elif let == str("8"):
#                 x += " 00111000"
#             elif let == str("9"):
#                 x += " 00111001"
#             elif let == str("?"):
#                 x += " 00111111"
#             elif let == str("@"):
#                 x += " 01000000"
#             elif let == str("_"):
#                 x += " 01011111"
#             elif let == str("exit").lower():
#                 break
#             elif let == str("info").lower():
#                 print(f"Malá písmena: abcdefghijklmnopqrstuvwxyz\nVelká písmena: ABCDEFGHIJKLMNOPQRSTUVWXYZ\nčísla: 0123456789\nZnaky: !{m}#%&'()+,-./@_*")
#                 input()
#             else:
#                 print("Zadaný znak není v nabídce, zkuste to znovu.")
#                 input()
#             os.system("cls")
#             print(x)
#     elif choos == 3: # konec programu
#         os.system("cls")
#         print("Program ukončen.")
#         break
#     elif choos == 22: # převaděč BC
#         os.system("cls")
#         input("Pokud budete chtít převaděč ukončit napište 'exit' místo znaku | Pokud budete chtít znovu zobrazit možnosti napište 'info' .")
#         x = ""
#         while True:
#             let = input("Napište BC: ")
#             if let == str("01100001"):
#                 x = x + " " + "a"
#             elif let == str("01100010"):
#                 x = x + " " + "b"
#             elif let == str("01100011"):
#                 x = x + " " + "c"
#             elif let == str("01100100"):
#                 x = x + " " + "d"
#             elif let == str("01100101"):
#                 x = x + " " + "e"
#             elif let == str("01100110"):
#                 x = x + " " + "f"
#             elif let == str("01100111"):
#                 x = x + " " + "g"
#             elif let == str("01101000"):
#                 x = x + " " + "h"
#             elif let == str("01101001"):
#                 x = x + " " + "i"
#             elif let == str("01101010"):
#                 x = x + " " + "j"
#             elif let == str("01101011"):
#                 x = x + " " + "k"
#             elif let == str("01101100"):
#                 x = x + " " + "l"
#             elif let == str("01101101"):
#                 x = x + " " + "m"
#             elif let == str("01101110"):
#                 x = x + " " + "n"
#             elif let == str("01101111"):
#                 x = x + " " + "o"
#             elif let == str("01110000"):
#                 x = x + " " + "p"
#             elif let == str("01110001"):
#                 x = x + " " + "q"
#             elif let == str("01110010"):
#                 x = x + " " + "r"
#             elif let == str("01110011"):
#                 x = x + " " + "s"
#             elif let == str("01110100"):
#                 x = x + " " + "t"
#             elif let == str("01110101"):
#                 x = x + " " + "u"
#             elif let == str("01110110"):
#                 x = x + " " + "v"
#             elif let == str("01110111"):
#                 x = x + " " + "w"
#             elif let == str("01111000"):
#                 x = x + " " + "x"
#             elif let == str("01111001"):
#                 x = x + " " + "y"
#             elif let == str("01111010"):
#                 x = x + " " + "z"
#             elif let == str("01000001"):
#                 x = x + " " + "A"
#             elif let == str("01000010"):
#                 x = x + " " + "B"
#             elif let == str("01000011"):
#                 x = x + " " + "C"
#             elif let == str("01000100"):
#                 x = x + " " + "D"
#             elif let == str("01000101"):
#                 x = x + " " + "E"
#             elif let == str("01000110"):
#                 x = x + " " + "F"
#             elif let == str("01000111"):
#                 x = x + " " + "G"
#             elif let == str("01001000"):
#                 x = x + " " + "H"
#             elif let == str("01001001"):
#                 x = x + " " + "I"
#             elif let == str("01001010"):
#                 x = x + " " + "J"
#             elif let == str("01001011"):
#                 x = x + " " + "K"
#             elif let == str("01001100"):
#                 x = x + " " + "L"
#             elif let == str("01001101"):
#                 x = x + " " + "M"
#             elif let == str("01001110"):
#                 x = x + " " + "N"
#             elif let == str("01001111"):
#                 x = x + " " + "O"
#             elif let == str("01010000"):
#                 x = x + " " + "P"
#             elif let == str("01010001"):
#                 x = x + " " + "Q"
#             elif let == str("01010010"):
#                 x = x + " " + "R"
#             elif let == str("01010011"):
#                 x = x + " " + "S"
#             elif let == str("01010100"):
#                 x = x + " " + "T"
#             elif let == str("01010101"):
#                 x = x + " " + "U"
#             elif let == str("01010110"):
#                 x = x + " " + "V"
#             elif let == str("01010111"):
#                 x = x + " " + "W"
#             elif let == str("01011000"):
#                 x = x + " " + "X"
#             elif let == str("01011001"):
#                 x = x + " " + "Y"
#             elif let == str("01011010"):
#                 x = x + " " + "Z"
#             elif let == str("00100001"):
#                 x = x + " " + "!"
#             elif let == str('00100010'):
#                 x = x + " " + '"'
#             elif let == str("00100011"):
#                 x = x + " " + "#"
#             elif let == str("00100101"):
#                 x = x + " " + "%"
#             elif let == str("00100110"):
#                 x = x + " " + "&"
#             elif let == str("00100111"):
#                 x = x + " " + "'"
#             elif let == str("00101000"):
#                 x = x + " " + "("
#             elif let == str("00101001"):
#                 x = x + " " + ")"
#             elif let == str("00101010"):
#                 x = x + " " + "*"
#             elif let == str("00101011"):
#                 x = x + " " + "+"
#             elif let == str("00101100"):
#                 x = x + " " + ","
#             elif let == str("00101101"):
#                 x = x + " " + "-"
#             elif let == str("00101110"):
#                 x = x + " " + "."
#             elif let == str("00101111"):
#                 x = x + " " + "/"
#             elif let == str("00110000"):
#                 x = x + " " + "0"
#             elif let == str("00110001"):
#                 x = x + " " + "1"
#             elif let == str("00110010"):
#                 x = x + " " + "2"
#             elif let == str("00110011"):
#                 x = x + " " + "3"
#             elif let == str("00110100"):
#                 x = x + " " + "4"
#             elif let == str("00110101"):
#                 x = x + " " + "5"
#             elif let == str("00110110"):
#                 x = x + " " + "6"
#             elif let == str("00110111"):
#                 x = x + " " + "7"
#             elif let == str("00111000"):
#                 x = x + " " + "8"
#             elif let == str("00111001"):
#                 x = x + " " + "9"
#             elif let == str("00111111"):
#                 x = x + " " + "?"
#             elif let == str("01000000"):
#                 x = x + " " + "@"
#             elif let == str("01011111"):
#                 x = x + " " + "_"
#             elif let == str("exit").lower():
#                 break
#             else:
#                 print("Finálně přeložený znak zadaný binárním kódem není v nabídce, zkuste to znovu.")
#                 input()
#             os.system("cls")
#             print(x)
