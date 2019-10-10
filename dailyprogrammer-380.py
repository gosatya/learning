import string

morse_alphabets_raw = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."

morse_dict = {key:value for key,value in zip(string.ascii_lowercase, morse_alphabets_raw.split(" "))}

def smorse(word):
    output = ""
    for w in word:
        output += morse_dict.get(w)
    return output

print(smorse('daily'))