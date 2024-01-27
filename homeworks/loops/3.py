login = input('create a login:  ')
incorrectSymbols = ""
for i in login:
    if i == "=" or i == "?" or i == "^" or i == "$" or i == "№" or i == "@" or i == "_":
        incorrectSymbols += i
        incorrectSymbols += " "
if incorrectSymbols != "":
    print(f"Убери эти символы из логина {incorrectSymbols}")
else:
    print("хороший логин")
