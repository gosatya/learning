def right_justify(s):
    lengthString = len(s)
    newString = (70 - lengthString) * ' ' + s
    return newString


print(right_justify('Satyawrat'))
print(right_justify('Janghu'))
