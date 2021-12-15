# oliwer toth
# Tetek20
# 2021-12-15
# filhantering

def fil():
    global filnamn
    filnamn = input("Vad ska filen heta? ")
    barnnamn = input("Vad heter barnet? ")
    with open(filnamn+".txt", "a", encoding="utf8") as personal:
        personal.write(f"\nbarnet heter {barnnamn}\n\n")
        print("Skriv in vad barnet vill ha i sin önskelista, Skriv # om du vill avsluta?\n")
        personal.write(f"{barnnamn}s ÖNSKELISTA\n")
        tr = True
        while tr:
            skriv = input("vad önskar barnet sig? ")
            if "#" in skriv:
                break
            else:
                personal.write(f"{barnnamn} önskar sig: {skriv}\n")

def läsa():
    filnamn = input("vilken fil vill du öppna?(du behöver inte skriva txt)\n")
    with open(filnamn+".txt", "r", encoding="utf8") as personal:
        s = personal.readlines()
        for line in s:
            print(line,end="")

def main():
    tr = True
    while tr:
        print("vad vill du göra, önskelista, läsa en viss önskelista eller avsluta med #")
        s = input("")
        if s == str("önskelista"):
            fil()
        elif s == str("läsa"):
            läsa()
        elif s == str("#"):
            break
    

if __name__ == "__main__":
        main()