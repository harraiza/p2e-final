def dectobin(number,binary=""):
    if number==1 or number == 0:
        binary=str(number)+binary
        return binary
    else:
        binary=str(number%2) + binary
        return dectobin(number//2,binary)

print(dectobin(10))
        