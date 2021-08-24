n1 = int(input("como é seu nome ?"))
n2 = int(input("seu numero é"))
print(f"seu nome é {n1 + n2:=^20}!")
print(f"seu segundo nome é {n1} e seu numero é {n2}")
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
##há duas formas de fazer o .format. ex 1- print(f"{variavel} {variavel2}") ou print("{}". format(variavel/s))

print(f"escrevendo a soma {s}  a divisão {d:.3f}, a multiplicação {m}, a divisão inteira {di} e a exponenciação {e}")
